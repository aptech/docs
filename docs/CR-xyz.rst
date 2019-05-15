
xyz
==============================================

Purpose
----------------
Graphs X vs. Y vs. Z using Cartesian coordinates.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: xyz(x, y, z)

    :param x: Each column contains the X values for a particular line.
    :type x: Nx1 or NxK matrix

    :param y: Each column contains the Y values for a particular line.
    :type y: Nx1 or NxK matrix

    :param z: Each column contains the Z values for a particular line.
    :type z: Nx1 or NxK matrix

Remarks
-------

Missing values are ignored when plotting symbols. If missing values are
encountered while plotting a curve, the curve will end and a new curve
will begin plotting at the next non-missing value.

Source
------

pxyz.src

