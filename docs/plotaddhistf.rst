
plotAddHistF
==============================================

Purpose
----------------
Adds a frequency histogram to an existing graph.

Format
----------------
.. function:: plotAddHistF([myPlot, ]f, c)

    :param myPlot: Optional argument. A :class:`plotControl` structure.
    :type myPlot: struct

    :param f: frequencies to be graphed.
    :type f: Nx1 vector

    :param c: numeric labels for categories. If this is a scalar 0, a sequence from 1 to ``rows(f)`` will be created.
    :type c: Nx1 vector


Remarks
-------

:func:`plotAddHistF` may only add a histogram to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

Examples
----------------

::

    // Create frequency counts and category labels
    f1 = 10|25|40|15|10;
    c = 1|2|3|4|5;

    // Plot initial frequency histogram
    plotHistF(f1, c);

    // Add a second frequency histogram
    f2 = 5|20|30|25|20;
    plotAddHistF(f2, c);

.. seealso:: Functions :func:`plotAddBar`, :func:`plotAddHist`, :func:`plotAddHistP`, :func:`plotAddPolar`, :func:`plotAddXY`
