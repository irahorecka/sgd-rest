"""
sgd/constants
~~~~~~~~~~~~~
"""

import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

with open(DATA_PATH / "genes_to_loci.json", "r", encoding="utf-8") as f:
    GENES_TO_LOCI = json.load(f)
