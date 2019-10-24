
scale3d
==============================================

Purpose
----------------

Fixes the scaling for subsequent graphs. The axes endpoints and increments are computed as a best guess based on
the data passed to it.

.. NOTE:: This function is for use with the deprecated PQG graphics.


Format
----------------
.. function:: scale3d(x, y, z)

    :param x: the x-axis data.
    :type x: matrix

    :param y: the y-axis data.
    :type y: matrix

    :param z: the Z axis data.
    :type z: matrix

Library
-------

pgraph


Remarks
-------

*x*, *y* and *z* must each have at least 2 elements. Only the minimum and
maximum values are necessary.

This routine fixes the scaling for all subsequent graphs until graphset
is called. This also clears `xtics`, `ytics` and `ztics` whenever it is
called.

If any of the arguments is a scalar missing, the main graphics function
will set the scaling for that axis using the actual data.

If an argument has 2 elements, the first will be used for the minimum
and the last will be used for the maximum.

If an argument has 2 elements, and contains a missing value, that end of
the axis will be scaled from the data by the main graphics function.

If you want direct control over the axes endpoints and tick marks, use
`xtics`, `ytics`, or `ztics`. If one of these functions have been called, they
will override `scale3d`.

Source
------

pscale.src

.. seealso:: Functions :func:`scale`, :func:`xtics`, :func:`ytics`, :func:`ztics`
