
plotLogLog
==============================================

Purpose
----------------
Graphs X vs. Y using log coordinates.

Format
----------------
.. function:: plotLogLog([myPlot, ]x, y)

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param x: Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

::

    // Create X data
    x = seqa(1, 1, 50);

    // Create Y as a power function of X
    y = x .^ 2;

    // Plot with log scaling on both axes
    plotLogLog(x, y);

.. seealso:: Functions :func:`plotXY`, :func:`plotLogX`, :func:`plotLogY`

