
indices2
==============================================

Purpose
----------------

Processes two sets of variable names or indices from a single file. The first is a single variable and
 the second is a set of variables. The first must not occur in the second set and all must be in the file.

Format
----------------
.. function:: indices2(dataset,  var1,  var2)

    :param dataset: the name of the data set.
    :type dataset: string

    :param var1: variable name or index.
        This can be either the name of the variable, or the column index of the variable.If null or 0, the last variable in the data set will be used.
    :type var1: string or scalar

    :param var2: a character vector of names or a numeric vector of column indices.
        If scalar 0, all variables in the data set except the
        one associated with  var1 will be selected.
    :type var2: Nx1 vector

    :returns: name1 (*TODO*), scalar character matrix containing the name of the variable associated with
        var1.

    :returns: indx1 (*scalar*), the column index of  var1.

    :returns: name2 (*Nx1 character vector*), the names associated with  var2.

    :returns: indx2 (*Nx1 numeric vector*), the column indices of  var2.

