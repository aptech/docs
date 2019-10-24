
plotXY
==============================================

Purpose
----------------

Graphs X vs. Y using Cartesian coordinates.

Format
----------------
.. function:: plotXY([myPlot, ]x, y)

    :param myPlot: Optional argument, a :class:`plotControl` structure.
    :type myPlot: struct

    :param x: Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

::

  // Random y data
  y = rndn(100, 1);

  // Sequential x data
  x = seqa(1, 1, rows(y));

  // Plot using XY plot
  plotXY(x, y);

Remarks
-------

By default missing values in *y* will be represented as gaps
in the line.

.. seealso:: Functions :func:`plotLogX`, :func:`plotLogLog`, :func:`plotScatter`
