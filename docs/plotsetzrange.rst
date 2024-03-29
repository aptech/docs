
plotSetZRange
==============================================

Purpose
----------------
Sets the range for the Z-axis.

Format
----------------
.. function:: plotSetZRange(&myPlot, z_min, z_max)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param z_min: minimum limit of the Z-axis.
    :type z_min: scalar

    :param z_max: maximum limit of the Z-axis.
    :type z_max: scalar

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("surface");

    // Set Z-axis to to range from 0 to 10
    plotSetZRange(&myPlot, 0, 10);

    // Create and plot data using our Z-range
    x = seqa(1, 1, 5);
    y = seqa(1, 1, 6);

    z = { 3 3 2 4 5 4,
          3 3 2 3 4 5,
          4 3 2 2 4 4,
          4 4 3 3 5 6,
          5 6 4 4 6 7 };

    plotSurface(myPlot, x', y, z');

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

