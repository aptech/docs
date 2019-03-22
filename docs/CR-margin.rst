
margin
==============================================

Purpose
----------------

Sets the margins for the current graph's graphic panel. Note: This function is for use with the deprecated PQG graphics. For similar functionality, use plotCustomLayout.

Format
----------------
.. function:: margin(l, r, t, b)

    :param l: the left margin in inches.
    :type l: scalar

    :param r: the right margin in inches.
    :type r: scalar

    :param t: the top margin in inches.
    :type t: scalar

    :param b: the bottom margin in inches.
    :type b: scalar



Remarks
-------

By default, the dimensions of the graph are the same as the graphic
panel dimensions. With this function the graph dimensions may be
decreased. The result will be a smaller plot area surrounded by the
specified margin. This procedure takes into consideration the axes
labels and numbers for correct placement.

All input inch values for this procedure are based on a full size window
of 9x6.855 inches. If this procedure is used with a graphic panel, the
values will be scaled to ''window inches'' automatically.

If the axes must be placed an exact distance from the edge of the page,
axmargin should be used.



Source
------

pgraph.src

.. seealso:: Functions :func:`axmargin`
