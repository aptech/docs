
plotFreq
==============================================

Purpose
----------------

Generate frequency plot of categorical data.

Format
----------------
.. function:: plotFreq([myPlot, ] x, column)

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: struct

    :param x: data.
    :type x: NxK matrix

    :param column: Categorical variable to be plotted.
    :type column: scalar or string


Examples
----------------

::

  // Load data
  fname = getGAUSSHome $+ "examples//auto2.dta";
  auto2 = loadd(fname);

  // Frequency plot
  plotFreq(auto2, "rep78");



.. seealso:: Functions :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`
