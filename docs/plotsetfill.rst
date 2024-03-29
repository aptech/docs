
plotSetFill
==============================================

Purpose
----------------
Sets the fill style, transparency and color for scatter symbols, area plots, histograms and bar graphs.

Format
----------------
.. function:: plotSetFill(&myPlot, fillType[, opacity_pct[, colors]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param fillType: vector where *N* is the number of bar styles to set.

        .. csv-table::
            :widths: auto

            "0", "No fill"
            "1", "Solid"
            "2", "Dense 1"
            "3", "Dense 2"
            "4", "Dense 3"
            "5", "Dense 4"
            "6", "Dense 5"
            "7", "Dense 6"
            "8", "Horizontal lines"
            "9", "Vertical lines"
            "10", "Cross pattern"
            "11", "B diagonal pattern"
            "12", "F diagonal pattern"
            "13", "Diagonal Cross"

    :type fillType: Nx1 vector

    :param opacity_pct: Optional argument, between 0 and 1. The percent opacity of the fill.
    :type opacity_pct: scalar

    :param colors: Optional argument, color names or HTML hex value colors.
    :type colors: string array

Examples
----------------
.. figure:: _static/images/plotsetfill-cr.png
   :scale: 50 %

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("bar");

    // Set all bars to have a solid, blue, fill, with 50% opacity
    textures = 1;
    plotSetFill(&myPlot, textures, 0.5, "blue");

    // Create data
    x = seqa(1, 1, 5);
    y = { 1.5, 2, 3, 0.5, 1 };

    // Draw bar graph
    plotBar(myPlot, x, y);

Remarks
-------

When graphing without the use of a :class:`plotControl` structure, these settings
may be chosen by selecting  :menuselection:`Tools --> Preferences --> Graphics --> Profiles` from the main menu.

.. seealso:: Functions :func:`plotBar`, :func:`plotAddVBar`, :func:`plotHist`
