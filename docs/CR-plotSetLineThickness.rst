
plotSetLineThickness
==============================================

Purpose
----------------

Sets the thickness of the lines on a graph.

Format
----------------
.. function:: plotSetLineThickness(&myPlot,  newTh)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param newTh: new line thickness settings.
    :type newTh: 1 x N matrix

Examples
----------------

::

    //Declare plotControl structure               
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    //Set all lines to have a thickness of 2
    newTh = 2;
    plotSetLineThickness(&myPlot, newTh);
    
    //Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    //Plot the data with the new line thickness settings
    plotXY(myPlot, x, y);

Remarks
+++++++

This function sets an attribute in a plotControl structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools->Preferences->Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotLayout`, :func:`plotSetTitle`
