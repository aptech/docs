
plotSetLineStyle
==============================================

Purpose
----------------

Sets the line styles for a graph.

Format
----------------
.. function:: plotSetLineStyle(&myPlot, newStyle)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param newStyle: new line styles. Options include:

        .. include:: include/plotpenstyletable.rst

    :type newStyle: matrix or string array

Examples
----------------

Example 1: Basic usage with string names
++++++++++++++++++++++++++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set line 1 as a solid line, line 2 as dashed
    plotSetLineStyle(&myPlot, "solid" $| "dash");

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x);

    // Plot the data with the new line styles
    plotXY(myPlot, x, y);

Example 2: Using numeric values
+++++++++++++++++++++++++++++++

::

    // Declare plotControl structure
    struct plotControl myPlot;

    // Initialize plotControl structure
    myPlot = plotGetDefaults("xy");

    // Set line 1 as solid, line 2 as dash,
    // line 3 as dot, line 4 as dash-dot, line 5 as dash-dot-dot
    plotSetLineStyle(&myPlot, seqa(1, 1, 5));

    // Create data
    x = seqa(0.1, 0.1, 50);
    y = sin(x)~cos(x)~sin(x+1)~cos(x+1)~sin(x+2);

    // Plot the data with the new line styles
    plotXY(myPlot, x, y);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotGetDefaults`, :func:`plotSetTitle`, :func:`plotSetLineSymbol`

