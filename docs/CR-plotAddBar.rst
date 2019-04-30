
plotAddBar
==============================================

Purpose
----------------
Adds a bar or a set of bars to an existing graph.

Format
----------------
.. function:: plotAddBar([myPlot, ]val, ht) 

    :param myPlot: A plotControl structure
    :type myPlot: struct

    :param val: bar labels. If scalar 0, a sequence from 1 to ``rows(ht)`` will be created.
    :type val: Nx1 numeric vector

    :param ht: bar heights.
        
        *K* overlapping or side-by-side sets of *N* bars will be graphed.

    :type ht: NxK numeric vector

Remarks
-------

:func:`plotAddBar` may only add bars to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

.. seealso:: Functions :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddPolar`, :func:`plotAddXY`

