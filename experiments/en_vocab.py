from collections import Counter

import pandas as pd

from src.tagger import tag_sentence

df = pd.read_csv("data/taglish_dataset.csv")
taglish = df[df.language_pattern == "Taglish"]

counts = Counter()
for text in taglish.text:
    for token, tag in tag_sentence(text):
        if tag == "EN":
            counts[token.lower()] += 1

print(len(counts), "unique EN words in Taglish rows")
print(", ".join(sorted(counts)))