
movingaveExpwgt
==============================================

Purpose
----------------

Computes exponentially weighted moving average of a series.

Format
----------------
.. function:: movingaveExpwgt(x,  d,  p)

    :param x: NxK matrix.
    :type x: TODO

    :param d: order of moving average.
    :type d: scalar

    :param p: smoothing coefficient where 0 > p > 1.
    :type p: scalar

    :returns: y (*NxK matrix*), filtered series. The first d-1 rows of x are set to missing values.

