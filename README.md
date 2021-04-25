

[![PyPI version](https://badge.fury.io/py/findCPcore.svg)](https://badge.fury.io/py/findCPcore) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Documentation Status](https://readthedocs.org/projects/findcpcore/badge/?version=latest&style=flat-square)](https://findcpcore.readthedocs.io/en/latest/?badge=latest)		
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/findCP/findCPcore/HEAD?filepath=docs%2Fsource%2FCORE.ipynb)

## findCPcore - find ChokePoint reactions in genome-scale metabolic models

```findCPcore``` is a Python tool for the computation of chokepoint reactions in genome-scale metabolic models. The tool allows the calculation of chokepoints taking into account only the topology of the metabolic network or also using its dynamic information.

The documentation can be found at [readthedocs](https://findcpcore.readthedocs.io/en/latest/) and can also be [downloaded](https://findcpcore.readthedocs.io/_/downloads/en/latest/pdf/).

A command line application of the tool is provided at [findCPcli](https://github.com/findCP/findCPcli).

You can also [try it with Binder](https://mybinder.org/v2/gh/findCP/findCPcore/HEAD?filepath=docs%2Fsource%2FCORE.ipynb).

For citation purposes please refer to:

Oarga et al. "Growth Dependent Computation of Chokepoints in Metabolic Networks." International Conference on Computational Methods in Systems Biology. Springer, Cham, 2020. https://doi.org/10.1007/978-3-030-60327-4_6

## Table of Contents
- [Install](#install)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Install

```sh
$ pip install findCPcore
```

## Quickstart

Example of network refinement and chokepoint computation:

```python
from findCPcore import CobraMetabolicModel

model = CobraMetabolicModel("aureus.xml")

# update flux bounds with FVA
model.fva(update_flux=True)

# compute chokepoints
model.find_chokepoints()

# get chokepoints
model.chokepoints()
```

## Maintainers

[@alexOarga](https://github.com/alexOarga)

## Contributing

Feel free to dive in! [Open an issue](https://github.com/findCP/findCPcore/issues) or submit PRs.

Standard Readme follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

## License

[GPL](LICENSE) © Alex Oarga
