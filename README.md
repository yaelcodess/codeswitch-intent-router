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

## Initial Research Scope

- Language pair: Tagalog-English
- Domain: Campus Registrar Inquiries
- Primary task: Intent Classification
- Programming language: Python

## Technology Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pytest

## Project Status

Day 1: Project initialization.
Day 2: Dataset creation (in progress, 36 of 120 examples).

## Dataset

`language_pattern` is a sentence-level label. English = no Tagalog tokens; Tagalog = no English content words; Taglish = both present. Token-level annotation is done separately.