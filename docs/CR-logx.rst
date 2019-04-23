
logx
==============================================

Purpose
----------------

Graphs X vs. Y using log coordinates for the X axis.

.. NOTE:: This function is for use with the deprecated PQG graphics. Use :func:`plotLogX` instead.

Library
-------

pgraph

Format
----------------
.. function:: logx(x, y)

    :param x:  Each column contains the X values for a particular line.
    :type x: Nx1 or NxM matrix

    :param y:  Each column contains the Y values for a particular line.
    :type y: Nx1 or NxM matrix

Source
------

plogx.src

.. seealso:: Functions :func:`xy`, :func:`logy`, :func:`loglog`

