
plotSetYMinorTicCount
==============================================

Purpose
----------------
Controls the number of minor ticks to place between major ticks on the y-axis of a 2-D plot.

Format
----------------
.. function:: plotSetYMinorTicCount(&myPlot, num_tics)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param num_tics: the number of minor ticks to place between major ticks on the y-axis.
    :type num_tics: Scalar

Examples
----------------
.. figure:: _static/images/plotsetyminorticcount-cr.png
   :scale: 50 %

::

  // Declare plotControl structure
  struct plotControl myPlot;

  // Initialize plotControl structure
  myPlot = plotGetDefaults("scatter");

  // Set x-axis major and minor grid lines on
  plotSetYGrid(&myPlot, "both");

  // Set y-axis minor grid lines tick count
  plotSetYMinorTicCount(&myPlot, 4);

  // Create a scatter plot of random data
  plotScatter(myPlot, seqa(1, 1, 10 ), rndn(10, 1));

Remarks
-------
- The y-axis minor grid must turned on using :func:`plotSetYGrid` or :func:`plotSetGrid` for the minor axis to show.

    .. include:: include/plotattrremark.rst

    .. seealso:: Functions :func:`plotSetYGrid`, :func:`plotSetYGridPen`, :func:`plotSetYMinorGridPen`, :func:`plotSetXMinorTicCount`
