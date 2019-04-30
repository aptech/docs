
plotAddHistP
==============================================

Purpose
----------------
Adds a percent histogram to an existing graph.

Format
----------------
.. function:: plotAddHistP([myPlot, ]x, v)

    :param myPlot: A :class:`plotControl` structure
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

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddPolar`, :func:`plotAddXY`

