
plotSetLegendBkd
==============================================

Purpose
----------------
Sets the opacity and color for the background of a graph legend.

Format
----------------
.. function:: plotSetLegendBkd(&myPlot, opacity[, bkd_clr])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param opacity: a value between 0 (completely transparent) and 1 (completely opaque).
    :type opacity: Scalar

    :param bkd_clr: Optional input, the name or rgb value of the new background colors
    :type bkd_clr: string

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

Examples
----------------

Example 1
+++++++++

::

    // Declare plotControl structure
    // and fill with default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");
    
    // Set legend text
    plotSetLegend(&myPlot, "Sin" $| "Cos");
    
    // Set the legend background to be
    // 90% opaque and gray.
    clrs = "gray";
    plotSetLegendBkd(&myPlot, 0.9, clrs);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

Example 2
+++++++++

::

    // Declare plotControl structure
    // and fill with default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");
    
    // Set legend text
    plotSetLegend(&myPlot, "Sin" $| "Cos");
    
    // Set the legend background to be completely transparent.
    // This will make the legend background and border invisible.
    // Th legend text will still be seen.
    plotSetLegendBkd(&myPlot, 0);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLegendFont`

