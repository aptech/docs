
plotSetLineSymbol
==============================================

Purpose
----------------
Sets the symbols displayed on the plotted points of a graph.

Format
----------------
.. function:: plotSetLineSymbol(&myPlot, newSymbol[, symbolWidth])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param newSymbol: new line symbol settings. Options include:

        .. csv-table::
            :widths: auto
    
            "-1", "None."
            "0", "Ellipse."
            "1", "Rectangle."
            "2", "Diamond."
            "3", "Upward pointing triangle."
            "4", "Downward pointing triangle."
            "5", "Triangle."
            "6", "Leftward pointing triangle."
            "7", "Rightward pointing triangle."
            "8", "Cross."
            "9", "Diagonal cross."
            "10", "Horizontal line."
            "11", "Vertical line."
            "12", "Star 1."
            "13", "Star 2."
            "14", "Hexagon."

    :type newSymbol: matrix

    :param symbolWidth: Optional input, width to draw line symbols.
    :type symbolWidth: scalar

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

Examples
----------------

::

    // Declare plotControl structure               
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set line 1 to have no symbol
    // Set line 2 to display an ellipse at each plotted point.
    newSymbol = { -1, 0 };
    symbolWidth = 5;
    plotSetLineSymbol(&myPlot, newSymbol, symbolWidth);
    
    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line symbols
    plotXY(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXLabel`, :func:`plotSetLineColor`

