
plotSetNewWindow
==============================================

Purpose
----------------

Determines whether each new graph is drawn in a new graph tab or re-uses a pre-existing graph tab.

Format
----------------
.. function:: plotSetNewWindow(&myPlot, newW)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param newW: 1 to create a new graph tab or 0 to re-use.
    :type newW: Scalar

Examples
----------------

::

    //Declare plotControl structure               
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("xy");
    
    //Set graph to create a new graph tab
    newW = 1;
    plotSetNewWindow(&myPlot, newW);
    
    //Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    //Plot the data in a new graph tab window
    plotXY(myPlot, x, y);

Remarks
-------

To open a new graph window once, use plotOpenWindow. This function sets
an attribute in a plotControl structure. It does not affect an existing
graph, or a new graph drawn using the default settings that are
accessible in the main application window from the
**Tools->Graphics>Preferences** menu. See **GAUSS Graphics**, Chapter 1,
for more information on the methods available for customizing your
graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotOpenWindow`, :func:`plotSetTitle`, :func:`plotSetLineColor`
