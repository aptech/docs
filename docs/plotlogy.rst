
plotLogY
==============================================

Purpose
----------------
Graphs X vs. Y using log coordinates for the y-axis.

Format
----------------
.. function:: plotLogY([myPlot, ]x, y)

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param x: Each column represents the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y: Each column represents the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Examples
----------------

::

    // Create X data
    x = seqa(1, 1, 50);

    // Create exponentially growing Y data
    y = exp(x ./ 10);

    // Plot with log scaling on the y-axis
    plotLogY(x, y);

.. seealso:: Functions :func:`plotXY`, :func:`plotLogX`, :func:`plotLogLog`
