
plotSetGrid
==============================================

Purpose
----------------
Controls the settings for the background grid of a plot.

Format
----------------
.. function:: plotSetGrid(&myPlot, ticStyle[, color])
              plotSetGrid(&myPlot, onOff)

    :param ticStyle: specifies whether grid marks should be drawn on major tic marks. Options: "major"
    :type ticStyle: string

    :param color: name or rgb value of the new color.
    :type color: string

    :param onOff: turns the grid on or off. Options: "on" or "off." If used, this must be the only argument passed to the function besides the :class:`plotControl` structure pointer.
    :type onOff: string

Examples
----------------

::

    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    //Set grid to be black and on the major tics only
    plotSetGrid(&myPlot, "major", "black");
    
    //Create a scatter plot of random data
    plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));
    
    //Turn off the grid
    plotSetGrid(&myPlot, "off");

.. seealso:: Functions :func:`plotCustomLayout`, :func:`plotSetTitle`

