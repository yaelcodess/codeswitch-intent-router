import pandas as pd

from src.tagger import tag_token, tokenize

data = pd.read_csv("data/taglish_dataset.csv").set_index("id")
gold = pd.read_csv("data/gold_tokens.csv")

correct = 0
total = 0
for sid, rows in gold.groupby("id"):
    tokens = tokenize(data.loc[sid, "text"])
    expected = list(rows.sort_values("token_index")["tag"])
    predicted = [tag_token(t) for t in tokens]
    if len(tokens) != len(expected):
        print(f"id {sid}: token count differs ({len(tokens)} vs {len(expected)})")
        continue
    for tok, exp, pred in zip(tokens, expected, predicted):
        total += 1
        if exp == pred:
            correct += 1
        else:
            print(f"id {sid}: {tok!r} gold={exp} tagger={pred}")

print(f"{correct}/{total} tokens match the gold tags")