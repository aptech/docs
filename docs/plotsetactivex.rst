
plotSetActiveX
==============================================

Purpose
----------------
Configures the x-axis to apply attribute changes to when supported ``plotSet`` functions are used. This function only affects the behavior of future ``plotSet`` calls, and will not retroactively change axis attributes that were set prior to this call. 

Format
----------------
.. function:: plotSetActiveX(&myPlot, axis)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param axis: The axis to set as "active". Supported options: 

        .. csv-table::
            :widths: auto
    
            "bottom" (default)
            "top"
            "both"

    :type axis: string


Examples
----------------

Set attributes for top x-axis only
+++++++++++++++++++++++++++++++++++

::

    new;

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("XY");

    // Set grid line options specifically for the top X Axis.
    plotSetActiveX(&myPlot, "top");

    // Set X Grid Pen attributes. This will apply to the top only.
    plotSetXGridPen(&myPlot, "major", 2, "blue");

    // Specify that first line should be on the bottom, and second on the top.
    // This setter is independent of the active x-axis.
    plotSetWhichXAxis(&myPlot, "bottom"$|"top");

    // Only the top x-axis will have a 2px thick blue grid line.
    plotXY(myPlot, seqa(1,1,10), rndu(10,2));


Set attributes for both x axes simultaneously
+++++++++++++++++++++++++++++++++++++++++++++

::

    new;

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("XY");

    // Set grid line options specifically for the top X Axis.
    plotSetActiveX(&myPlot, "both");

    // Set X Grid Pen attributes. This will apply to the top only.
    plotSetXGridPen(&myPlot, "major", 2, "blue");

    // Specify that first line should be on the bottom, and second on the top.
    // This setter is independent of the active x-axis.
    plotSetWhichXAxis(&myPlot, "bottom"$|"top");

    // Both x-bottom and x-top will have 2px thick blue grid lines.
    plotXY(myPlot, seqa(1,1,10), rndu(10,2));


.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetXPen`, :func:`plotSetXGridPen`, :func:`plotSetXLabel`, :func:`plotSetXTicCount`, :func:`plotSetAxesPen`

