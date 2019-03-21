
scale
==============================================

Purpose
----------------

Fixes the scaling for subsequent graphs. The
axes endpoints and increments are computed as a best guess based on
the data passed to it.
Note: This function is for use with the deprecated PQG graphics.
 

Format
----------------
.. function:: scale(x, y)

    :param x: the X axis data.
    :type x: matrix

    :param y: the Y axis data.
    :type y: matrix



Remarks
-------

x and y must each have at least 2 elements. Only the minimum and maximum
values are necessary.

This routine fixes the scaling for all subsequent graphs until graphset
is called. This also clears xtics and ytics whenever it is called.

If either of the arguments is a scalar missing, the main graphics
function will set the scaling for that axis using the actual data.

If an argument has 2 elements, the first will be used for the minimum
and the last will be used for the maximum.

If an argument has 2 elements, and contains a missing value, that end of
the axis will be scaled from the data by the main graphics function.

If you want direct control over the axes endpoints and tick marks, use
xtics or ytics. If xtics or ytics have been called after scale, they
will override scale.



Source
------

pscale.src

