
indicesf
==============================================

Purpose
----------------

Processes a set of variable names or indices and returns a vector of variable names and a vector of indices.

Format
----------------
.. function:: indicesf(fp, namein, indxin)

    :param fp: file handle of an open data set.
    :type fp: scalar

    :param namein: names
        of selected columns in the data set. If set to a null string, columns
        are selected using indxin
    :type namein: Nx1 string array

    :param indxin: indices of selected
        columns in the data set. If set to 0, columns are selected using
        namein.
    :type indxin: Nx1 vector

    :returns: name (*Nx1 string array*), the names of the selected columns.

    :returns: indx (*Nx1 vector*), the indices of the selected columns.



Remarks
-------

If namein is a null string and indxin is 0, all columns of the data set
will be selected.

If an error occurs, indx will be set to a scalar error code. The
following error codes are possible:

+---+-----------------------------------------------------+
| 1 | Can't open data file                                |
+---+-----------------------------------------------------+
| 2 | Variable not found                                  |
+---+-----------------------------------------------------+
| 3 | Indices outside of range of columns                 |
+---+-----------------------------------------------------+



Source
------

indices.src

