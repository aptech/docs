
plotSetXTicCount
==============================================

Purpose
----------------
Sets the target number of major ticks on the x-axis of a 2-D plot.

Format
----------------
.. function:: plotSetXTicCount(&myPlot, num_tics)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param num_tics: the target number of major ticks on the x-axis. GAUSS draws about this many ticks, at round values. Set to 0 to turn off the x-axis ticks and tick labels.
    :type num_tics: Scalar

Examples
----------------

::

    // Create some data to plot
    x = seqa(-3, 0.1, 61);
    y = x.^3;

    // Declare and initialize plotControl structure
    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    // Aim for 4 ticks on the x-axis
    plotSetXTicCount(&myPlot, 4);

    // Plot the data, using the plotControl structure
    plotXY(myPlot, x, y);

The x-axis runs from -3 to 3, the ends of the data, and has 3 major ticks, at
-2, 0 and 2. No round spacing gives exactly 4 ticks on this range: a spacing of
2 gives 3 ticks and a spacing of 1 gives 7, and 3 is nearer the request. The
ends, -3 and 3, are not labeled, because they do not fall on a tick.

If we aim for 7 ticks, there will be one major tick for every integer on the
x-axis, from -3 to 3. We can make that change like this:

::

    // Aim for 7 ticks on the x-axis
    plotSetXTicCount(&myPlot, 7);

    // Plot the data, using the plotControl structure
    plotXY(myPlot, x, y);

Remarks
-------

The number of ticks is a target, not an exact count. GAUSS draws about that
many ticks and keeps the tick values round, such as 1, 2, 2.5 or 5 times a power
of 10, so the number drawn can differ from the number requested. For instance,
in the example above, 8 or 9 ticks would need a spacing of 0.857 or 0.75, so
GAUSS draws the same 7 ticks, every 1.

* If the x-axis range is set automatically from the data, the axis ends at the
  data. An end is rounded out to the next tick only when that adds very little
  empty space (at most 5% of the range of the data), so an end is labeled only
  when it falls on a tick, as -3 and 3 do with 7 ticks above but not with 4.

* If the x-axis range is set with :func:`plotSetXRange`, the range is drawn
  exactly as given. The ends of the range are labeled only when they
  fall on a tick. When the requested count divides the range evenly at round
  values, that count is used: for a range of 0 to 1, 5 ticks gives 0, 0.25,
  0.5, 0.75 and 1, and 6 ticks gives 0, 0.2, 0.4, 0.6, 0.8 and 1.

* Otherwise, whether or not the range is set, GAUSS uses the round tick
  values whose number is nearest the request. If two choices are equally
  near, the one with more ticks is used.
  In the example above, 5 ticks, which lies halfway between 3 and 7, gives
  7 ticks, at -3, -2, ..., 3, and 6 ticks also gives 7.

* At most 11 ticks are drawn, and a request for more than 11 is treated as 11;
  at least 2 are drawn, so a request for 1 is treated as 2.
  In the example above, 10, 11 or 12 ticks gives 7 ticks, every 1, because the
  next round spacing, 0.5, would need 13.

* If the graph is too small for the requested number of tick labels to fit,
  fewer are drawn.

* If you zoom the graph, the requested count stays the target, and GAUSS places
  round ticks inside the visible range.

* If a tick interval is also set with :func:`plotSetXTicInterval`, the interval
  is used and the tick count is ignored.

For exact control of the tick positions, and for more control over the x-axis
of time series plots, use :func:`plotSetXTicInterval`, which sets the distance
between ticks and the first labeled value.

.. include:: include/plotattrremark.rst
.. include:: include/plotsetactivexremark.rst

.. seealso:: Functions :func:`plotSetXTicInterval`, :func:`plotSetXRange`, :func:`plotSetYTicCount`, :func:`plotSetXLabel`
