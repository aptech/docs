
plotSetOutlineEnabled
==============================================

Purpose
----------------

Turns on outline around the plot.

Format
----------------
.. function:: plotSetOutlineEnabled(&myPlot, enabled)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param enabled: A 0 to hide the outline, or a 1 to show it.
    :type enabled: scalar

Examples
----------------
.. figure:: _static/images/plotsetoutlineenabled-cr.jpg
   :scale: 50 %

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Turn on plot outline
    plotSetOutlineEnabled(&myPlot, 1);

    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);

    // Plot the data with outline enabled.
    plotScatter(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXPen`, :func:`plotSetYPen`, :func:`plotSetAxesPen`
