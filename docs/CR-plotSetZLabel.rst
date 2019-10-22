
plotSetZLabel
==============================================

Purpose
----------------

Controls the settings for the Z-axis label on a surface plot.

Format
----------------
.. function:: plotSetZLabel(&myPlot, label[, font[, fontSize[, fontColor]]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param label: the new label.
    :type label: string

    :param font: Optional argument, font or font family name.
    :type font: string

    :param fontSize: Optional argument, font size in points.
    :type fontSize: scalar

    :param fontColor: Optional argument, named color or RGB value.
    :type fontColor: string

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("surface");

    // Set the Z-axis label, label font, font size, and color
    plotSetZLabel(&myPlot, "Depth", "verdana", 10, "black");

    // Create data
    x = seqa(-10.6, .3, 71)';
    y = seqa(-12.4, .35, 71);
    z = sin(sqrt((x/2)^2+(y/2)^2)) ./ sqrt(x^2+y^4);
    z = z .* sin(x/3);

    // Plot the data
    plotSurface(myPlot, x, y, z);

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetXLabel`, :func:`plotSetXTicInterval`, :func:`plotSetXTicLabel`, :func:`plotSetYLabel`, :func:`plotSetLineColor`, :func:`plotSetGrid`
