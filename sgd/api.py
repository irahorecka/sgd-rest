import inspect
from functools import lru_cache

import requests

from sgd.constants import genes_to_loci


class InvalidGene(Exception):
    pass


class BaseAPI:
    endpoint = ""

    def __init__(self):
        pass

    @property
    def url(self):
        return f"https://www.yeastgenome.org/backend/{self.endpoint}"

    @lru_cache(maxsize=128)
    def get_response(self, *args, **kwargs):
        """Gets response for instance URL.

        Returns:
            requests.models.Response: Instance URL response.
        """
        r = requests.get(self.url, *args, **kwargs)
        r.raise_for_status()
        return r


class locus(BaseAPI):
    def __init__(self, locus_id, *args, **kwargs):
        super().__init__()
        self.locus_id = locus_id.upper()
        self._args = args
        self._kwargs = kwargs
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a locus.

        Returns:
            requests.models.Response: Locus details.
        """
        # Pair base URL endpoint with locus ID
        self.endpoint = f"{self._base_endpoint}/{self.locus_id}"
        return self.get_response(*self._args, **self._kwargs)

    @property
    def go_details(self):
        """Gets GO (gene ontology) annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus GO details.
        """
        # Pair base URL endpoint with locus ID and terminal endpoint (i.e., this method's name)
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def interaction_details(self):
        """Gets interaction annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus interaction details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def literature_details(self):
        """Gets references which refer to a gene, organized by subject of relevance.

        Returns:
            requests.models.Response: Locus literature details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def neighbor_sequence_details(self):
        """Gets get sequences for neighboring loci in the strains for which they are available.

        Returns:
            requests.models.Response: Locus neighbor sequence details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def phenotype_details(self):
        """Gets phenotype annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus phenotype details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def posttranslational_details(self):
        """Gets posttranslational protein data.

        Returns:
            requests.models.Response: Locus posttranslational details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def protein_domain_details(self):
        """Gets protein domains, their sources, and their positions relative to protein sequence.

        Returns:
            requests.models.Response: Locus protein domain details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def protein_experiment_details(self):
        """Gets metadata and data values for protein experiments.

        Returns:
            requests.models.Response: Locus protein experiment details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def regulation_details(self):
        """Gets regulation annotations and the references used to make them.

        Returns:
            requests.models.Response: Locus regulation details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)

    @property
    def sequence_details(self):
        """Gets sequence for genomic, coding, protein, and +/- 1KB sequence.

        Returns:
            requests.models.Response: Locus sequence details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.locus_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)


class gene(locus):
    def __init__(self, gene, *args, **kwargs):
        super().__init__(self._get_locus_id_from_gene(gene, *args, **kwargs))
        self._base_endpoint = locus.__name__

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
    def __init__(self, phenotype_name, *args, **kwargs):
        super().__init__()
        self.phenotype_name = phenotype_name
        self._args = args
        self._kwargs = kwargs
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a phenotype.

        Returns:
            requests.models.Response: Phenotype details.
        """
        self.endpoint = f"{self._base_endpoint}/{self.phenotype_name}"
        return self.get_response(*self._args, **self._kwargs)

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.

        Returns:
            requests.models.Response: Phenotype locus details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.phenotype_name}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)


class go(BaseAPI):
    def __init__(self, go_id, *args, **kwargs):
        super().__init__()
        # Convert simple numeric ID to GO ID if needed
        self.go_id = f"GO:{go_id}" if go_id.isdigit() else go_id.upper()
        self._args = args
        self._kwargs = kwargs
        self._base_endpoint = self.__class__.__name__

    @property
    def details(self):
        """Gets basic information about a GO term.

        Returns:
            requests.models.Response: GO details.
        """
        self.endpoint = f"{self._base_endpoint}/{self.go_id}"
        return self.get_response(*self._args, **self._kwargs)

    @property
    def locus_details(self):
        """Gets a list of genes annotated to a GO term.

        Returns:
            requests.models.Response: GO locus details.
        """
        self.endpoint = (
            f"{self._base_endpoint}/{self.go_id}/{inspect.currentframe().f_code.co_name}"
        )
        return self.get_response(*self._args, **self._kwargs)
