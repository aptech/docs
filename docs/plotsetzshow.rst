
plotSetZShow
==============================================

Purpose
----------------
Hides or enables the display of the z-axis.

Format
----------------
.. function:: plotSetZShow(&myPlot, is_on)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param is_on: A 0 to hide the z-axis, or a 1 to show it. 
    :type is_on: Scalar


Examples
----------------

::

    // Declare plotControl structure
    // and fill with default settings
    struct plotControl myPlot;
    myPlot = plotGetDefaults("surface");

    // Turn off the z-axis
    plotSetZShow(&myPlot, 0);

    // Create data
    y = seqa(0.1, 0.1, 50);
    x = y';
    z = sin(x)+sin(y);

    // Plot the data
    plotSurface(myPlot, x, y, z);

Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetXRange`, :func:`plotSetXShow`

