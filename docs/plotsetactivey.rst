
plotSetActiveY
==============================================

Purpose
----------------
Configures the y-axis to apply attribute changes to when supported ``plotSet`` functions are used. This function only affects the behavior of future ``plotSet`` calls, and will not retroactively change axis attributes that were set prior to this call. 

Format
----------------
.. function:: plotSetActiveY(&myPlot, axis)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param axis: The axis to set as "active". Supported options: 

        .. csv-table::
            :widths: auto
    
            "left (default)"
            "right"
            "both"

    :type axis: string


Examples
----------------

Set attributes for right y-axis only
++++++++++++++++++++++++++++++++++++

::

    new;

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("XY");

    // Set grid line options specifically for the right Y Axis.
    plotSetActiveY(&myPlot, "right");

    // Set Y Grid Pen attributes. This will apply to the right only.
    plotSetYGridPen(&myPlot, "major", 2, "blue");

    // Specify that first line should be on the bottom, and second on the right.
    // This setter is independent of the active y-axis.
    plotSetWhichYAxis(&myPlot, "left"$|"right");

    // Only the right y-axis will have a 2px thick blue grid line.
    plotXY(myPlot, seqa(1,1,10), rndu(10,2));


Set attributes for both y axes simultaneously
+++++++++++++++++++++++++++++++++++++++++++++

::

    new;

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("XY");

    // Set grid line options specifically for the right Y Axis.
    plotSetActiveY(&myPlot, "both");

    // Set Y Grid Pen attributes. This will apply to the right only.
    plotSetYGridPen(&myPlot, "major", 2, "blue");

    // Specify that first line should be on the bottom, and second on the right.
    // This setter is independent of the active y-axis.
    plotSetWhichYAxis(&myPlot, "left"$|"right");

    // Both y-left and y-right will have 2px thick blue grid lines.
    plotXY(myPlot, seqa(1,1,10), rndu(10,2));


.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetYPen`, :func:`plotSetYGridPen`, :func:`plotSetYLabel`, :func:`plotSetYTicCount`, :func:`plotSetAxesPen`

