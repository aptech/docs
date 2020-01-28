
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

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See the `GAUSS Graphics chapter <GG-GAUSSGraphics.html>`_ for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotLayout`, :func:`plotSetTitle`

