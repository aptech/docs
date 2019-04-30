
plotSetFill
==============================================

Purpose
----------------
Sets the fill style, transparency and color for area plots, histograms and bar graphs.

Format
----------------
.. function:: plotSetFill(&myPlot, fillType[, transparency_pct[, colors]])

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

    :param transparency_pct: between 0 and 1. The percent opacity of the fill.
    :type transparency_pct: scalar

    :param colors: color names or HTML hex value colors.
    :type colors: string array

Remarks
-------

When graphing without the use of a plotControl structure, these settings
may be chosen through the **Tools > Preferences > Graphics** menu, after
selecting the Bar radio button. See **GAUSS Graphics**, Chapter 1, for
more information on the methods available for customizing your graphs.

Examples
----------------

::

    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("bar");
    
    //Set all bars to have a solid, blue, fill, with 50% opacity
    textures = 1;
    plotSetFill(&myPlot, textures, 0.5, "blue");
    
    //Create data
    x = seqa(1, 1, 5);
    y = { 1.5, 2, 3, 0.5, 1 };
    
    //Draw bar graph
    plotBar(myPlot, x, y);

.. seealso:: Functions :func:`plotBar`, :func:`plotGetDefaults`, :func:`plotHist`

