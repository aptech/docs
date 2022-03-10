
plotSetYRange
==============================================

Purpose
----------------
Sets the range for the left and/or right y-axes.

Format
----------------
.. function:: plotSetYRange(&myPlot, y_min, y_max)
              plotSetYRange(&myPlot, y_min, y_max [, tic_interval, first_labeled])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param y_min: minimum limit of the y-axis.
    :type y_min: scalar, or 2x1 vector

    :param y_max: maximum limit of the y-axis.
    :type y_max: scalar, or 2x1 vector

    :param tic_interval: Optional input, the distance between y-axis tick labels.
    :type tic_interval: scalar

    :param first_labeled: Optional input, the value of the first ``y`` value on which to place a tick label.
    :type first_labeled: scalar

Examples
----------------

Basic example
+++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    // Set left y-axis to to range from 0 to 2
    plotSetYRange(&myPlot, 0, 2);
    
    // Create and plot data using our y-range
    x = rndu(100, 1);
    y = rndu(100, 1);
    
    plotScatter(myPlot, x, y);


Set the range for the left and right y-axes
+++++++++++++++++++++++++++++++++++++++++++++++

::

    x = seqa(-3, 0.1, 61);
    y = x.^2 ~ sin(x);
    
    struct plotControl plt;
    plt = plotGetDefaults("xy");
    
    plotSetWhichYAxis(&plt, "left" $| "right");
    
    // Set the left y-axis range to between -5 and +15,
    // and the right y-axis to between -2 and +2
    plotSetYRange(&plt, -5|-2, 15|2);
    
    plotXY(plt, x, y);


Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

