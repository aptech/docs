
plotSetTicLabelFont
==============================================

Purpose
----------------
Controls the font name, size and color for the X and Y axis tic labels.

Format
----------------
.. function:: plotSetTicLabelFont(&myPlot, font)plotSetTicLabelFont(&myPlot, font,  size)plotSetTicLabelFont(&myPlot, font,  size,  color)

    :param &myPlot: Pointer to a plotControl structure.
    :type &myPlot: TODO

    :param font: the name of the desired font.
    :type font: String

    :param size: scalar, the size of the font in points.
    :type size: Optional input

    :param color: string, named color or RGB value.
    :type color: Optional input

Examples
----------------

::

    //Simulate some data to plot 
    x = rndn(10, 1);
    y = x .* 3 + rndn(10,1);
    
    //Declare ‘myPlot’ to be a plotControl structure
    //and fill with default scatter plot settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("scatter");
    
    //Set axes tic labels to be 14 point 'times new roman'
    plotSetTicLabelFont(&myPlot, "times new roman", 14);
    
    //Create graph with tic label settings applied above
    plotScatter(myPlot, x, y);

Remarks
+++++++

plotSetTicLabelFont does not apply changes to surface plots.

.. seealso:: Functions :func:`plotSetXTicLabel`, :func:`plotSetXTicInterval`
