
polar
==============================================

Purpose
----------------

Graph data using polar coordinates. 

.. NOTE:: This function is for use only with the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: polar(radius, theta)

    :param radius: Each column contains the magnitude for a particular line.
    :type radius: Nx1 or NxM matrix

    :param theta: Each column represents the angle values for a particular line.
    :type theta: Nx1 or NxM matrix

Source
------

polar.src

.. seealso:: Functions :func:`xy`, :func:`logx`, :func:`logy`, :func:`loglog`, :func:`scale`, :func:`xtics`, :func:`ytics`

