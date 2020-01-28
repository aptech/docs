
plotAddBar
==============================================

Purpose
----------------
Adds a bar or a set of bars to an existing graph.

Format
----------------
.. function:: plotAddBar([myPlot, ]val, ht)

    :param myPlot: Optional argument. A :class:`plotControl` structure
    :type myPlot: struct

    :param val: bar labels.

        .. csv-table::
          :widths: auto

          "Scalar 0", "a sequence from 1 to ``rows(ht)`` will be created."
          "Numeric", "*val* represents the label indices."
          "String array", "*val* represents labels and the bar is added to the existing matching label. If the label in *val* is not found on the existing graph, the label and associated bar is added to the end of the plot window."

    :type val: Nx1 numeric vector or Nx1 string array

    :param ht: bar heights.

        *K* overlapping or side-by-side sets of *N* bars will be graphed.

    :type ht: NxK numeric vector

Remarks
-------

:func:`plotAddBar` may only add bars to 2-D graphs.

This function will not change any of the current graph's settings other
than to resize the view as necessary to display the new curve.

.. seealso:: Functions :func:`plotAddHist`, :func:`plotAddHistF`, :func:`plotAddHistP`, :func:`plotAddPolar`, :func:`plotAddXY`
