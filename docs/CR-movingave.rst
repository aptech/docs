
movingave
==============================================

Purpose
----------------

Computes moving average of a series.

Format
----------------
.. function:: movingave(x,  d)

    :param x: NxK matrix.
    :type x: TODO

    :param d: order of moving average.
    :type d: scalar

    :returns: y (*NxK matrix*), filtered series. The first  d-1 rows of x are set to missing values.

