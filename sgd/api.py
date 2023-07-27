"""
sgd/api
~~~~~~~
"""

import inspect
from functools import lru_cache

import requests

from sgd.constants import genes_to_loci
from sgd.exceptions import InvalidGene


class BaseAPI:
    _base_endpoint = ""
    _id = ""

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    @lru_cache(maxsize=128)
    def get_response_for_endpoint(self, addl_endpoint=None):
        """Gets response for an endpoint.

        Returns:
            requests.models.Response: Endpoint response.
        """
        endpoint = "/".join(filter(lambda x: x, (self._base_endpoint, self._id, addl_endpoint)))
        url = f"https://www.yeastgenome.org/backend/{endpoint}"
        r = requests.get(url, **self._kwargs)
        r.raise_for_status()
        return r


class locus(BaseAPI):
    def __init__(self, locus_id, **kwargs):
        super().__init__(**kwargs)
        self.locus_id = self._id = locus_id.upper()
        self._kwargs = kwargs
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a locus.

        Returns:
            requests.models.Response: Locus details.
        """
        # Pair base URL endpoint with locus ID
        return self.get_response_for_endpoint()

    @property
    def go_details(self):
        """Gets GO (gene ontology) annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus GO details.
        """
        # Pair base URL endpoint with locus ID and terminal endpoint (i.e., this method's name)
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def interaction_details(self):
        """Gets interaction annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus interaction details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def literature_details(self):
        """Gets references which refer to a gene, organized by subject of relevance.

        Returns:
            requests.models.Response: Locus literature details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def neighbor_sequence_details(self):
        """Gets get sequences for neighboring loci in the strains for which they are available.

        Returns:
            requests.models.Response: Locus neighbor sequence details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def phenotype_details(self):
        """Gets phenotype annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus phenotype details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def posttranslational_details(self):
        """Gets posttranslational protein data.

        Returns:
            requests.models.Response: Locus posttranslational details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def protein_domain_details(self):
        """Gets protein domains, their sources, and their positions relative to protein sequence.

        Returns:
            requests.models.Response: Locus protein domain details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def protein_experiment_details(self):
        """Gets metadata and data values for protein experiments.

        Returns:
            requests.models.Response: Locus protein experiment details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def regulation_details(self):
        """Gets regulation annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus regulation details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)

    @property
    def sequence_details(self):
        """Gets sequence for genomic, coding, protein, and +/- 1KB sequence.

        Returns:
            requests.models.Response: Locus sequence details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)


class gene(locus):
    def __init__(self, gene, **kwargs):
        super().__init__(self._get_locus_id_from_gene(gene, **kwargs))
        self._base_endpoint = self.__class__.__base__.__name__

    @staticmethod
    def _get_locus_id_from_gene(gene):
        """Gets locus ID for gene.

        Args:
            gene (str): Gene to convert to locus ID.

        Raises:
            InvalidGene: SGD does not recognize gene.

        Returns:
            str: Locus ID for gene.
        """
        try:
            return genes_to_loci[gene.upper()]
        except KeyError as e:
            raise InvalidGene(f"Could not find gene with name '{gene}'.") from e


class phenotype(BaseAPI):
    def __init__(self, phenotype_name, **kwargs):
        super().__init__(**kwargs)
        self.phenotype_name = self._id = phenotype_name
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a phenotype.

        Returns:
            requests.models.Response: Phenotype details.
        """
        return self.get_response_for_endpoint()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.

        Returns:
            requests.models.Response: Phenotype locus details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)


class go(BaseAPI):
    def __init__(self, go_id, **kwargs):
        super().__init__(**kwargs)
        # Convert simple numeric ID to GO ID if needed
        self.go_id = self._id = f"GO:{go_id}" if go_id.isdigit() else go_id.upper()
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a GO term.

        Returns:
            requests.models.Response: GO details.
        """
        return self.get_response_for_endpoint()

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a GO term.

        Returns:
            requests.models.Response: GO locus details.
        """
        return self.get_response_for_endpoint(addl_endpoint=inspect.currentframe().f_code.co_name)
