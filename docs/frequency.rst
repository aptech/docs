
frequency
==============================================

Purpose
----------------

Generate frequency table.

Format
----------------
.. function:: frequency(x, column)

    :param x: Data.
    :type x: NxK dataframe

    :param column: Variable to be counted.
    :type column: Scalar or string


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname);

  // Create frequency table for the 'rep78' variable in 'auto2'
  frequency(auto2, "rep78");



.. seealso:: Functions :func:`plotFreq`, :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`
