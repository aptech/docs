
bar
==============================================

Purpose
----------------
Generates a bar graph.

.. NOTE:: This function is for the deprecated PQG graphics, use :func:`plotBar` instead.

Library
-------

pgraph

Format
----------------
.. function:: bar(val, ht)

    :param val: bar labels. If scalar 0, a sequence from 1 to :code:`rows(ht)` will be created.
    :type val: Nx1 numeric vector

    :param ht: bar heights.
    :type ht: NxK numeric vector

Global Input
----------------

.. data:: \_pbarwid

    *scalar*, width and type of bars in bar graphs and histograms. The valid
    range is 0-1. If this is 0, the bars will be a single pixel wide. If
    this is 1, the bars will touch each other.

    If this value is positive, the bars will overlap. If negative, the bars
    will be plotted side-by-side. The default is 0.5.

.. data:: \_pbartyp

    *Kx2 matrix*. The first column controls the bar shading:

    .. csv-table::
        :widths: auto

        0,"no shading."
        1,"dots."
        2,"vertical cross-hatch."
        3,"diagonal lines with positive slope."
        4,"diagonal lines with negative slope."
        5,"diagonal cross-hatch."
        6,"solid"


    The second column controls the bar color.


Examples
----------------

In this example, three overlapping sets of bars will be created. The three heights for the ith
bar are stored in :math:`x[i,.]`.

::

    library pgraph;
    graphset;

    t = seqa(0, 1, 10);
    x =(t^2/2).*(1~0.7~0.3);

    _plegctl = { 1 4 };
    _plegstr = "Accnt #1\000Accnt #2\000Accnt #3";
    title("Theoretical Savings Balance");
    xlabel("Years");
    ylabel("Dollars x 1000");

    // Set color of the bars
    _pbartyp = { 1 10 };
    _pnum = 2;

    // Use t vector to label x-axis.
    bar(t, x);

Remarks
-------

Use :func:`scale` or :func:`ytics` to fix the scaling for the bar heights.


Source
------------

pbar.src

.. seealso:: Functions :func:`asclabel`, :func:`xy`, :func:`logx`, :func:`logy`, :func:`loglog`, :func:`scale`, :func:`hist`
