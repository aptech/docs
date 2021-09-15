
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

        .. include:: include/plotpenstyletable.rst

    :type newStyle: matrix

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

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetTitle`, :func:`plotSetLineSymbol`

