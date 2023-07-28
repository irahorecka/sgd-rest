"""
tests/test_exceptions
~~~~~~~~~~~~~~~~~~~~~
"""

import pytest

import sgd
from sgd.exceptions import InvalidGene


def test_bad_gene():
    """Tests proper raise of `InvalidGene` when using an unregistered gene."""
    with pytest.raises(InvalidGene):
        sgd.gene("BadGene")
