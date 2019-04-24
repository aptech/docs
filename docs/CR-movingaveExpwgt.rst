
movingaveExpwgt
==============================================

Purpose
----------------

Computes exponentially weighted moving average of a series.

Format
----------------
.. function:: movingaveExpwgt(x, d, p)

    :param x: data
    :type x: NxK matrix

    :param d: order of moving average.
    :type d: scalar

    :param p: smoothing coefficient where :math:`0 > p > 1`.
    :type p: scalar

    :returns: y (*NxK matrix*), filtered series. The first :math:`d-1` rows of *x* are set to missing values.

Remarks
-------

:func:`movingaveExpwgt` is smoothing time series filter using exponential
weights. The moving average as performed by column and thus it treats
the NxK matrix as *K* time series of length *N*.

.. seealso:: Functions :func:`movingaveWgt`, :func:`movingave`

