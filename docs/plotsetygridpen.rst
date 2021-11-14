
plotSetYGridPen
==============================================

Purpose
----------------
Controls the thickness, color, and style for the y-axis major grid lines.

Format
----------------
.. function:: plotSetYGridPen(&myPlot, thickness[, clr[, style]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the y-axis major grid lines in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the y-axis major grid lines.
    :type clr: string

    :param style: the style of the pen. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar

Examples
----------------
.. figure:: _static/images/plotsetygridpen-cr.png
   :scale: 50 %

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set grid to on the major x-axis ticks only
    plotSetYGrid(&myPlot, "major");

    // Set grid line to be 0.5 px, black, and dashed
    plotSetYGridPen(&myPlot, 0.5, "Black", 2);

    // Create a scatter plot of random data
    plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));


.. seealso:: Functions :func:`plotSetYGrid`, :func:`plotSetGridPen`, :func:`plotSetXGridPen`
