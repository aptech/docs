
plotSetBkdColor
==============================================

Purpose
----------------
Sets the background color of a graph.

Format
----------------
.. function:: plotSetBkdColor(&myPlot, color)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param color: name or rgb value of the new color.
    :type color: string

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("polar");

    // Set new background color to light grey
    plotSetBkdColor(&myPlot, "light grey");

    // Create data
    x = seqa(0.1, 0.1, 200);
    y = x;

    // Create a polar plot of the data with the new background
    // color
    plotPolar(myPlot, x, y);

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See the `GAUSS Graphics chapter <GG-GAUSSGraphics.html>`_ for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineColor`, :func:`plotSetLineSymbol`
