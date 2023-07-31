"""
tests/test_constants
~~~~~~~~~~~~~~~~~~~~
"""

from pytest import mark

import sgd
from sgd.constants import GENES_TO_LOCI


# fmt: off
sgd_instances = (
    sgd.locus('S000002534'),
    sgd.gene('ARO1'),
    sgd.phenotype('increased_chemical_compound_accumulation'),
    sgd.go('GO:0000001'),
)
# fmt: on
@mark.parametrize("instance", sgd_instances)
def test_endpoints(instance):
    """Tests proper return of SGD REST endpoints.

    Args:
        instance (tuple): Args to unpack for testing proper display of instance endpoints.
    """
    assert isinstance(instance.endpoints, dict)


def test_genes_to_loci():
    """Tests proper instance of GENES_TO_LOCI variable and fetching of appropriate locus ID for gene."""
    assert isinstance(GENES_TO_LOCI, dict)
    assert GENES_TO_LOCI["ARO1"] == "S000002534"
