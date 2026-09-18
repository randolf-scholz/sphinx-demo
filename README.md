# sphinx-demo

Example for both using recursive autosummary (adapted from <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion>) or autoapi.

## Setup with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run
these commands from the repository root with Python 3.13 or newer:

```sh
uv venv
uv pip install -e .
```

Clean and build either documentation example using `just`:

```sh
just make_autosummary
just make_apidoc
```
