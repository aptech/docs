
frequency
==============================================

Purpose
----------------

Generate frequency table.

Format
----------------
.. function:: frequency(x, column)

    :param x: data matrix.
    :type x: NxK matrix

    :param column: Variable to be counted.
    :type column: scalar or string


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples//auto2.dta";
  auto2 = loadd(fname);

  // Frequency plot
  frequency(auto2, "rep78");



.. seealso:: Functions :func:`plotFreq`, :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`
