import pytest

from src.density import density, density_by_sentence


def test_single_language_is_zero():
    assert density(["TL", "TL", "TL"]) == 0.0
    assert density(["EN", "EN"]) == 0.0


def test_balanced_is_half():
    assert density(["EN", "TL", "EN", "TL"]) == 0.5


def test_same_for_either_minority_language():
    assert density(["EN", "TL", "TL", "TL"]) == density(["TL", "EN", "EN", "EN"])


def test_ne_tokens_are_ignored():
    assert density(["EN", "TL", "NE", "NE"]) == 0.5


def test_only_ne_tokens_is_zero():
    assert density(["NE", "NE"]) == 0.0


def test_gold_sentences():
    result = density_by_sentence("data/gold_tokens.csv")
    assert result[92] == pytest.approx(3 / 11)
    assert result[110] == pytest.approx(4 / 11)