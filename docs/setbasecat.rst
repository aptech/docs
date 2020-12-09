
setBaseCat
==============================================

Purpose
----------------

Assign the label *basecase* to be the base case for the categorical variable specified by *columns* .

Format
----------------
.. function:: x_meta = setBaseCat(x, basecase [, columns])

    :param x: data.
    :type x: NxK matrix

    :param basecase: category to be set to base case.
    :type basecase: Mx1 string array

    :param columns: Optional argument, indicates columns of categorical variables to set base case for. Default = all columns.
    :type columns: Mx1 scalar or string

    :return x_meta: contains data with categorical base cases set to the categories specified in *basecase* for the variables in *columns* .
    :rtype x_meta: NxK dataframe


Examples
----------------

::

  // Load yarn data file
  yarn = loadd("C:\\gauss21\\examples\\yarn.xlsx",
                "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get categorical labels for
  // yarn_length and amplitude
  getColLabels(yarn, "yarn_length");

  // Change base case
  // to high for both
  // yarn_length and amplitude
  yarn = setBaseCat(yarn, "low", "yarn_length");



.. seealso:: Functions :func:`setColtypes`, :func:`getColLabels`, :func:`setColLabels`
