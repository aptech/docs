
plotAddHistP
==============================================

Purpose
----------------
Adds a percent histogram to an existing graph.

Format
----------------
.. function:: plotAddHistP([myPlot, ]x, v)

    :param myPlot: Optional argument. A :class:`plotControl` structure.
    :type myPlot: struct

    :param x: data
    :type x: Mx1 vector

    :param v:

        ======= ==================
        Type    Value
        ======= ==================
        vector  the breakpoints to be used to compute the frequencies.
        scalar  the number of categories.
        ======= ==================

    :type v: Nx1 vector or scalar


Remarks
-------

:func:`plotAddHistP` may only add a histogram to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

Examples
----------------

::

    // Create two sets of random data
    x1 = rndn(500, 1);
    x2 = rndn(500, 1) + 2;

    // Plot first percent histogram with 20 bins
    plotHistP(x1, 20);

    // Add second percent histogram to same graph
    plotAddHistP(x2, 20);

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddPolar`, :func:`plotAddXY`
