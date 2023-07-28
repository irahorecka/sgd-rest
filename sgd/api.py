"""
sgd/api
~~~~~~~
"""

from functools import lru_cache

import requests

from sgd.constants import GENES_TO_LOCI
from sgd.exceptions import InvalidGene


class BaseAPI:
    _base_endpoint = ""
    endpoints = {}

    def __init__(self, id, **kwargs):
        self._id = id
        self._kwargs = kwargs

    @lru_cache(maxsize=64)
    def get_endpoint_response(self, addl_endpoint=None):
        """Gets response for an endpoint.

        Args:
            addl_endpoint (str | None, optional): Additional endpoint to append to URL.

        Returns:
            requests.models.Response: Endpoint response.
        """
        endpoint = "/".join(filter(lambda x: x, (self._base_endpoint, self._id, addl_endpoint)))
        url = f"https://www.yeastgenome.org/backend/{endpoint}"
        response = requests.get(url, **self._kwargs)
        response.raise_for_status()
        return response


class locus(BaseAPI):
    """SGD REST locus API."""

    _base_endpoint = "locus"
    endpoints = {
        "details": "Gets basic information about a locus.",
        "go_details": "Gets GO (gene ontology) annotations and the references used to make them.",
        "interaction_details": "Gets interaction annotations and the references used to make them.",
        "literature_details": "Gets references which refer to a gene, organized by subject of relevance.",
        "neighbor_sequence_details": "Gets get sequences for neighboring loci in the strains for which they are available.",
        "phenotype_details": "Gets phenotype annotations and the references used to make them.",
        "posttranslational_details": "Gets posttranslational protein data.",
        "protein_domain_details": "Gets protein domains, their sources, and their positions relative to protein sequence.",
        "protein_experiment_details": "Gets metadata and data values for protein experiments.",
        "regulation_details": "Gets regulation annotations and the references used to make them.",
        "sequence_details": "Gets sequence for genomic, coding, protein, and +/- 1KB sequence.",
    }

    def __init__(self, locus_id, **kwargs):
        self.locus_id = locus_id.upper()
        super().__init__(self.locus_id, **kwargs)

    @property
    def details(self):
        """Gets basic information about a locus.

        Returns:
            requests.models.Response: Locus details.
        """
        return self.get_endpoint_response()

    @property
    def go_details(self):
        """Gets GO (gene ontology) annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus GO details.
        """
        return self.get_endpoint_response(addl_endpoint="go_details")

    @property
    def interaction_details(self):
        """Gets interaction annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus interaction details.
        """
        return self.get_endpoint_response(addl_endpoint="interaction_details")

    @property
    def literature_details(self):
        """Gets references which refer to a gene, organized by subject of relevance.

        Returns:
            requests.models.Response: Locus literature details.
        """
        return self.get_endpoint_response(addl_endpoint="literature_details")

    @property
    def neighbor_sequence_details(self):
        """Gets get sequences for neighboring loci in the strains for which they are available.

        Returns:
            requests.models.Response: Locus neighbor sequence details.
        """
        return self.get_endpoint_response(addl_endpoint="neighbor_sequence_details")

    @property
    def phenotype_details(self):
        """Gets phenotype annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus phenotype details.
        """
        return self.get_endpoint_response(addl_endpoint="phenotype_details")

    @property
    def posttranslational_details(self):
        """Gets posttranslational protein data.

        Returns:
            requests.models.Response: Locus posttranslational details.
        """
        return self.get_endpoint_response(addl_endpoint="posttranslational_details")

    @property
    def protein_domain_details(self):
        """Gets protein domains, their sources, and their positions relative to protein sequence.

        Returns:
            requests.models.Response: Locus protein domain details.
        """
        return self.get_endpoint_response(addl_endpoint="protein_domain_details")

    @property
    def protein_experiment_details(self):
        """Gets metadata and data values for protein experiments.

        Returns:
            requests.models.Response: Locus protein experiment details.
        """
        return self.get_endpoint_response(addl_endpoint="protein_experiment_details")

    @property
    def regulation_details(self):
        """Gets regulation annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus regulation details.
        """
        return self.get_endpoint_response(addl_endpoint="regulation_details")

    @property
    def sequence_details(self):
        """Gets sequence for genomic, coding, protein, and +/- 1KB sequence.

        Returns:
            requests.models.Response: Locus sequence details.
        """
        return self.get_endpoint_response(addl_endpoint="sequence_details")


class gene(locus):
    """SGD REST locus API from gene name."""

    # Class variables are inherited as-is from `locus`
    def __init__(self, gene_name, **kwargs):
        self.gene_name = gene_name.upper()
        try:
            super().__init__(GENES_TO_LOCI[self.gene_name], **kwargs)
        except KeyError as e:
            raise InvalidGene(f"Could not find gene with name '{gene_name}'.") from e


class phenotype(BaseAPI):
    """SGD REST phenotype API."""

    _base_endpoint = "phenotype"
    endpoints = {
        "details": "Gets basic information about a phenotype.",
        "locus_details": "Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.",
    }

    def __init__(self, phenotype_name, **kwargs):
        self.phenotype_name = phenotype_name
        super().__init__(self.phenotype_name, **kwargs)

    @property
    def details(self):
        """Gets basic information about a phenotype.

        Returns:
            requests.models.Response: Phenotype details.
        """
        return self.get_endpoint_response()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.

        Returns:
            requests.models.Response: Phenotype locus details.
        """
        return self.get_endpoint_response(addl_endpoint="locus_details")


class go(BaseAPI):
    """SGD REST GO (gene ontology) API."""

    _base_endpoint = "go"
    endpoints = {
        "details": "Gets basic information about a GO term.",
        "locus_details": "Gets a list of genes annotated to a GO term.",
    }

    def __init__(self, go_id, **kwargs):
        # Convert simple numeric ID to GO ID if needed
        self.go_id = f"GO:{go_id}" if go_id.isdigit() else go_id.upper()
        super().__init__(self.go_id, **kwargs)

    @property
    def details(self):
        """Gets basic information about a GO term.

        Returns:
            requests.models.Response: GO details.
        """
        return self.get_endpoint_response()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a GO term.

        Returns:
            requests.models.Response: GO locus details.
        """
        return self.get_endpoint_response(addl_endpoint="locus_details")
