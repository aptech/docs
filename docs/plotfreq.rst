
plotFreq
==============================================

Purpose
----------------

Generate frequency plot of categorical data.

Format
----------------
.. function:: plotAddArea([myPlot, ] x, index)

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: struct

    :param x: data matrix.
    :type x: Nx1 vector

    :param index: Index of categorical variable.
    :type index: Scalar or string


Examples
----------------

Creating confidence intervals
+++++++++++++++++++++++++++++

::

  // Load data
  fname = getGAUSSHome $+ "examples//auto2.dta";
  auto2 = loadd(fname);

  // Frequency plot
  plotFreq(auto2, "rep78");



.. seealso:: Functions :func:`plotHist`, :func:`plotHistP`, :func:`plotHistF`