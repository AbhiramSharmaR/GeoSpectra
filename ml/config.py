import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "ml" / "data"

# Classification Thresholds
HIGH_RISK_THRESHOLD = 0.1
MEDIUM_RISK_THRESHOLD = 0.03
