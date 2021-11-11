
plotSetWhichXAxis
==============================================

Purpose
----------------
Assigns curves to the top or bottom x-axis.

Format
----------------
.. function:: plotSetWhichXAxis(&myPlot, which)

    :param &myPlot: A :class:`plotControl` structure pointer.
    :type &myPlot: struct pointer

    :param which: where each element contains either ``"top"`` or ``"bottom"``.
    :type which: string or Nx1 string array


Remarks
-------

.. include:: include/plotattrremark.rst

.. seealso:: Functions :func:`plotSetWhichYAxis`, :func:`plotSetAxesPen`

