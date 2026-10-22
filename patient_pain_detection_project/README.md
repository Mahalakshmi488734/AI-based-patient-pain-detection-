# AI-Based Non-Communicative Patient Pain Detection — Starter Prototype

## Overview
A small Streamlit starter app for an educational project exploring the challenges of assessing pain in patients who cannot communicate verbally.

**Important limitation:** Facial expressions alone cannot reliably determine a person's pain. This starter project does not diagnose pain and does not make predictions. It only demonstrates an image-upload interface.

## Features
- Upload a JPG, JPEG, or PNG image.
- Preview the uploaded image.
- Display a clear message that no trained model is included.
- Includes a placeholder for planning a future training pipeline.

## Requirements
- Python 3.10 or newer
- pip

## Run locally

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Training
`train_model.py` is intentionally a placeholder. It does not train a model until a properly licensed, ethically sourced, labelled dataset and a validated training pipeline are provided.

## Suggested next steps
1. Decide on a clearly defined research objective and dataset.
2. Review dataset licensing, consent, privacy, and potential bias.
3. Create a reproducible train/validation/test split.
4. Evaluate using suitable metrics and document limitations.
5. Do not use the output for diagnosis or clinical decisions.

## Safety and privacy
Do not upload identifiable patient photos without appropriate permission. Do not use this prototype for clinical decisions.
