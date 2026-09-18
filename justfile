[doc('List available commands.')]
help:
    @just --list

[doc('Clean and build the autosummary example.')]
make_autosummary:
    rm -rf docs_autosummary/_build
    rm -rf docs_autosummary/_autosummary
    rm -rf docs_autosummary/autoapi
    sphinx-build -b html docs_autosummary docs_autosummary/_build/html


[doc('Clean and build the AutoAPI example.')]
make_apidoc:
    rm -rf docs_autoapi/_build
    rm -rf docs_autoapi/_autosummary
    rm -rf docs_autoapi/autoapi
    sphinx-build -b html docs_autoapi docs_autoapi/_build/html
