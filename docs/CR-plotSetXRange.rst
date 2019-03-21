
plotSetXRange
==============================================

Purpose
----------------
Sets the range for the X-axis.

Format
----------------
.. function:: plotSetXRange(&myPlot, x_min, x_max)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param x_min: minimum limit of the x-axis.
    :type x_min: Scalar

    :param x_max: maximum limit of the x-axis.
    :type x_max: Scalar

Examples
----------------

::

    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    //Set X-axis to to range from -5 to +5
    plotSetXRange(&myPlot, -5, 5);
    
    //Create and plot data using our x-range
    x_1 = rndn(100, 1);
    x_2 = rndn(100, 1);
    
    plotScatter(myPlot, x_1, x_2);

Remarks
+++++++

This function sets an attribute in a plotControl structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the **Tools > Preferences > Graphics**
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`
