
plotSetLegendFont
==============================================

Purpose
----------------
Controls the legend font name, size and color.

Format
----------------
.. function:: plotSetLegendFont(&myPlot, font[, font_size[, font_color]])

    :param &myPlot: A :class:`plotControl` structure pointer
    :type &myPlot: struct pointer

    :param font: font or font family name.
    :type font: string

    :param font_size: font size in points.
    :type font_size: scalar

    :param font_color: named color or RGB value.
    :type font_color: string

Examples
----------------

::

    new;
    cls;
    			
    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    // Set labels, location, and orientation of legend
    label = "sample A"$|"sample B";
    location = "top right";
    orientation = 0;
    plotSetLegend(&myPlot, label, location, orientation);
    
    // Set font of legend
    plotSetLegendFont(&myPlot, "arial", 18, "dark grey");
    
    // Create data
    x = rndn(30, 2);
    y = rndn(30, 2);
    
    // Plot the data with the legend settings
    plotScatter(myplot, x, y);

.. seealso:: Functions :func:`plotSetLegend`, :func:`plotSetLegendBkd`

