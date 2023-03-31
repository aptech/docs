
normalizecollabels
==============================================

Purpose
----------------

Finds instances of identical labels that have differing keys in a dataframe and merges them so all labels are unique.

If identical labels are merged, all references to the key of the duplicate label will be updated.

Format
----------------
.. function:: x_norm = normalizecollabels(x[, columns])

    :param x: data.
    :rtype x: NxK dateframe

    :param columns: Optional. The names or indices of the string/category columns in *x* to normalize. All string/category columns will be processed if omitted.
    :type columns: Mx1 scalar or string/string array.

    :return x_norm: Data with normalized string/categorical variables
    :rtype x_norm: NxK dataframe

Remarks
-------

The :func:`normalizecollabels` procedure is useful when cleaning and merging categorical variables that may come from different sources. This is primarily a convenience function utilized by multiple string-related functions and in general should not need to be called explicitly by an end-user.

.. seealso:: :func:`dfappend`

