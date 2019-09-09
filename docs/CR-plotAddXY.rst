
plotAddXY
==============================================

Purpose
----------------

Adds an XY graph to an existing graph.

Format
----------------
.. function:: plotAddXY([myPlot, ]x, y)

    :param myPlot: Optional argument. A :class:`plotControl` structure.
    :type myPlot: struct

    :param x: Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Remarks
-------

:func:`plotAddXY` may only add curves to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddPolar`
