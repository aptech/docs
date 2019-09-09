
plotSetAxesPen
==============================================

Purpose
----------------
Sets the color for the axes line.

Format
----------------
.. function:: plotSetAxesPen(&myPlot, thickness[, clr])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the axis line in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the axes.
    :type clr: string

Remarks
-------

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

Examples
----------------

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set axis to be 2 pixeles wide and black
    plotSetAxesPen(&myPlot, 2, "black");

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);

    // Plot the data with the new line colors
    plotXY(myPlot, x, y);

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineSymbol`
