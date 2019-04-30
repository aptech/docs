
plotHistP
==============================================

Purpose
----------------
Computes and graphs a percent frequency histogram of a vector. The percentages in each category are plotted.

Format
----------------
.. function:: plotHistP([myPlot, ]x, v)

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

Basic example with specified number of bins
+++++++++++++++++++++++++++++++++++++++++++

::

    // Simulate random normal data to plot
    X = rndn(100, 1);
    
    // Number of bins to create
    nbins = 30;
    
    // Draw histogram with default settings
    plotHistP(X, nbins);

Basic example with specified bin breakpoints
++++++++++++++++++++++++++++++++++++++++++++

::

    // Simulate random normal data to plot
    X = rndn(100, 1);
    
    // Specify bin breakpoints
    brk_pts = { -3, -2, -1, 0, 1, 2, 3 };
    
    // Draw histogram with default settings
    plotHistP(X, brk_pts);

Control plot settings with plotControl structure
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Simulate random normal data to plot
    X = rndn(100, 1);
    
    // Number of bins to create
    nbins = 30;
    
    // Declare 'myPlot' to be a plotControl structure
    // and fill with bar/hist default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("bar");
    
    // Change Histogram fill settings
    fill_type = 1;
    opacity_pct = 0.8;
    fill_clr = "light blue";
    plotSetFill(&myPlot, fill_type, opacity_pct, fill_clr);
    
    // Draw histogram with settings stored in 'myPlot'
    plotHistP(myPlot, X, nbins);

.. seealso:: Functions :func:`plotHist`, :func:`plotHistF`, :func:`plotBar`, :func:`plotBox`, :func:`plotScatter`

