
plotSetWhichXAxis
==============================================

Purpose
----------------
Assigns curves to the top or bottom x-axis.

Format
----------------
.. function:: plotSetWhichXAxis(&myPlot, which)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param which: where each element contains either ``"top"`` or ``"bottom"``.
    :type which: string or Nx1 string array

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set up the top x-axis with a different range
    plotSetActiveX(&myPlot, "top");
    plotSetXRange(&myPlot, 0, 100);
    plotSetXLabel(&myPlot, "Top axis");

    // Set up the bottom x-axis
    plotSetActiveX(&myPlot, "bottom");
    plotSetXRange(&myPlot, 0, 10);
    plotSetXLabel(&myPlot, "Bottom axis");

    // Assign line 1 to the bottom x-axis, line 2 to the top x-axis
    plotSetWhichXAxis(&myPlot, "bottom" $| "top");

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);

    // Plot the data
    plotXY(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetWhichYAxis`, :func:`plotSetAxesPen`

