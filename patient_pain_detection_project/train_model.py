"""
Starter placeholder for model training.

Before training:
1. Obtain a properly licensed, ethically sourced, labelled dataset.
2. Review dataset limitations, consent, privacy, and bias.
3. Define an evaluation plan with appropriate metrics and held-out test data.
4. Do not interpret facial expression labels as a clinical pain diagnosis.

This file intentionally does not train a model without a dataset.
"""

from pathlib import Path

DATASET_DIR = Path("data")

def main():
    if not DATASET_DIR.exists():
        print("No dataset found in ./data.")
        print("Add an appropriately licensed dataset and implement a validated training pipeline.")
        return

    print("Dataset directory found.")
    print("Training is not implemented in this educational starter project.")

if __name__ == "__main__":
    main()
