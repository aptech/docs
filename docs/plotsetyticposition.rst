
plotSetYTicPosition
==============================================

Purpose
----------------
Controls if the y-axis tick is inside or outside the y-axis line.

Format
----------------
.. function:: plotSetYTicPosition(&myPlot, position)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param position: Position of the ticks. Options: [``"outside"``, ``"inside"``, ``"hidden"``].
    :type position: string

Examples
----------------
.. figure:: _static/images/plotsetyticsposition-cr.jpg
   :scale: 50 %

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set ticks to be inside the plot
    plotSetYTicPosition(&myPlot, "inside");

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);

    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetXTicPosition`, :func:`plotSetAxesTicPosition`
