
plotSetWhichYAxis
==============================================

Purpose
----------------
Assigns curves to the right or left y-axis.

Format
----------------
.. function:: plotSetWhichYAxis(&myPlot, which)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param which: where each element contains either ``"right"`` or ``"left"``.
    :type which: string or Nx1 string array

Examples
----------------

::

    // Create data
    x = seqa(0.1, 0.1, 50);

    // Data with y-range of -1 to 1
    y1 = sin(x);

    // Data with y-range of 0 to 150
    y2 = exp(x);

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set the first curve, 'y1' to the left y-axis
    // Set the second curve 'y2' to the right y-axis
    string which = { "left", "right" };
    plotSetWhichYAxis(&myPlot, which);

    // Plot the data
    plotXY(myPlot, x, y1~y2);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

