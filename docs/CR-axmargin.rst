
axmargin
==============================================

Purpose
----------------
Sets absolute margins for the plot axes which control placement and size of plot. NOTE: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: axmargin(l, r, t, b)

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

:func:`axmargin` sets an absolute distance from the axes to the edge of the
graphic panel. Note that the user is responsible for allowing enough
space in the margin if axes labels, numbers and title are used on the
graph, since axmargin does not size the plot automatically as in the
case of margin.

All input inch values for this procedure are based on a full size window
of 9x6.855 inches. If this procedure is used within a graphic panel, the
values will be scaled to window inches automatically.

If both :func:`margin` and :func:`axmargin` are used for a graph, :func:`axmargin` will override
any sizes specified by margin.

Examples
----------------
The statement:

::

    library pgraph;
    axmargin(1, 1, .5, .855);

will create a plot area of 7 inches horizontally by 5.5 inches
vertically, and positioned 1 inch right and .855 up from the lower
left corner of the graphic panel/page.

Source
------------

pgraph.src
