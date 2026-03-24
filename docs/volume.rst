
volume
==============================================

Purpose
----------------
Sets the length, width, and height ratios of the 3-D workbox.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: volume(x, y, z)

    :param x: the X length of the 3-D workbox.
    :type x: scalar

    :param y: the Y length of the 3-D workbox.
    :type y: scalar

    :param z: the Z length of the 3-D workbox.
    :type z: scalar

Remarks
-------

The ratio between these values is what is important. If :func:`volume` is not
called, a default workbox will be calculated.

Examples
--------

.. NOTE:: This function is for use with the deprecated PQG graphics.

::

    library pgraph;

    // Set the 3-D workbox to a 2:1:1 ratio (wider in X)
    volume(2, 1, 1);
    // ... followed by a surface or contour call

Source
------

pgraph.src

.. seealso:: Functions :func:`view`

