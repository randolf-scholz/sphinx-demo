# sphinx-demo

Example for both using recursive autosummary (adapted from <https://github.com/JamesALeedham/Sphinx-Autosummary-Recursion>) or autoapi.

## Setup with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run
these commands from the repository root with Python 3.10 or newer:

```sh
uv venv
source .venv/bin/activate
uv pip install -e .
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`
instead. The editable install includes the Sphinx dependencies and picks up
changes to the package source without reinstalling.

Build either documentation example from the repository root:

```sh
sphinx-build -b html docs_autosummary docs_autosummary/_build/html
sphinx-build -b html docs_autoapi docs_autoapi/_build/html
```
