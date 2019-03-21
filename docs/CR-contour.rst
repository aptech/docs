
contour
==============================================

Purpose
----------------

Graphs a matrix of contour data.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph


Format
----------------
.. function:: contour(x, y, z)

    :param x: the *X* axis data. *K* must be odd.
    :type x: 1xK vector

    :param y: the *Y* axis data. *N* must be odd.
    :type y: Nx1 vector

    :param z: the matrix of height data to be plotted.
    :type z: NxK matrix

Global Input
------------

.. data:: \_plev

    Kx1 vector, user-defined contour levels for contour. Default 0.
    
.. data:: \_pzclr

    Nx1 or Nx2 vector. This controls the Z level colors. 
    See :func:`surface` for a complete description of how to set this global.

Remarks
-------

A vector of evenly spaced contour levels will be generated automatically
from the *z* matrix data. Each contour level will be labeled. For
unlabeled contours, use :func:`ztics`.

To specify a vector of your own unequal contour levels, set the vector
`\_plev` before calling :func:`contour`.

To specify your own evenly spaced contour levels, see :func:`ztics`.

Source
------

pcontour.src

.. seealso:: :func:`surface`

