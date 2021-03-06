
plotAddBox
==============================================

Purpose
----------------
Adds a box graph to an existing graph.

Format
----------------
.. function:: plotAddBox([myPlot, ]grp, y)

    :param myPlot: Optional argument. A :class:`plotControl` structure
    :type myPlot: struct

    :param grp: contains the group numbers corresponding to each column of *y* data. If scalar 0, a sequence from 1 to ``cols(y)`` will be generated automatically for the x-axis.
    :type grp: 1xM vector

    :param y: Each column represents the set of *y* values for an individual percentiles box symbol.
    :type y: NxM matrix

Remarks
-------

:func:`plotAddBox` may only add a box graph to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

.. seealso:: Functions :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddPolar`, :func:`plotAddXY`
