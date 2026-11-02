import pytest

from src.density import density
from src.tagger import switch_count, switch_rate, tag_sentence, tag_token


def test_numbers_and_brands_are_ne():
    assert tag_token("137") == "NE"
    assert tag_token("GCash") == "NE"
    assert tag_token("TOR") == "NE"


def test_affixed_english_root_is_en():
    assert tag_token("i-request") == "EN"
    assert tag_token("Nag-deposit") == "EN"
    assert tag_token("nagre-reflect") == "EN"


def test_tagalog_function_words():
    for word in ["ko", "na", "ba", "yung", "po", "bang", "kong"]:
        assert tag_token(word) == "TL"


def test_filipinized_spanish_words_are_tl():
    assert tag_token("klase") == "TL"
    assert tag_token("Huwebes") == "TL"


def test_english_spelling_is_en():
    for word in ["clearance", "tuition", "so", "or"]:
        assert tag_token(word) == "EN"


def test_punctuation_is_removed():
    tokens = [t for t, _ in tag_sentence("Pwede ba magbayad ng tuition using GCash?")]
    assert tokens[-1] == "GCash"


def test_switch_count_ignores_ne():
    assert switch_count(["TL", "TL", "EN", "TL"]) == 2
    assert switch_count(["EN", "EN"]) == 0
    assert switch_count(["TL", "NE", "EN"]) == 1


def test_switch_rate():
    assert switch_rate(["TL", "EN", "TL", "EN"]) == 1.0
    assert switch_rate(["TL"]) == 0.0


def test_full_sentence_density():
    text = "Hindi pa lumalabas yung grades ko sa portal, kailan kaya mauupload?"
    tags = [t for _, t in tag_sentence(text)]
    assert density(tags) == pytest.approx(3 / 11)