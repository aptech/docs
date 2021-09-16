
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
    :type x_min: Scalar, or 2x1 matrix

    :param x_max: maximum limit of the x-axis.
    :type x_max: Scalar, or 2x1 matrix

Examples
----------------

Basic usage
+++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set X-axis to to range from -5 to +5
    plotSetXRange(&myPlot, -5, 5);

    // Create and plot data using our x-range
    x = rndn(100, 1);
    y = rndn(100, 1);

    plotScatter(myPlot, x, y);


Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

