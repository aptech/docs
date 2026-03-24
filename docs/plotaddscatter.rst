
plotAddScatter
==============================================

Purpose
----------------
Adds a 2-dimensional scatter plot to an existing graph.

Format
----------------
.. function:: plotAddScatter([myPlot, ]x, y)

    :param myPlot: Optional argument. A :class:`plotControl` structure.
    :type myPlot: struct

    :param x: Each column contains the X values for a particular data point.
    :type x: Nx1 or NxM matrix

    :param y: Each column contains the Y values for a particular data point.
    :type y: Nx1 or NxM matrix

Remarks
-------

:func:`plotAddScatter` may only add a scatter plot to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

Examples
----------------

::

    // Create first set of scatter data
    x1 = rndn(50, 1);
    y1 = rndn(50, 1);

    // Create initial scatter plot
    plotScatter(x1, y1);

    // Add a second set of points
    x2 = rndn(30, 1) + 2;
    y2 = rndn(30, 1) + 2;
    plotAddScatter(x2, y2);

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddScatter`, :func:`plotAddXY`
