
plotSetXRange
==============================================

Purpose
----------------
Sets the range for the X-axis.

Format
----------------
.. function:: plotSetXRange(&myPlot, x_min, x_max)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param x_min: minimum limit of the x-axis.
    :type x_min: Scalar

    :param x_max: maximum limit of the x-axis.
    :type x_max: Scalar

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set X-axis to to range from -5 to +5
    plotSetXRange(&myPlot, -5, 5);

    // Create and plot data using our x-range
    x_1 = rndn(100, 1);
    x_2 = rndn(100, 1);

    plotScatter(myPlot, x_1, x_2);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

