
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
    
    // Set new line colors to aqua and midnight blue
    clrs = "aqua"$|"midnight blue";
    plotSetLineColor(&myPlot, clrs);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

