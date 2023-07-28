"""
tests/test_api
~~~~~~~~~~~~~~
"""

import requests
from pytest import mark

import sgd


# fmt: off
locus_gene_attributes = (
    (sgd.locus, "S000002534", "S000002534", "https://www.yeastgenome.org/backend/locus/S000002534"),
    (sgd.gene, "ARO1", "S000002534", "https://www.yeastgenome.org/backend/locus/S000002534"),
)
# fmt: on
@mark.parametrize("attributes", locus_gene_attributes)
def test_locus_gene_attributes(attributes):
    """Test proper instance attributes for locus and gene classes.

    Args:
        attributes (tuple): Args to unpack for constructing and testing proper instance attributes.
    """
    sgd_obj, arg, locus_id, url = attributes
    sgd_inst = sgd_obj(arg)
    assert sgd_inst.locus_id == locus_id
    assert sgd_inst.url == url


# fmt: off
phenotype_go_attributes = (
    (sgd.phenotype, "increased_chemical_compound_accumulation", "https://www.yeastgenome.org/backend/phenotype/increased_chemical_compound_accumulation"),
    (sgd.go, "GO:0000001", "https://www.yeastgenome.org/backend/go/GO:0000001"),
)
# fmt: on
@mark.parametrize("attributes", phenotype_go_attributes)
def test_phenotype_go_attributes(attributes):
    """Test proper instance attributes for phenotype and GO classes.

    Args:
        attributes (tuple): Args to unpack for constructing and testing proper instance attributes.
    """
    sgd_obj, arg, url = attributes
    sgd_inst = sgd_obj(arg)
    assert sgd_inst.url == url


# fmt: off
locus_gene_constructors = (
    (sgd.locus, "S000002534"),
    (sgd.gene, "ARO1"),
)
# fmt: on
@mark.parametrize("constructor", locus_gene_constructors)
def test_locus_gene_endpoints(constructor):
    """Test proper responses from locus and gene endpoints.

    Args:
        constructor (tuple): Args to unpack for constructing and testing proper endpoint responses.
    """
    sgd_class, arg = constructor
    # Requests throws SSLError during testing - suppress error
    sgd_inst = sgd_class(arg, verify=False)
    details = sgd_inst.details
    go_details = sgd_inst.go_details
    interaction_details = sgd_inst.interaction_details
    literature_details = sgd_inst.literature_details
    neighbor_sequence_details = sgd_inst.neighbor_sequence_details
    phenotype_details = sgd_inst.phenotype_details
    posttranslational_details = sgd_inst.posttranslational_details
    protein_domain_details = sgd_inst.protein_domain_details
    protein_experiment_details = sgd_inst.protein_experiment_details
    regulation_details = sgd_inst.regulation_details
    sequence_details = sgd_inst.sequence_details
    # Assert HTTP response object
    assert isinstance(details, requests.models.Response)
    assert isinstance(go_details, requests.models.Response)
    assert isinstance(interaction_details, requests.models.Response)
    assert isinstance(literature_details, requests.models.Response)
    assert isinstance(neighbor_sequence_details, requests.models.Response)
    assert isinstance(phenotype_details, requests.models.Response)
    assert isinstance(posttranslational_details, requests.models.Response)
    assert isinstance(protein_domain_details, requests.models.Response)
    assert isinstance(protein_experiment_details, requests.models.Response)
    assert isinstance(regulation_details, requests.models.Response)
    assert isinstance(sequence_details, requests.models.Response)
    # Assert HTTP response status code is 200
    assert details.status_code == 200
    assert go_details.status_code == 200
    assert interaction_details.status_code == 200
    assert literature_details.status_code == 200
    assert neighbor_sequence_details.status_code == 200
    assert phenotype_details.status_code == 200
    assert posttranslational_details.status_code == 200
    assert protein_domain_details.status_code == 200
    assert protein_experiment_details.status_code == 200
    assert regulation_details.status_code == 200
    assert sequence_details.status_code == 200


# fmt: off
phenotype_go_constructors = (
    (sgd.phenotype, "increased_chemical_compound_accumulation"),
    (sgd.go, "GO:0000001"),
)
# fmt: on
@mark.parametrize("constructor", phenotype_go_constructors)
def test_phenotype_go_endpoints(constructor):
    """Test proper responses from phenotype and GO endpoints.

    Args:
        constructor (tuple): Args to unpack for constructing and testing proper endpoint responses.
    """
    sgd_class, arg = constructor
    # Requests throws SSLError during testing - suppress error
    sgd_inst = sgd_class(arg, verify=False)
    details = sgd_inst.details
    locus_details = sgd_inst.locus_details
    # Assert HTTP response object
    assert isinstance(details, requests.models.Response)
    assert isinstance(locus_details, requests.models.Response)
    # Assert HTTP response status code is 200
    assert details.status_code == 200
    assert locus_details.status_code == 200
