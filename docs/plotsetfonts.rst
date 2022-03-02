
plotSetFonts
==============================================

Purpose
----------------
Sets the fonts for one or more elements of a graph.

Format
----------------
.. function:: plotSetFonts(&myPlot, location, font_name [, font_size, font_color]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param location: Optional argument, which attributes the interpreter change applies to.

        **Valid options:**

        .. list-table::
            :widths: auto
    
            * - "all"
            * - "legend"
            * - "legend_title"
            * - "title"
            * - "axes"
            * - "xaxis"
            * - "yaxis"
            * - "zaxis"
            * - "ticks" (numbers or tick labels)
            * - "xticks"
            * - "yticks"
            * - "zticks"


    :type location: Nx1 string array

    :param font: Optional argument, font or font family name. If this is an empty string, the font family setting will be left unchanged.
    :type font: string

    :param fontSize: Optional argument, font size in points.
    :type fontSize: scalar

    :param fontColor: Optional argument, named color or RGB value.
    :type fontColor: string

Examples
----------------

Set the font family and size for all text
++++++++++++++++++++++++++++++++++++++++++

This example will first set the font family and size for all text. It will then add a y-axis label using this font and finally add a title which uses the font family that was set, but alters the size.

::

    new;

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("hist");

    // Set all text in the font to use "times" 12 pt font
    plotSetFonts(&myPlot, "all", "times", 12);

    // Add y-axis label using font specified above
    plotSetYLabel(&myPlot, "Count");

    // Since we pass in an empty string "" for
    // the title font, it will be left alone
    plotSetTitle(&myPlot, "Histgram of Random Normal Data", "", 14);

    // Create data
    x = rndn(1e5, 1);

    // Plot a histogram of the x data spread over 20 bins
    plotHist(myPlot, x, 20);


Set the font family, size and color for the x-axis and legend
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Declare plotControl structure
    // and fill we default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("scatter");

    plotSetFonts(&myPlot, "xaxis legend", "arial", 14, "dimgray");

    // Set the x-axis label
    plotSetXLabel(&myPlot, "X variable");

    // Plot some random normal data
    plotScatter(myPlot, rndn(100, 1), rndn(100,1);


.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetLinePen`, :func:`plotSetYLabel`, :func:`plotSetXLabel`, :func:`plotSetTitle`, :func:`plotSetLegend`

