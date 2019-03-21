
delete
==============================================

Purpose
----------------

Deletes global symbols from the symbol table.

Format
----------------
.. function:: delete -flags symbol_list 
			  delete symbol_list

    :param flags: 
    :type flags: specify the type(s) of symbols to be deleted

    .. csv-table::
        :widths: auto

        "p", "procedures"
        "k", "keywords"
        "f", "fn functions"
        "m", "matrices"
        "s", "strings"
        "g", "only procedures with global references"
        "l", "only procedures with all local references"
        "n", "no pause for confirmation"

    :param symbol: name of symbol to be deleted. If symbol ends in an asterisk, all symbols matching the leading characters will be deleted.
    :type symbol: literal

Remarks
-------

This completely and irrevocably deletes a symbol from GAUSS's memory and
workspace.

Flags must be preceded by a dash (e.g. -pfk). If the n (no pause) flag
is used, you will not be asked for confirmation for each symbol.

This command is supported only from interactive level. Since the
interpreter executes a compiled pseudo-code, this command would
invalidate a previously compiled code image and therefore would destroy
any program it was a part of. If any symbols are deleted, all
procedures, keywords and functions with global references to those
symbols will be deleted as well.


Examples
----------------

::

    //Create a matrix 'x'
    x = { 1, 2, 3, 4 };
    
    //'show' returns information about active symbols
    show x;

This should return:

::

    32 bytes   x       MATRIX                 4,1
    
    delete -m x;

At the Delete?[Yes No Previous Quit] prompt, enter y.

::

    show x;

x no longer exists.

