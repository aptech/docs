
plotSetLegend
==============================================

Purpose
----------------

Adds a legend to a graph.

Format
----------------
.. function:: plotSetLegend(&myPlot,  label,  location,  orientation) 
			              plotSetLegend(&myPlot,  label,  location) 
			              plotSetLegend(&myPlot,  label) 
			              plotSetLegend(&myPlot,  turn_off)

    :param &myPlot: A plotControl structure pointer.
    :type &myPlot: TODO

    :param label: names of the line labels.
    :type label: String array

    :param location: the location to place the legend.
    :type location: String

    .. csv-table::
        :widths: auto

        "The location string may contain up to three tokens, or words.1.  Vertical location: top (default), vcenter or bottom. (Note: for backwards compatibilty middle may still be used for vcenter. However, new programs should use vcenter).2.  Horizontal location: left, hcenter or right (default). (Note: for backwards compatibility center may still be used for hcenter. However, new programs should use hcenter.3.  Inside/Outside location: inside (default), below or outside."

    :param orientation: 0 for a horizontal legend or 1 for a vertical legend.
    :type orientation: scalar

    :param turn_off: "off" will disable the legend.
    :type turn_off: string

Examples
----------------

::

    //Declare plotControl structure
    struct plotControl myPlot;
    
    //Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");
    
    //Set labels, location, and orientation of legend
    label = "sample A"$|"sample B";
    location = "top right";
    orientation = 0;
    plotSetLegend(&myPlot, label, location, orientation);
    
    //Create data
    x = rndn(30, 2);
    y = rndn(30, 2);
    
    //Plot the data with the legend settings
    plotScatter(myplot, x, y);

.. seealso:: Functions :func:`plotSetLegendFont`, :func:`plotSetTextInterpreter`
