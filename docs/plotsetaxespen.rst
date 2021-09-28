
plotSetAxesPen
==============================================

Purpose
----------------
Sets the color, thickness and style for the axes lines.

Format
----------------
.. function:: plotSetAxesPen(&myPlot, thickness[, clr[, style]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the axis line in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the axes.
    :type clr: string

    :param style: the style of the pen. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar

Examples
----------------

Basic Example
++++++++++++++++

::

    // Declare plotControl structure
    // and fill with default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");
    
    // Specify both lines to be 2 pixels wide,
    // for the first line to be coral and the
    // second to be cadet blue
    clrs = "coral" $| "cadet blue";
    plotSetLinePen(&myPlot, 2, clrs);
    
    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x) ~ cos(x);
    
    // Plot the data with the new line colors
    plotXY(myPlot, x, y);


Complete Example
+++++++++++++++++++

    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");
    
    
    /*
    ** Set XY lines to 
    ** 1. Be 2 pixels wide.
    ** 2. Use the colors from the 'accent' color palette
    ** 3. Set the line styles to be solid=1, dash=2, dot=3
    */
    clrs = getColorPalette("accent");
    styles = { 1, 2, 3 };
    plotSetLinePen(&myPlot, 3, clrs, styles);
    
    // Create 3 series of data
    x = seqa(0.1, 0.1, 50);
    y = sin(x) ~ cos(x) ~ (sin(x) .* cos(x));
    
    labels = "sin(x)" $| "cos(x)" $| "sin(x) * cos(x)";
    plotSetLegend(&myPlot, labels);
    
    // Plot the data with the new line
    // colors, styles and thickness
    plotXY(myPlot, x, y);


Remarks
-------

- The X and Y axis line properties can be set separately with :func:`plotSetXPen` and :func:`plotSetYPen`.
- A bounding box can be set around the entire graph with :func:`plotSetOutlineEnabled`.

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLinePen`, :func:`plotSetXPen`, :func:`plotSetYPen`

