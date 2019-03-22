
ytics
==============================================

Purpose
----------------
Sets and fixes scaling, axes numbering and tick marks for the Y axis. NOTE: This function is for the deprecated PQG graphics.

Format
----------------
.. function:: ytics(min, max, step, minordiv)

    :param min: the minimum value.
    :type min: scalar

    :param max: the maximum value.
    :type max: scalar

    :param step: the value between major tick marks.
    :type step: scalar

    :param minordiv: the number of minor subdivisions.
    :type minordiv: scalar



Remarks
-------

This routine fixes the scaling for all subsequent graphs until graphset
is called.

This gives you direct control over the axes endpoints and tick marks. If
ytics is called after a call to scale, it will override scale.

X and Y axes numbering may be reversed for xy, logx, logy and loglog
graphs. This may be accomplished by using a negative step value in the
xtics and ytics functions.



Source
------

pscale.src

.. seealso:: Functions :func:`scale`, :func:`xtics`, :func:`ztics`
