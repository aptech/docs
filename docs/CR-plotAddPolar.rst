
plotAddPolar
==============================================

Purpose
----------------
Adds a graph using polar coordinates to an existing polar graph.

Format
----------------
.. function:: plotAddPolar([myPlot, ]radius, theta)

    :param myPlot: A :class:`plotControl` structure
    :type myPlot: struct

    :param radius: Each column contains the magnitude for a particular line.
    :type radius: Nx1 or NxM matrix

    :param theta: Each column represents the angle values for a particular line.
    :type theta: Nx1 or NxM matrix

Remarks
-------

:func:`plotAddPolar` may only add curves to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddXY`

