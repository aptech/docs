
ztics
==============================================

Purpose
----------------
Sets and fixes scaling, axes numbering and tick marks for the Z axis. NOTE: This function is for the deprecated PQG graphics.

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
        If this function is used with contour, contour labels
        will be placed every  minordiv levels. If 0, there
        will be no labels.
    :type minordiv: scalar



Remarks
-------

This routine fixes the scaling for all subsequent graphs until graphset
is called.

This gives you direct control over the axes endpoints and tick marks. If
ztics is called after a call to scale3d, it will override scale3d.



Source
------

pscale.src

