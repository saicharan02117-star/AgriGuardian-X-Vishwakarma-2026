# Algorithm verification status

No labeled crop-disease evaluation dataset, model weights, predictions, or confusion matrix were supplied. Consequently, crop-classification accuracy, sensitivity, specificity, and generalization cannot be independently verified.

## Reproducible verification protocol
1. Freeze model version and preprocessing code.
2. Collect consented, labeled images by crop, disease, lighting, and camera condition.
3. Split by farm/date to avoid leakage.
4. Record predictions and compute per-class precision, recall, F1, confusion matrix and calibration.
5. Validate on an unseen field set; document failure cases.
6. Record software build and hardware board versions.

## Current evidence
Website screenshots show a prototype interface, not a validated classifier. Numerical chassis and motor models are not evidence of algorithmic diagnosis accuracy.