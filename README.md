# AI Code Reviewer

A Streamlit app that reviews pasted code and gives structured, actionable
feedback using Google Gemini — like a first-pass senior reviewer.

## What it checks

- **Syntax validation** — flags syntax errors with an explanation and a
  corrected version of the code
- **Logical analysis** — flags logical issues (infinite loops, incorrect
  conditionals, wrong variable usage) and suggests fixes, or confirms the
  logic is sound
- **Code optimization** — recommends performance and readability
  improvements

## Tech stack

- **Streamlit** for the UI
- **Google Gemini** (`google-generativeai`) as the reviewing model

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in GEMINI_API_KEY
```

## Run

```bash
streamlit run aiicode.py
```
