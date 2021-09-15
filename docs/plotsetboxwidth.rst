
plotSetJitterRange
==============================================

Purpose
----------------

Sets the allowable jitter range for :func:`plotBox` or :func:`plotScatter` plots.

Format
----------------
.. function:: plotSetJitterRange(&myPlot, range)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param range: the jitter range. 

        For box plots, the allowable range is between [0.0 - 1.0], representing the percentage of the box width that jitter is allowed to occur. The default value is 1.0 (jitter spans the entire box width). 

        For scatter plots, this is a fixed value representing how far from the initial `x` value in either direction that points will be plotted. The default value is 0.0 (no jitter).

    :type range: 1xN matrix

Examples
----------------

::

    // Declare plotControl structure               
    struct plotControl myPlot;
    
    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    // Set all lines to have a jitter range of 0.25
    jitterRange = 0.25;
    plotSetJitterRange(&myPlot, jitterRange);
    
    // Create data
    x = seqa(0.1, 1, 50);
    y = sin(x)~cos(x);
    
    // Plot the data with the new jitter range settings.
    plotScatter(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetBoxWidth`

