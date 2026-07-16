# infrastructure-contracts-engine

![PyPI](https://img.shields.io/pypi/v/infrastructure-contracts-engine)
![License](https://img.shields.io/github/license/samcole8/infrastructure-contracts-engine)

Infrastructure Contracts Engine (ICE) is a tool for detecting and preventing drift-driven incompatibilities across heterogenous infrastructure. It is designed to work with [terraform-provider-ice](https://github.com/samcole8/terraform-provider-ice).

> **Note: ICE is a proof of concept and is not intended for production use**. Input schema validation, reliability, operational concerns, and security hardening are outside the scope of this prototype.


## Installation

### Install from PyPI

```bash
pip install infrastructure-contracts-engine
```

### Install from source

```bash
git clone https://github.com/samcole8/infrastructure-contracts-engine
cd infrastructure-contracts-engine
python3 -m venv ice-venv
source ice-venv/bin/activate
pip install -e .
```

After installation, the `ice` command is available from the shell.

## Usage

ICE is currently a proof of concept. The configuration schema and interface are under active development and may change between releases.

See `integration/` for a manual integration example and the project source for implementation details.