
viewxyz
==============================================

Purpose
----------------
To set the position of the observer in plot coordinates for 3-D plots.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: viewxyz(x, y, z)

    :param x: the X position in plot coordinates.
    :type x: scalar

    :param y: the Y position in plot coordinates.
    :type y: scalar

    :param z: the Z position in plot coordinates.
    :type z: scalar

Remarks
-------

The viewer MUST be outside of the workbox. The closer the observer, the
more perspective distortion there will be.

If :func:`viewxyz` is not called, a default position will be calculated.

Use :func:`view` to locate the observer in workbox units.

Examples
--------

.. NOTE:: This function is for use with the deprecated PQG graphics.

::

    library pgraph;

    // Set observer position in plot coordinates for a 3-D plot
    viewxyz(10, 10, 5);
    // ... followed by a surface or contour call

Source
------

pgraph.src

.. seealso:: Functions :func:`volume`, :func:`view`

