
plotSetLegend
==============================================

Purpose
----------------

Adds a legend to a graph.

Format
----------------
.. function:: plotSetLegend(&myPlot, label[, location[, orientation]])
              plotSetLegend(&myPlot, turn_off)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param label: names of the line labels.
    :type label: string array

    :param location: Optional argument, the location to place the legend.

        The location string may contain up to three tokens, or words.

        #.  Vertical location: top (default), vcenter or bottom. (Note: for backwards compatibilty middle may still be used for vcenter. However, new programs should use vcenter).

        #.  Horizontal location: left, hcenter or right (default). (Note: for backwards compatibility center may still be used for hcenter. However, new programs should use hcenter.

        #.  Inside/Outside location: inside (default), below or outside.

    :type location: string

    :param orientation: Optional argument, 0 for a horizontal legend or 1 for a vertical legend.
    :type orientation: scalar

    :param turn_off: "off" will disable the legend.
    :type turn_off: string

Technical Notes
---------------

-  The *location* parameter is a string with up to three tokens or words that are separated by a space. For example,

   ::

       location = "top right";
       location = "right top";
       location = "inside top right";

-  Use :func:`plotSetLegendFont` to control the legend font family, size and color.
-  See :func:`plotSetTextInterpreter`, for instructions on using LaTeX, or HTML in the legend labels.

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set labels, location, and orientation of legend
    label = "sample A"$|"sample B";
    location = "top right";
    orientation = 0;
    plotSetLegend(&myPlot, label, location, orientation);

    // Create data
    x = rndn(30, 2);
    y = rndn(30, 2);

    // Plot the data with the legend settings
    plotScatter(myplot, x, y);

.. seealso:: Functions :func:`plotSetLegendFont`, :func:`plotSetTextInterpreter`
