
plotSetLegendBorder
==============================================

Purpose
----------------
Controls the color and thickness of the legend border.

Format
----------------
.. function:: plotSetLegendBorder(&myPlot, clr[, thickness, style])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param clr: name or rgb value of the new color.
    :type clr: string

    :param thickness: Optional input, the thickness of the legend border in pixels.
    :type thickness: scalar

    :param style: Optional input, border line style. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: scalar

Examples
----------------

::

    // Create the sequence 0.25, 0.5, 0.75...3
    x = seqa(0.25, 0.25, 12);
    y = sin(x);
    
    // Declare plotControl structure
    // and fill with default settings for XY plots
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    plotSetLegend(&myPlot, "sin(x)", 1|0.25);
    
    // Set the legend border to light gray
    // and 2 pixels thick
    plotSetLegendBorder(&myPlot, "light gray", 2);
    
    plotXY(myPlot, x, y);


.. figure:: _static/images/pslb1.png
   :scale: 50 %

Remarks
-------

* You can hide the legend border by either setting it to the background color or using :func:`plotSetLegendBkd` to make
  the legend background transparent.
* :func:`plotSetLegendBorder` is supported for use with all plot types except for PQG graphics and :func:`plotSurface`.

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetLegend`, :func:`plotSetLegendBkd`, :func:`plotSetLegendFont`

