
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

The `extern` statement tells the translator not to generate local code for the listed
variables, and not to assume that they are elements of the input data
set.

All `extern` statements should be placed before any reference to the symbols
listed. The specified names should not exist in the input dataset, or
be used in a `make` statement.


Examples
----------------
This example shows how to assign the contents of an external vector to
a new variable in the dataset, by iteratively assigning a range of
elements to the variable. The reserved variable ``x_x`` contains the data
read from the input dataset on each iteration. The external vector
must have at least as many rows as the dataset.

::

    /*
    ** Used to index a range of
    ** elements from exvec
    */
    base = 1;

    dataloop oldata newdata;
    extern base, exvec;
    make ndvar = exvec[seqa(base, 1, rows(x_x))];

    /*
    ** Execute command
    ** literally
    */
    # base = base + rows(x_x);

    endata;
