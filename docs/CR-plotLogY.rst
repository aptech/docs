
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

.. seealso:: Functions :func:`plotXY`, :func:`plotLogX`, :func:`plotLogLog`
