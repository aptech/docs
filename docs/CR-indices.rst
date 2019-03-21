
indices
==============================================

Purpose
----------------

Processes a set of variable names or indices and returns a vector of variable names and a vector of indices.

Format
----------------
.. function:: indices(dataset, vars)

    :param dataset: the name of the data set.
    :type dataset: string

    :param vars: a character vector of names or a numeric vector of column indices.
        If scalar 0, all variables in the data set will be selected.
    :type vars: Nx1 vector

    :returns: name (*Nx1 character vector*), the names associated with  vars.

    :returns: indx (*Nx1 numeric vector*), the column indices associated with  vars.



Remarks
-------

If an error occurs, indices will either return a scalar error code or
terminate the program with an error message, depending on the trap
state. If the low order bit of the trap flag is 0, indices will
terminate with an error message. If the low order bit of the trap flag
is 1, indices will return an error code. The value of the trap flag can
be tested with trapchk; the return from indices can be tested with
scalerr. You only need to check one argument; they will both be the
same. The following error codes are possible:

.. raw:: html

   <div align="center">

+---+-----------------------------------------------------+
| 1 | Can't open dataset.                                 |
+---+-----------------------------------------------------+
| 2 | Index of variable out of range, or undefined data   |
|   | set variables.                                      |
+---+-----------------------------------------------------+

