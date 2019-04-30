
plotSetLineStyle
==============================================

Purpose
----------------

Sets the line styles for a graph.

Format
----------------
.. function:: plotSetLineStyle(&myPlot, newStyle)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param newStyle: new line styles. Options include:

        .. csv-table::
            :widths: auto
    
            "1", "Solid line."
            "2", "Dash line."
            "3", "Dot line."
            "4", "Dash-Dot line."
            "5", "Dash-Dot-Dot line."

    :type newStyle: matrix

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools > Preferences > Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set line 1 as a solid line, 
    // set line 2 as a dash line, etc.
    newStyle = { 1, 2, 3, 4, 5 };
    plotSetLineStyle(&myPlot, newStyle);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line styles
    plotXY(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetTitle`, :func:`plotSetLineSymbol`

