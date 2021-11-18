
plotSetBoxWidth
==============================================

Purpose
----------------
Sets the width of the boxes in box plots.



Format
----------------
.. function:: plotSetBoxWidth(&myPlot, boxWidth)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param boxWidth: Width of the boxes in plot set between 0 and 1. If set to 1, the boxes will touch each other. Default box width is 0.5.
    :type boxWidth: Scalar

Examples
----------------
.. figure:: _static/images/plotsetboxwidth-cr.jpg
   :scale: 50 %

::

  // Import data
  auto2 = loadd(getGAUSSHome() $+ "examples/auto2.dta");

  // Declare plotControl structure
  // and fill in default values for box plot
  struct plotControl myPlot;
  myPlot = plotGetDefaults("box");

  // Set box width to 50% of available width
  plotSetBoxWidth(&myPlot, 0.5);

  // Draw the two boxes
  plotBox(myPlot, auto2, "mpg ~ foreign");


Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotBox`, :func:`plotGetDefaults`, :func:`plotSetBarWidth`
