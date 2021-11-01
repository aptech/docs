
normalizecollabels
==============================================

Purpose
----------------

Removes duplicate keys from a categorical variable and consolidates removed keys into a common key.

Format
----------------
.. function:: x_meta = normalizecollabels()

    :param x: data.
    :rtype x: NxK dateframe

    :param columns: The names or indices of the date columns in *X* to normalize.
    :type columns: Mx1 scalar or string

    :return x_norm: Data with normalized categorical variables
    :rtype x_norm: NxK dataframe

Remarks
-------
The :func:`normalizecollabels` procedure is useful when cleaning and merging categorical variables.
