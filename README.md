# sgd-rest

Saccharomyces Genome Database ([SGD](https://www.yeastgenome.org/)) REST API wrapper. Refer to the [SGD REST](https://www.yeastgenome.org/api/doc) page for information about API usage and terms of service.

[![pypiv](https://img.shields.io/pypi/v/sgd-rest.svg)](https://pypi.python.org/pypi/sgd-rest)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![continuous-integration](https://github.com/irahorecka/sgd-rest/workflows/continuous-integration/badge.svg?branch=main)](https://github.com/irahorecka/sgd-rest/actions)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/irahorecka/sgd-rest/main/LICENSE)

## Installation

```bash
pip install sgd-rest
```

## Quick start

Get GO (gene ontology) information for gene ARO1.

```python
import sgd

aro1 = sgd.gene("ARO1")
aro1.go_details.json()
```

## Background

Navigate the SGD REST API with Python.

### Classes

| Class | Description | Example |
| ----- | ----------- | ------- |
| `locus` | Query SGD REST using locus ID. | `locus("S000002534")` |
| `gene` | Query SGD REST using gene name. | `gene("ARO1")` |
| `phenotype` | Query SGD REST using phenotype name. | `phenotype("increased_chemical_compound_accumulation")` |
| `go` | Query SGD REST using GO ID. | `go("GO:0000001")` |

First, instantiate an SGD class prior to working with subclasses:

```python
import sgd

aro1 = sgd.gene("ARO1")
```

### Subclasses

Use the `endpoints` attribute to search a class's subclasses:

```python
import sgd

print(sgd.gene.endpoints)
```

| Class | Subclass | Description |
| ----- | -------- | ----------- |
| `locus` & `gene` | `details` | Gets basic information about a locus.
| `locus` & `gene` | `go_details` | Gets GO (gene ontology) annotations and the references used to make them.
| `locus` & `gene` | `interaction_details` | Gets interaction annotations and the references used to make them.
| `locus` & `gene` | `literature_details` | Gets references which refer to a gene, organized by subject of relevance.
| `locus` & `gene` | `neighbor_sequence_details` | Gets get sequences for neighboring loci in the strains for which they are available.
| `locus` & `gene` | `phenotype_details` | Gets phenotype annotations and the references used to make them.
| `locus` & `gene` | `posttranslational_details` | Gets posttranslational protein data.
| `locus` & `gene` | `protein_domain_details` | Gets protein domains, their sources, and their positions relative to protein sequence.
| `locus` & `gene` | `protein_experiment_details` | Gets metadata and data values for protein experiments.
| `locus` & `gene` | `regulation_details` | Gets regulation annotations and the references used to make them.
| `locus` & `gene` | `sequence_details` | Gets sequence for genomic, coding, protein, and +/- 1KB sequence.
| `phenotype` | `details` | Gets basic information about a phenotype.
| `phenotype` | `locus_details` | Gets a list of genes annotated to a phenotype with some information about the experiment and strain background.
| `go` | `details` | Gets basic information about a GO term.
| `go` | `locus_details` | Gets a list of genes annotated to a GO term.

Use a subclass to retrieve the endpoint's response. This library utilizes the [`requests`](https://github.com/psf/requests) library, returning a `requests.models.Response` instance. Use this instance to define the desired processing of the REST API content.

For example, for the gene ARO1, get GO details as JSON and literature details as text:

```python
import sgd

aro1 = sgd.gene("ARO1")
aro1.go_details.json()
aro1.literature_details.text
```

## Advanced

Just like a subclass returns a `requests.models.Response` instance, the user can pass keyword arguments directly to the `requests.get` method during class instantiation. For example, you can add a header to prevent server-side caching and parse the locus details response as text:

```python
import sgd

go_0000001 = sgd.go("GO:0000001", headers={"Cache-Control": "no-cache", "Pragma": "no-cache"})
go_0000001.locus_details.text
```

## Additional attributes

* `url`: Gets the endpoint's URL. Available for all classes.
* `locus_id`: Gets the endpoint's locus ID. Avaialble for `locus` and `gene` classes.

```python
import sgd

tor2 = sgd.gene("TOR2")

# 1 
print(tor2.url)
# >>> 'https://www.yeastgenome.org/backend/locus/S000001686'

# 2
print(tor2.locus_id)
# >>> 'S000001686'
```

## Exceptions

* `InvalidGene`: An invalid gene was queried.

```python
import sgd
from sgd.exceptions import InvalidGene

try:
    bad_gene = sgd.gene("BadGene")
except InvalidGene:
    print("Whoops, an invalid gene was queried.")
```

## Contribute

* [Issues Tracker](https://github.com/irahorecka/sgd-rest/issues)
* [Source Code](https://github.com/irahorecka/sgd-rest/tree/main/sgd)

## Support

If you are having issues or would like to propose a new feature, please use the [issues tracker](https://github.com/irahorecka/sgd-rest/issues).

## License

This project is licensed under the MIT license.
