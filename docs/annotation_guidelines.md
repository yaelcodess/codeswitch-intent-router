# Token-Level Annotation Guidelines (v0.1)

## Tags
- EN: English token
- TL: Tagalog token
- NE: language-independent token (excluded from density)

## Tokenization
- Split on whitespace. Strip punctuation (. , ? !).
- Hyphenated tokens such as "i-request" stay as one token.
- Lowercase before comparing, but keep the original text.

## Rules
1. Affixed words: the ROOT decides the tag.
   "i-request", "Na-sign", "mag-enroll", "nagre-reflect" -> EN.
   "magbabayad" -> TL (Tagalog root).
2. Borrowed English words written in English spelling -> EN.
   "clearance", "tuition", "schedule", "enrollment" -> EN.
   This matches the sentence-level Rule A.
3. Filipinized or Spanish-origin words in Filipino spelling -> TL.
   "klase", "iskedyul", "semestre", "estudyante", "bangko" -> TL.
4. Names, brands, acronyms, numbers -> NE.
   "GCash", "TOR", "Math", "137" -> NE.
5. Function words follow their language:
   "ko", "na", "ba", "yung", "po", "ang", "ng" -> TL;
   "my", "I", "the", "to" -> EN.
6. Ambiguous token: tag by the more likely language and record it in the notes.

## Density (defined in the next step)
Computed only over EN and TL tokens. NE tokens are ignored.