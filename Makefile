# Sphinx documentation build
#
# Usage:
#   make html          Build HTML docs
#   make clean         Remove build output
#   make help          Show all targets
#
# First-time setup:
#   python3 -m venv venv
#   source venv/bin/activate
#   pip install -r requirements.txt

PYTHON_BINARY = ./venv/bin/python

# You can set these variables from the command line.
SPHINXOPTS    = -j auto
SPHINXBUILD   = $(PYTHON_BINARY) -m sphinx
SOURCEDIR     = docs
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean

clean:
	rm -rf $(BUILDDIR)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
