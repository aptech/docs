
plotSetLinePen
==============================================

Purpose
----------------
Sets the color, thickness and style for the lines on an XY or contour plot.

Format
----------------
.. function:: plotSetLinePen(&myPlot, thickness[, clr[, style]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the line in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the axes.
    :type clr: string

    :param style: the style of the pen. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar

Examples
----------------

Basic example
+++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set axis to be 2 pixeles wide and black
    plotSetLinePen(&myPlot, 2, "black");

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x) ~ cos(x);

    // Plot the data with the new line colors
    plotXY(myPlot, x, y);


Example setting all options
+++++++++++++++++++++++++++++

.. figure:: _static/images/plotsetlinepen-cr-2.jpg

    // Declare plotControl structure
    // and fill with default settings
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

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetLineStyle`, :func:`plotSetXPen`, :func:`plotSetYPen`

