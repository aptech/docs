
plotGetDefaults
==============================================

Purpose
----------------
Gets default settings for plotting graphs.

Format
----------------
.. function:: plotGetDefaults(graph)

    :param graph: name of graph type: bar, box, hist, polar, scatter, surface or xy.
    :type graph: String

    :returns: myPlot (*TODO*), A plotControl structure.

Examples
----------------

::

    //Declare plotControl structure
    
    struct plotControl myPlot;
    
    //Initialize plotControl structure with defaults for an
    //'xy' graph
    myPlot = plotGetDefaults("xy");
    
    //Create some data to plot
    x = seqa(-5, 0.1, 50);
    y = pdfn(x);
    
    //Make a desired change to the plotControl structure
    plotSetTitle(&myPlot, "Default XY Settings");
    
    //Plot the data using the plotControl structure
    plotXY(myPlot, x, y);

Remarks
+++++++

The plotGetDefaults function will use the default settings for the
specified graph type. These may be accessed from the main menu bar:
**Tools->Preferences->Graphics**.

.. seealso:: Functions :func:`plotSetBkdColor`, :func:`plotSetLineColor`, :func:`plotSetLineSymbol`
