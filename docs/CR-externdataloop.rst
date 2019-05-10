
extern (dataloop)
==============================================

Purpose
----------------
Allows access to matrices or strings in memory from inside a data loop.

Format
----------------
.. function:: extern [variable_list]

Remarks
-------

Commas in *variable_list* are optional.

`extern` tells the translator not to generate local code for the listed
variables, and not to assume that they are elements of the input data
set.

`extern` statements should be placed before any reference to the symbols
listed. The specified names should not exist in the input data set, or
be used in a `make` statement.


Examples
----------------
This example shows how to assign the contents of an external vector to
a new variable in the data set, by iteratively assigning a range of
elements to the variable. The reserved variable x_x contains the data
read from the input data set on each iteration. The external vector
must have at least as many rows as the data set.

::

    base = 1;    /* used to index a range of */
                 /* elements from exvec */
    dataloop oldata newdata;
    extern base, exvec;
    make ndvar = exvec[seqa(base,1, rows(x_x))];
    # base = base + rows(x_x); /* execute command */
                                /* literally */
    endata;

