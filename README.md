# Taglish Router

An AI-powered routing system that investigates how
code-switching between Tagalog and English affects
language model performance.

## Research Objectives

- Detect intra-sentence language switching.
- Calculate code-switch density.
- Select matching few-shot examples.
- Evaluate LLM intent-classification accuracy.
- Implement a human handoff mechanism.

The longer-term research questions are whether model confidence tracks
actual accuracy as code-switching density increases, whether
density-matched Taglish few-shot examples improve classification, and
where a sensible human-handoff threshold lies.

## Initial Research Scope

- Language pair: Tagalog-English
- Domain: Campus Registrar Inquiries
- Primary task: Intent Classification
- Programming language: Python

## Intent Categories

- enrollment_status
- document_request
- class_schedule
- tuition_payment
- student_records
- clearance

## Technology Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pytest

## Project Status

This is a compressed 7-day MVP. It does not claim to test the full research hypothesis.

- Day 1: Project initialization. Done.
- Day 2: Dataset creation. Done. 120 synthetic utterances.
- Day 3: Token-level language annotation and density formula. Next.

## Dataset

File: `data/taglish_dataset.csv`

Columns: `id, text, intent, language_pattern, source, split`

- 120 synthetic utterances, 20 per intent.
- `language_pattern` counts: Taglish 60, English 31, Tagalog 29.
- `source` is `synthetic` for all rows.
- `split` is `unassigned` until the train/validation/test split is made.
- `split` is a placeholder (`unassigned`) in this file; see `data/splits.csv`.

### Language pattern labels

`language_pattern` is a sentence-level label:

- **English**: no Tagalog tokens.
- **Tagalog**: no English content words.
- **Taglish**: both present.

These labels are rough categories. They are separate from token-level
language annotation, which will be used to compute code-switching density.

## Limitations

- The dataset is small and synthetic, written by a small number of authors.
  It does not capture real student writing, typos, slang or spelling variants.
- Many examples are near-paraphrases of each other. The train/validation/test
  split must be grouped by paraphrase to avoid data leakage.
- Borrowed terms (for example "clearance", "tuition") and affixed English
  roots (for example "i-request") are ambiguous. They will be handled
  explicitly in the token-level annotation guidelines.
- Results on this dataset do not generalize beyond it.