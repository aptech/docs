
plotAddPolar
==============================================

Purpose
----------------
Adds a graph using polar coordinates to an existing polar graph.

Format
----------------
.. function:: plotAddPolar([myPlot, ]radius, theta)

    :param myPlot: Optional argument. A :class:`plotControl` structure.
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

Examples
----------------

::

    // Create angle values
    theta = seqa(0, 0.1, 63);

    // Plot a circle with radius 2
    r1 = ones(63, 1) * 2;
    plotPolar(r1, theta);

    // Add a cardioid curve to the same graph
    r2 = 1 + cos(theta);
    plotAddPolar(r2, theta);

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddXY`
