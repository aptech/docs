
movingaveWgt
==============================================

Purpose
----------------

Computes weighted moving average of a series

Format
----------------
.. function:: y = movingaveWgt(x, d, w)

    :param x: data
    :type x: NxK matrix

    :param d: order of moving average.
    :type d: scalar

    :param w: weights.
    :type w: dx1 vector

    :return y: filtered series. The first :math:`d-1` rows of *x* are set to missing values.

    :rtype y: NxK matrix

Remarks
-------

:func:`movingaveWgt` is essentially a smoothing time series filter with weights.
The moving average as performed by column and thus it treats the NxK
matrix as *K* time series of length *N*.

.. seealso:: Functions :func:`movingave`, :func:`movingaveExpwgt`

