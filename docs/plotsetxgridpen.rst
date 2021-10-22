
plotSetGrid
==============================================

Purpose
----------------
Controls the settings for the background grid of a plot.

Format
----------------
.. function:: plotSetXGridPen(&myPlot, thickness [, color, line_style])
              plotSetGrid(&myPlot, onOff)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: specifies the thickness of the major X grid line.
    :type thickness: Scalar

    :param color: Optional argument, name or rgb value of the major X grid line color. Default color: Light Grey (#e2e2e2).
    :type color: string

    :param line_style: Optional argument, turns the grid on or off.
    :type line_style: Scalar

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set grid to on the major X-axis ticks only
    plotSetXGrid(&myPlot, "major");

    // Set grid line to be 2 px and black
    plotSetXGridPen(&myPlot, 2, "Black");

    // Create a scatter plot of random data
    plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));

    // Turn off the grid
    plotSetGrid(&myPlot, "off");

Remarks
-------

    Please note that :func:`plotSetXGridPen` is not
    supported for bar, box, or historgram plots.

.. seealso:: Functions :func:`plotSetXGrid`, :func:`plotSetYGridPen`, :func: `plotSetAxesGridPen`
