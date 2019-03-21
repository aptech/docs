
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

