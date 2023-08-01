"""
sgd/api
~~~~~~~
"""

from functools import lru_cache

import requests

from sgd.constants import GENES_TO_LOCI
from sgd.exceptions import InvalidGene


class BaseAPI:
    """Base API for SGD REST."""

    _base_endpoint = ""
    _endpoint = ""
    endpoints = {}

    def __init__(self, id, **kwargs):
        self._id = id
        self._kwargs = kwargs

    @property
    def url(self):
        """Gets URL for an endpoint.

        Returns:
            str: Endpoint URL.
        """
        endpoint = "/".join(filter(lambda x: x, (self._base_endpoint, self._id, self._endpoint)))
        return f"https://www.yeastgenome.org/backend/{endpoint}"

    @lru_cache(maxsize=64)
    def _get_endpoint_response(self):
        """Gets response for an endpoint.

        Returns:
            requests.models.Response: Endpoint response.
        """
        response = requests.get(self.url, timeout=60, **self._kwargs)
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
        self._endpoint = ""
        return self._get_endpoint_response()

    @property
    def go_details(self):
        """Gets GO (gene ontology) annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus GO details.
        """
        self._endpoint = "go_details"
        return self._get_endpoint_response()

    @property
    def interaction_details(self):
        """Gets interaction annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus interaction details.
        """
        self._endpoint = "interaction_details"
        return self._get_endpoint_response()

    @property
    def literature_details(self):
        """Gets references which refer to a gene, organized by subject of relevance.

        Returns:
            requests.models.Response: Locus literature details.
        """
        self._endpoint = "literature_details"
        return self._get_endpoint_response()

    @property
    def neighbor_sequence_details(self):
        """Gets get sequences for neighboring loci in the strains for which they are available.

        Returns:
            requests.models.Response: Locus neighbor sequence details.
        """
        self._endpoint = "neighbor_sequence_details"
        return self._get_endpoint_response()

    @property
    def phenotype_details(self):
        """Gets phenotype annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus phenotype details.
        """
        self._endpoint = "phenotype_details"
        return self._get_endpoint_response()

    @property
    def posttranslational_details(self):
        """Gets posttranslational protein data.

        Returns:
            requests.models.Response: Locus posttranslational details.
        """
        self._endpoint = "posttranslational_details"
        return self._get_endpoint_response()

    @property
    def protein_domain_details(self):
        """Gets protein domains, their sources, and their positions relative to protein sequence.

        Returns:
            requests.models.Response: Locus protein domain details.
        """
        self._endpoint = "protein_domain_details"
        return self._get_endpoint_response()

    @property
    def protein_experiment_details(self):
        """Gets metadata and data values for protein experiments.

        Returns:
            requests.models.Response: Locus protein experiment details.
        """
        self._endpoint = "protein_experiment_details"
        return self._get_endpoint_response()

    @property
    def regulation_details(self):
        """Gets regulation annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus regulation details.
        """
        self._endpoint = "regulation_details"
        return self._get_endpoint_response()

    @property
    def sequence_details(self):
        """Gets sequence for genomic, coding, protein, and +/- 1KB sequence.

        Returns:
            requests.models.Response: Locus sequence details.
        """
        self._endpoint = "sequence_details"
        return self._get_endpoint_response()


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
        self._endpoint = ""
        return self._get_endpoint_response()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.

        Returns:
            requests.models.Response: Phenotype locus details.
        """
        self._endpoint = "locus_details"
        return self._get_endpoint_response()


class go(BaseAPI):
    """SGD REST GO (gene ontology) API."""

    _base_endpoint = "go"
    endpoints = {
        "details": "Gets basic information about a GO term.",
        "locus_details": "Gets a list of genes annotated to a GO term.",
    }

    def __init__(self, go_id, **kwargs):
        self.go_id = go_id.upper()
        super().__init__(self.go_id, **kwargs)

    @property
    def details(self):
        """Gets basic information about a GO term.

        Returns:
            requests.models.Response: GO details.
        """
        self._endpoint = ""
        return self._get_endpoint_response()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a GO term.

        Returns:
            requests.models.Response: GO locus details.
        """
        self._endpoint = "locus_details"
        return self._get_endpoint_response()
