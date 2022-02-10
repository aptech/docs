
plotSetYRange
==============================================

Purpose
----------------
Sets the range for the y-axis.

Format
----------------
.. function:: plotSetYRange(&myPlot, y_min, y_max)
              plotSetYRange(&myPlot, y_min, y_max [, tic_interval, first_labeled])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param y_min: minimum limit of the y-axis.
    :type y_min: scalar

    :param y_max: maximum limit of the y-axis.
    :type y_max: scalar

    :param tic_interval: Optional input, the distance between y-axis tick labels.
    :type tic_interval: scalar

    :param first_labeled: Optional input, the value of the first ``y`` value on which to place a tick label.
    :type first_labeled: scalar

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    // Set y-axis to to range from 0 to 2
    plotSetYRange(&myPlot, 0, 2);
    
    // Create and plot data using our y-range
    x = rndu(100, 1);
    y = rndu(100, 1);
    
    plotScatter(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`

