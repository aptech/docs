
plotSetTicLabelFont
==============================================

Purpose
----------------
Controls the font name, size and color for the X and Y axis tick labels.

Format
----------------
.. function:: plotSetTicLabelFont(&myPlot, font[, size[, color]])

    :param &myPlot: Pointer to a :class:`plotControl` structure.
    :type &myPlot: struct pointer

    :param font: the name of the desired font.
    :type font: string

    :param size: Optional argument, the size of the font in points.
    :type size: scalar

    :param color: Optional argument, named color or RGB value.
    :type color: string

Examples
----------------

::

    // Simulate some data to plot
    x = rndn(10, 1);
    y = x .* 3 + rndn(10, 1);

    // Declare ‘myPlot’ to be a plotControl structure
    // and fill with default scatter plot settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("scatter");

    // Set axes tick labels to be 14 point 'times new roman'
    plotSetTicLabelFont(&myPlot, "times new roman", 14);

    // Create graph with tick label settings applied above
    plotScatter(myPlot, x, y);

Remarks
-------

:func:`plotSetTicLabelFont` does not apply changes to surface plots.

.. seealso:: Functions :func:`plotSetXTicLabel`, :func:`plotSetXTicInterval`
