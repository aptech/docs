
indicesfn
==============================================

Purpose
----------------

Processes a set of variable names or indices and
returns a vector of variable names and a vector of
indices.

Format
----------------
.. function:: indicesfn(dataset,  namein,  indxin)

    :param dataset: name of the data set.
    :type dataset: string

    :param namein: names
        of selected columns in the data set. If set to a null string, columns
        are selected using  indxin
    :type namein: Nx1 string array

    :param indxin: indices of selected
        columns in the data set. If set to 0, columns are selected using
        namein.
    :type indxin: Nx1 vector

    :returns: name (*Nx1 string array*), the names of the
        selected columns.

    :returns: indx (*Nx1 vector*), the indices of the
        selected columns.

