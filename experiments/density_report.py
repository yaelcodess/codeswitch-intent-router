import pandas as pd

from src.density import density
from src.tagger import switch_rate, tag_sentence

df = pd.read_csv("data/taglish_dataset.csv")

rows = []
for _, r in df.iterrows():
    tags = [t for _, t in tag_sentence(r["text"])]
    rows.append({
        "id": r["id"],
        "n_en": tags.count("EN"),
        "n_tl": tags.count("TL"),
        "density": density(tags),
        "switch_rate": switch_rate(tags),
    })

out = df.merge(pd.DataFrame(rows), on="id")


def implied_label(row):
    if row.n_en > 0 and row.n_tl > 0:
        return "Taglish"
    if row.n_tl > 0:
        return "Tagalog"
    return "English"


out["implied"] = out.apply(implied_label, axis=1)
bad = out[out.implied != out.language_pattern]

print(f"{len(out) - len(bad)}/{len(out)} rows: tagger agrees with the sentence label")
print(bad[["id", "text", "language_pattern", "implied"]].to_string(index=False))

out.drop(columns="implied").to_csv("data/dataset_with_density.csv", index=False)
print(out.groupby("language_pattern")["density"].describe())