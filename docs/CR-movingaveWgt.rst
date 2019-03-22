
movingaveWgt
==============================================

Purpose
----------------

Computes weighted moving average of a series

Format
----------------
.. function:: movingaveWgt(x, d, w)

    :param x: 
    :type x: NxK matrix

    :param d: order of moving average.
    :type d: scalar

    :param w: weights.
    :type w: dx1 vector

    :returns: y (*NxK matrix*), filtered series. The first d-1 rows of x are set to missing values.



Remarks
-------

movingaveWgt is essentially a smoothing time series filter with weights.
The moving average as performed by column and thus it treats the NxK
matrix as K time series of length N.

.. seealso:: Functions :func:`movingave`, :func:`movingaveExpwgt`
