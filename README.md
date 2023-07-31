# opscan

![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![codecov](https://codecov.io/gh/tssujt/opscan/branch/main/graph/badge.svg?token=47PY3XC2DV)](https://codecov.io/gh/tssujt/opscan)

An open port scanner.

## Install

```
pip install git+https://github.com/tssujt/opscan.git
```

## Usage

Check if a port is open:

```
opscan localhost --port 22
```

Scan 0-65535 ports on a domain/ip:

```
opscan example.com
```

Scan 0-65535 ports on multiple domains/ips:

```
opscan example.com localhost
```
