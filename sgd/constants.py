"""
sgd/constants
~~~~~~~~~~~~~
"""

import json
from pathlib import Path


def read_json(filepath, **kwargs):
    """Reads and returns .json `filepath` as dictionary.

    Args:
        filepath (str | pathlib.Path): Filepath of JSON file to read.
        **kwargs (Any): Kwargs to pass to `json.load`.

    Returns:
        dict: Dictionary representation of JSON file as specified in `filepath`.
    """
    with open(filepath, "r") as f:
        data = json.load(f, **kwargs)
    return data


genes_to_loci = read_json(Path(__file__).parent / "data" / "genes_to_loci.json")
