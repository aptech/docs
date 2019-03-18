
show
==============================================

Purpose
----------------
Displays the global symbol table.

Format
----------------
.. function:: show -flags symbolshow -flagsshow symbolshow

    :param flags: flags to specify the symbol type that is shown.
    :type flags: TODO

    .. csv-table::
        :widths: auto

        "k", "keywords"
        "p", "procedures"
        "f", "fn functions"
        "m", "matrices"
        "s", "strings"
        "g", "show only symbols with global references"
        "l", "show only symbols with all local references"

    :param symbol: the name of the symbol to be shown. If the
        last character is an asterisk (*), all symbols
        beginning with the supplied characters will be
        shown.
    :type symbol: TODO

Examples
----------------

::

    show -fpg eig*;

This command will show all functions and procedures that have global
references and begin with eig.

::

    show -m;

This command will show all matrices.

.. seealso:: Functions :func:`new`, :func:`delete`
