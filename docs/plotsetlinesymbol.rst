
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

            "-1", "``none``", "No symbol."
            "0", "``circle``", "Circle."
            "1", "``square``", "Square."
            "2", "``diamond``", "Diamond."
            "3", "``triangle_up``", "Upward pointing triangle."
            "4", "``triangle_down``", "Downward pointing triangle."
            "5", "``triangle``", "Triangle."
            "6", "``triangle_left``", "Leftward pointing triangle."
            "7", "``triangle_right``", "Rightward pointing triangle."
            "8", "``plus``", "Plus sign."
            "9", "``x``", "X."
            "10", "``hline``", "Horizontal line."
            "11", "``vline``", "Vertical line."
            "12", "``star``", "Star."
            "13", "``star2``", "Six-pointed star."
            "14", "``hexagon``", "Hexagon."

    :type newSymbol: matrix or string array

    :param symbolWidth: Optional argument, width to draw line symbols.
    :type symbolWidth: scalar

Examples
----------------

Example 1: Basic usage with string names
++++++++++++++++++++++++++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set line 1 to have no symbol
    // Set line 2 to display a circle at each plotted point.
    plotSetLineSymbol(&myPlot, "none" $| "circle", 5);

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);

    // Plot the data with the new line symbols
    plotXY(myPlot, x, y);

Example 2: Using numeric values
+++++++++++++++++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set markers: circle for line 1, diamond for line 2, triangle for line 3
    plotSetLineSymbol(&myPlot, 0 | 2 | 3, 8);

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x)~sin(x+1);

    // Plot the data with the new line symbols
    plotXY(myPlot, x, y);

Remarks
-------

By default, markers are hollow (unfilled). Use :func:`plotSetFill` to fill the markers with a solid color or pattern.

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetFill`, :func:`plotSetLineColor`

