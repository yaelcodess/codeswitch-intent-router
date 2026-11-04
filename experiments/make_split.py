import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

THRESHOLD = 0.5
SEED = 42
TARGETS = {"train": 0.70, "validation": 0.15, "test": 0.15}

df = pd.read_csv("data/taglish_dataset.csv")

# Link near-paraphrases: same intent and similar wording.
vectors = TfidfVectorizer(lowercase=True).fit_transform(df["text"])
similarity = cosine_similarity(vectors)
intents = df["intent"].to_numpy()
same_intent = intents[:, None] == intents[None, :]
linked = (similarity >= THRESHOLD) & same_intent
n_groups, group = connected_components(csr_matrix(linked), directed=False)
df["group"] = group

# Assign whole groups to splits, separately for each intent.
rng = np.random.default_rng(SEED)
df["split"] = ""
for intent, part in df.groupby("intent"):
    sizes = part.groupby("group").size()
    group_ids = list(sizes.index)
    rng.shuffle(group_ids)
    total = len(part)
    filled = {name: 0 for name in TARGETS}
    for g in group_ids:
        # Give the group to the split furthest below its target size.
        name = max(TARGETS, key=lambda s: TARGETS[s] * total - filled[s])
        df.loc[(df["intent"] == intent) & (df["group"] == g), "split"] = name
        filled[name] += sizes[g]

df[["id", "intent", "language_pattern", "group", "split"]].to_csv(
    "data/splits.csv", index=False
)

print(f"{n_groups} groups, largest has {np.bincount(group).max()} sentences")
print()
print(df.groupby(["split", "intent"]).size().unstack(0))
print()
print(df.groupby(["split", "language_pattern"]).size().unstack(0))
print()
print("Linked groups (sentences treated as paraphrases):")
multi = df.groupby("group").filter(lambda g: len(g) > 1)
for gid, g in list(multi.groupby("group"))[:8]:
    print(f"group {gid} -> {g['split'].iloc[0]}")
    for text in g["text"]:
        print("   ", text)