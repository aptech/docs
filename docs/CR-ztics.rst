
ztics
==============================================

Purpose
----------------
Sets and fixes scaling, axes numbering and tick marks for the Z axis.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: ztics(min, max, step, minordiv)

    :param min: the minimum value.
    :type min: scalar

    :param max: the maximum value.
    :type max: scalar

    :param step: the value between major tick marks.
    :type step: scalar

    :param minordiv: the number of minor subdivisions.
        If this function is used with :func:`contour`, contour labels will be placed every 
        *minordiv* levels. If 0, there will be no labels.
    :type minordiv: scalar

Remarks
-------

This routine fixes the scaling for all subsequent graphs until :func:`graphset`
is called.

This gives you direct control over the axes endpoints and tick marks. If
:func:`ztics` is called after a call to :func:`scale3d`, it will override :func:`scale3d`.

Source
------

pscale.src

.. seealso:: Functions :func:`scale3d`, :func:`xtics`, :func:`ytics`, :func:`contour`

