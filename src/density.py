import pandas as pd


def density(tags):
    """Share of the minority language among EN and TL tags. NE is ignored."""
    en = sum(1 for t in tags if t == "EN")
    tl = sum(1 for t in tags if t == "TL")
    total = en + tl
    if total == 0:
        return 0.0
    return min(en, tl) / total


def density_by_sentence(gold_path):
    """Read the gold token file and return density per sentence id."""
    gold = pd.read_csv(gold_path)
    return gold.groupby("id")["tag"].apply(lambda tags: density(list(tags)))