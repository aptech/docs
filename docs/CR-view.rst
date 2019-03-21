
view
==============================================

Purpose
----------------

Sets the position of the observer in workbox units for 3-D plots. NOTE: This function is for the deprecated PQG graphics.

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

The size of the workbox is set with volume. The viewer MUST be outside
of the workbox. The closer the position of the observer, the more
perspective distortion there will be. If x = y = z, the projection will
be isometric.

If view is not called, a default position will be calculated.

Use viewxyz to locate the observer in plot coordinates.

