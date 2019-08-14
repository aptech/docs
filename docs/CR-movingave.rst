
movingave
==============================================

Purpose
----------------

Computes moving average of a series.

Format
----------------
.. function:: y = movingave(x, d)

    :param x: data
    :type x: NxK matrix

    :param d: order of moving average.
    :type d: scalar

    :returns: y (*NxK matrix*), filtered series. The first :math:`d-1` rows of *x* are set to missing values.

Remarks
-------

*movingave* is essentially a smoothing time series filter. The moving
average is performed by column and thus it treats the NxK matrix as *K*
time series of length *N*.

.. seealso:: Functions :func:`movingaveWgt`, :func:`movingaveExpwgt`

