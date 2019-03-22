
indices2
==============================================

Purpose
----------------

Processes two sets of variable names or indices from a single file. The first is a single variable and
 the second is a set of variables. The first must not occur in the second set and all must be in the file.

Format
----------------
.. function:: indices2(dataset, var1, var2)

    :param dataset: the name of the data set.
    :type dataset: string

    :param var1: variable name or index.
        This can be either the name of the variable, or the column index of the variable.If null or 0, the last variable in the data set will be used.
    :type var1: string or scalar

    :param var2: a character vector of names or a numeric vector of column indices.
        If scalar 0, all variables in the data set except the
        one associated with  var1 will be selected.
    :type var2: Nx1 vector

    :returns: name1 (*scalar character matrix*) containing the name of the variable associated with
        var1.

    :returns: indx1 (*scalar*), the column index of  var1.

    :returns: name2 (*Nx1 character vector*), the names associated with  var2.

    :returns: indx2 (*Nx1 numeric vector*), the column indices of  var2.



Remarks
-------

If an error occurs, indices2 will either return a scalar error code or
terminate the program with an error message, depending on the trap
state. If the low order bit of the trap flag is 0, indices2 will
terminate with an error message. If the low order bit of the trap flag
is 1, indices2 will return an error code. The value of the trap flag can
be tested with trapchk; the return from indices2 can be tested with
scalerr. You only need to check one argument; they will all be the same.
The following error codes are possible:

+---+-----------------------------------------------------+
| 1 | Can't open dataset.                                 |
+---+-----------------------------------------------------+
| 2 | Index of variable out of range, or undefined data   |
|   | set variables.                                      |
+---+-----------------------------------------------------+
| 3 | First variable must be a single name or index.      |
+---+-----------------------------------------------------+
| 4 | First variable contained in second set.             |
+---+-----------------------------------------------------+



Source
------

indices2.src

