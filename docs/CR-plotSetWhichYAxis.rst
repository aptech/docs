
plotSetWhichYAxis
==============================================

Purpose
----------------
Assigns curves to the right or left Y-axis.

Format
----------------
.. function:: plotSetWhichYAxis(&myPlot, which)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param which: where each element contains either "right" or "left".
    :type which: string or Nx1 string array

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

    // Create data
    x = seqa(0.1, 0.1, 50);
    
    // Data with y-range of -1 to 1
    y1 = sin(x);
    
    // Data with y-range of 0 to 150
    y2 = exp(x);
    
    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set the first curve, 'y1' to the left Y-axis
    // Set the second curve 'y2' to the right Y-axis
    string which = { "left", "right" };
    plotSetWhichYAxis(&myPlot, which);
    
    // Plot the data
    plotXY(myPlot, x, y1~y2);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

