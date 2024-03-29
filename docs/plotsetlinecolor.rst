
plotSetLineColor
==============================================

Purpose
----------------
Sets the line colors for a graph.

Format
----------------
.. function:: plotSetLineColor(&myPlot, colors)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param colors: name or rgb value of the new colors.
    :type colors: String array

Examples
----------------

::

    // Declare plotControl structure               
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set new line colors to aqua and midnight blue
    clrs = "aqua"$|"midnight blue";
    plotSetLineColor(&myPlot, clrs);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

