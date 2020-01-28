
plotHist
==============================================

Purpose
----------------
Computes and graphs a frequency histogram for a vector. The actual frequencies are plotted for each category.

Format
----------------
.. function:: plotHist([myPlot, ]x, v)

    :param myPlot: Optional argument, a :class:`plotControl` structure
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

Examples
----------------

::

    // Create some data to plot
    x = rndn(5000, 1);
    
    // Plot the data
    plotHist(x, 20);

.. seealso:: Functions :func:`plotHistP`, :func:`plotHistF`, :func:`plotBar`

