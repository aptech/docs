
plotSetYRange
==============================================

Purpose
----------------
Sets the range for the y-axis.

Format
----------------
.. function:: plotSetYRange(&myPlot, y_min, y_max)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param y_min: minimum limit of the y-axis.
    :type y_min: scalar

    :param y_max: maximum limit of the y-axis.
    :type y_max: scalar

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools > Preferences > Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

Examples
----------------

::

    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    //Set y-axis to to range from 0 to 2
    plotSetYRange(&myPlot, 0, 2);
    
    //Create and plot data using our x-range
    x = rndu(100, 1);
    y = rndu(100, 1);
    
    plotScatter(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

