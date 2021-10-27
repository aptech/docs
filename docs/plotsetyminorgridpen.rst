
plotSetYMinorGridPen
==============================================

Purpose
----------------
Controls the thickness, color, and style for the minor Y-axis grid lines.


Format
----------------
.. function:: plotSetYMinorGridPen(&myPlot, thickness[, clr[, style]])

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
    .. figure:: _static/images/plotsetyminorgridpen-cr.png
       :scale: 50 %

    ::

        // Declare plotControl structure
        struct plotControl myPlot;

        // Initialize plotControl structure
        myPlot = plotGetDefaults("scatter");

        // Set Y-axis major and minor grid lines on
        plotSetYGrid(&myPlot, "both");

        // Set Y-axis minor grid lines tic count
        plotSetYMinorTicCount(&myPlot, 4);

        // Set Y-axis minor grid lines to be 0.5 pixels thick,
        // grey, and dashed
        plotSetYMinorGridPen(&myPlot, 0.5, "grey", 2);

        // Create a scatter plot of random data
        plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));

        // Turn off the grid
        plotSetGrid(&myPlot, "off");

    Remarks
    ---------
    - The Y-axis minor grid tick count must be set using :func:`plotSetYMinorTicCount` for the axis to show.

    .. include:: include/plotattrremark.rst

    .. seealso:: Functions :func:`plotSetXGridPen`, :func:`plotSetXMinorTicCount`, :func:`plotSetYMinorGridPen`, :func:`plotSetAxesMinorGridPen`
