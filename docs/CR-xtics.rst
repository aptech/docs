
xtics
==============================================

Purpose
----------------
Sets and fixes scaling, axes numbering and tick marks for the x-axis.

.. NOTE:: This function is for the deprecated PQG graphics.

Library
-------

pgraph

Format
----------------
.. function:: xtics(min, max, step, minordiv)

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

This routine fixes the scaling for all subsequent graphs until :func:`graphset`
is called.

This gives you direct control over the axes endpoints and tick marks. If
:func:`xtics` is called after a call to :func:`scale`, it will override :func:`scale`.

X and Y axes numbering may be reversed for :func:`xy`, :func:`logx`, :func:`logy`, and :func:`loglog`
graphs. This may be accomplished by using a negative step value in the :func:`xtics` and :func:`ytics` functions.

Source
------

pscale.src

.. seealso:: Functions :func:`scale`, :func:`ytics`, :func:`ztics`
