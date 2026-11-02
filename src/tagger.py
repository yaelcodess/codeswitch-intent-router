import re

# Names, brands and acronyms that are language-independent (Rule 4).
NE_WORDS = {"gcash", "tor"}

# Tagalog prefixes that can attach to an English root (Rule 1).
TL_AFFIXES = {
    "nag", "mag", "na", "ma", "i", "ipa", "ipapa", "pa", "ka", "naka",
    "nagre", "mache", "maka", "pag", "pinag",
}

# Tagalog words (function words and the content words seen in the dataset).
# Anything not listed is treated as English. Extend this list when the
# gold check shows a missing word.
TL_WORDS = {
    # function words
    "ako", "ko", "mo", "ka", "ba", "bang", "na", "pa", "rin", "din", "ang",
    "ng", "sa", "yung", "mga", "para", "pero", "kung", "kasi", "hindi",
    "wala", "walang", "may", "ano", "saan", "paano", "kailan", "bakit",
    "sino", "gusto", "kong", "akong", "aking", "namin", "po", "sana", "daw",
    "ay", "dito", "rito", "nang", "ngayong", "ngayon", "bukas", "tuwing",
    "hanggang", "bago", "kaya", "dahil", "noong", "nakaraang", "unang",
    "huli", "pwede", "maaari", "dapat", "pang", "lang", "ba",
    # content words
    "kailangan", "malaman", "malalaman", "makita", "makikita", "makuha",
    "makukuha", "makakuha", "makakakuha", "kumuha", "kopya", "marka",
    "iskedyul", "klase", "oras", "magbayad", "magbabayad", "pagbabayad",
    "pagbabayad", "matrikula", "paraan", "tapusin", "tapos", "dokumento",
    "humiling", "humingi", "sertipiko", "sertipikasyon", "katibayan",
    "pagtatapos", "nakalista", "nakatala", "pagpapatala", "natanggap",
    "pangalan", "bayad", "bayarin", "kulang", "magkano", "hulugan",
    "ipagpaliban", "katapusan", "buwan", "tanggapan", "daanan", "makalabas",
    "paaralan", "utang", "magpapatunay", "estudyante", "papel", "kausapin",
    "talaan", "pagkakamali", "maitatama", "lumalabas", "lumabas", "linggo",
    "pasok", "araw", "lunes", "martes", "miyerkules", "huwebes", "biyernes",
    "gaganapin", "natatapos", "nawala", "nakalagay", "tama", "mali",
    "tumatanggap", "bangko", "pamamagitan", "bawasan", "semestre",
    "gagawin", "pipirma", "humiling", "magkakaroon",
    "nagbayad", "nakakuha", "kulang", "ilang", "gaano", "katagal", "magkano",
    "aling", "anong", "sino",
    "magsisimula", "huling", "paghiling", "opisyal", "listahan", "kayo",
    "kukuha",
    "alam", "ibibigay", "kumpleto", "pumunta", "nasaan", "trabaho",
}


def tokenize(text):
    """Split into words. Punctuation is dropped; hyphens and apostrophes stay."""
    return re.findall(r"[\w'-]+", text)


def tag_token(token):
    """Return 'EN', 'TL' or 'NE' for one token, following the guideline rules."""
    low = token.lower()
    if low.isdigit() or low in NE_WORDS:
        return "NE"
    if "-" in low:
        prefix, root = low.split("-", 1)
        if prefix in TL_AFFIXES and root:
            return tag_token(root)
    if low in TL_WORDS:
        return "TL"
    return "EN"


def tag_sentence(text):
    """Return a list of (token, tag) pairs."""
    return [(t, tag_token(t)) for t in tokenize(text)]


def switch_count(tags):
    """Number of times the language changes between neighbouring EN/TL tokens."""
    seq = [t for t in tags if t in ("EN", "TL")]
    return sum(1 for a, b in zip(seq, seq[1:]) if a != b)


def switch_rate(tags):
    """Switches divided by the number of token boundaries (0 to 1)."""
    seq = [t for t in tags if t in ("EN", "TL")]
    if len(seq) < 2:
        return 0.0
    return switch_count(tags) / (len(seq) - 1)