
plotSetLineThickness
==============================================

Purpose
----------------

Sets the thickness of the lines on a graph.

Format
----------------
.. function:: plotSetLineThickness(&myPlot, thickness)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: line thickness settings.
    :type thickness: 1xN matrix

Examples
----------------

::

    // Declare plotControl structure               
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    // Set all lines to have a thickness of 2
    thickness = 2;
    plotSetLineThickness(&myPlot, thickness);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new line thickness settings
    plotXY(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotLayout`, :func:`plotSetTitle`

