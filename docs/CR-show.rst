
show
==============================================

Purpose
----------------
Displays the global symbol table.

.. _show:
.. index::

Format
----------------

::

    show -flags symbol;
    show -flags;
    show symbol;
    show;

**Parameters**

:flags: flags to specify the symbol type that is shown

    .. csv-table::
        :widths: auto

        "k", "keywords"
        "p", "procedures"
        "f", "`fn` functions"
        "m", "matrices"
        "s", "strings"
        "g", "show only symbols with global references"
        "l", "show only symbols with all local references"

:symbol: the name of the symbol to be shown. If the last character is 
    an asterisk (``*``), all symbols beginning with the supplied characters will be shown.

Remarks
-------

If there are no arguments, the entire symbol table will be displayed.

`show` is directed to the auxiliary output if it is open.

Here is an example listing with an explanation of the columns. Note that
show does not display the column titles shown here:

::

    Memory used Name Cplx Type References Info
    128 bytes a MATRIX 4,4
    672 bytes add KEYWORD global refs 0=1
    192 bytes area FUNCTION local refs 1=1
    256 bytes c C MATRIX 4,4
    296 bytes p1 PROCEDURE local refs 1=1
    384 bytes p2 PROCEDURE global refs 0=1
    8 bytes ps1 STRUCT sdat *
    16 bytes s STRING 8 char
    312 bytes s1 STRUCT sdat 1,1
    40 bytes sa STRING ARRAY 3,1
    56 bytes sm SPARSE MATRIX 15,15
    2104 bytes token PROCEDURE local refs 2=1
    216 bytes y ARRAY 3 dims 2,3,4
    672 bytes program space used
    12 global symbols, 2000 maximum, 12 shown
    0 active locals, 2000 maximum
    1 active structure

The 'Memory used' column gives the amount of memory used by each item.

The 'Name' column gives the name of each symbol.

The 'Cplx' column contains a 'C' if the symbol is a complex matrix.

The 'Type' column specifies the type of the symbol. It can be ARRAY,
FUNCTION, KEYWORD, MATRIX, PROCEDURE, STRING, STRING ARRAY, or STRUCT.

If the symbol is a procedure, keyword or function, the 'References'
column will show if it makes any global references. If it makes only
local references, the procedure or function can be saved to disk in an
*.fcg* file with the `save` command. If the function or procedure makes any
global references, it cannot be saved in an *.fcg* file.

If the symbol is a structure, the 'References' column will contain the
structure type. A structure pointer is indicated by a ``*`` following the
structure type.

The 'Info' column depends on the type of the symbol. If the symbol is a
procedure or a function, it gives the number of values that the function
or procedure returns and the number of arguments that need to be passed
to it when it is called. If the symbol is a matrix, sparse matrix,
string array or array of structures, then the 'Info' column gives the
number of rows and columns. If the symbol is a string, then it gives the
number of characters in the string. If the symbol is an N-dimensional
array, then it gives the orders of each dimension. As follows:

===================== ===========================================
Rets=Args             if procedure, keyword, or function
Row,Col               if matrix, sparse matrix, string array, or structure
Length                if string
OrdN,...,Ord2,Ord1    if array, where :math:`N is the slowest moving dimension of the array, and Ord is the order (or size) of a dimension 
===================== ===========================================

If the symbol is an array of structures, the 'Info' column will display
the size of the array. A scalar structure instance is treated as a 1x1
array of structures. If the symbol is a structure pointer, the 'Info'
column will be blank.

The program space is the area of space reserved for all nonprocedure,
nonfunction program code. The maximum program space can be controlled by
the `new` command.

The maximum number of global and local symbols is controlled by the
*maxglobals* and *maxlocals* configuration variables in *gauss.cfg*.

Examples
----------------

::

    show -fpg eig*;

This command will show all functions and procedures that have global
references and begin with *eig*.

::

    show -m;

This command will show all matrices.

.. seealso:: Functions `new`, `delete`

