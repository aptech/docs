
plotSetXTicCount
==============================================

Purpose
----------------
Controls the number of major ticks on the X-axis of a 2-D plot.

Format
----------------
.. function:: plotSetXTicCount(&myPlot, num_tics)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param num_tics: the number of major ticks to place on the X-axis.
    :type num_tics: Scalar

Examples
----------------

::

    // Create some data to plot
    x = seqa(-3, 0.1, 61);
    y = x.^3 + rndn(rows(x), 1);

    // Plot the data
    plotXY(x, y);

.. figure:: _static/images/gauss15_psxtc_1.png

    5 tick marks

will produce a graph that looks similar to the one above, with 5 major tick marks on the x-axis. If we use 8 tick marks, there will be one
major tick for every integer on the x-axis. We can make that change like this:

::

    // Declare and initialize plotControl structure
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    // Set the x-axis to have 8 tick marks
    plotSetXTicCount(&myPlot, 8);

    // Plot the data, using the plotControl structure
    plotXY(myPlot, x, y);

.. figure:: _static/images/gauss15_psxtc_8.png


Remarks
-------

Note that :func:`plotSetXTicInterval` does not provide complete control over the
x-axis ticks. If the number of x-ticks requested would cause an odd x-tick
interval, GAUSS will create a number of ticks that will provide more even
spacing. For instance, in the example above, 8 ticks gave a space between
ticks of 1. If we chose 9 ticks, the spacing between ticks would be 0.889.
In that case, GAUSS would instead draw 8 ticks for a more even
appearance.

For more control over the x-axis of time series plots, use
:func:`plotSetXTicInterval` instead.

This function sets an attribute in a :class:`plotControl` structure. It does not
affect an existing graph, or a new graph drawn using the default
settings that are accessible from the :menuselection:`Tools --> Preferences --> Graphics`
menu. See **GAUSS Graphics**, Chapter 1, for more information on the
methods available for customizing your graphs.

.. seealso:: Functions :func:`plotSetXTicInterval`, :func:`plotSetXLabel`
