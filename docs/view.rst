
view
==============================================

Purpose
----------------

Sets the position of the observer in workbox units for 3-D plots. 

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: view(x, y, z)

    :param x: the X position in workbox units.
    :type x: scalar

    :param y: the Y position in workbox units.
    :type y: scalar

    :param z: the Z position in workbox units.
    :type z: scalar

Remarks
-------

The size of the workbox is set with :func:`volume`. The viewer MUST be outside
of the workbox. The closer the position of the observer, the more
perspective distortion there will be. If :math:`x = y = z`, the projection will
be isometric.

If :func:`view` is not called, a default position will be calculated.

Use :func:`viewxyz` to locate the observer in plot coordinates.

Examples
--------

.. NOTE:: This function is for use with the deprecated PQG graphics.

::

    library pgraph;

    // Set observer position in workbox units for a 3-D plot
    view(5, 5, 5);    // isometric view
    // ... followed by a surface or contour call

Source
------

pgraph.src

.. seealso:: Functions :func:`volume`, :func:`viewxyz`

