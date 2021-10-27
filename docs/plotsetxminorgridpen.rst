
plotSetXMinorGridPen
==============================================

Purpose
----------------
Controls the thickness, color, and style for the x-axis minor grid lines.

Format
----------------
.. function:: plotSetXMinorGridPen(&myPlot, thickness[, clr[, style]])

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param thickness: the thickness of the x-axis minor grid lines in pixels.
    :type thickness: Scalar

    :param clr: Optional argument, name or rgb value of the new color for the x-axis minor grid lines.
    :type clr: string

    :param style: the style of the pen. Options include:

        .. include:: include/plotpenstyletable.rst

    :type style: Scalar

Examples
----------------
.. figure:: _static/images/plotsetxminorgridpen-cr.jpg
   :scale: 50 %

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("scatter");

    // Set x-axis major and minor grid lines on
    plotSetXGrid(&myPlot, "both");

    // Set x-axis minor grid lines tic count
    plotSetXMinorTicCount(&myPlot, 4);

    // Set x-axis minor grid lines to be 0.5 pixels thick,
    // grey, and dashed
    plotSetXMinorGridPen(&myPlot, 0.5, "grey", 2);

    // Create a scatter plot of random data
    plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));


Remarks
---------
    - The x-axis minor grid must turned on using :func:`plotSetXGrid` or :func:`plotSetGrid` for the minor axis to show.
    - The x-axis minor grid tick count must be set using :func:`plotSetXMinorTicCount` for the minor axis to show.
    - The x-axis minor grid is unsupported for bar, box, and histogram plots at this time.

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetXGrid`, :func:`plotSetXMinorTicCount`, :func:`plotSetYMinorGridPen`, :func:`plotSetAxesMinorGridPen`
