
plotAddXYFill
==============================================

Purpose
----------------

Adds an area plot between sets of 2-D vectors to an existing 2-D plot.

Format
----------------
.. function:: plotAddXYFill([myPlot, ]x, y_bottom, y_top)

    :param myPlot: Optional argument, a :class:`plotControl` structure
    :type myPlot: struct

    :param x: The X values for a particular line.
    :type x: Nx1 matrix

    :param y_bottom: Each column contains the Y values for the bottom of a filled area. If *y_bottom* contains more than
        one column, each column will be the bottom for a different area.
    :type y_bottom: Nx1 or NxM matrix

    :param y_top: Each column contains the Y values for the top of a filled area. If *y_top* contains more than
        one column, each column will be the top for a different area.
    :type y_top: Nx1 or NxM matrix

Examples
----------------

One set of vectors
+++++++++++++++++++

::

    new;
    
    // Create data
    x = seqa(0, 0.1, 30);
    y = cos(x);
    
    // Create basic line plot
    plotXY(x, y);
    
    /*
    ** Styling for XY filled area plot
    */
    
    // Declare plotControl structure
    // and fill with default values
    struct plotControl myPlot;
    myPlot = plotGetDefaults("area");
    
    // Set fill to be:
    // 1 - solid
    // 0.3 - 30% opacity
    // gray - gray fill color
    plotSetFill(&myplot, 1, 0.3, "gray");
    
    // Add filled area plot to previous line drawing
    plotAddXYFill(myPlot, x, y - 1, y + 1);




.. seealso:: Functions :func:`plotArea`, :func:`plotSetFill`, :func:`plotXY`
