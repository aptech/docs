
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

Examples
----------------

::

    x = { 1, 3, 5, 7, 9, 11 };

    // Equal weights for a 2-period moving average
    w = { 0.5, 0.5 };
    y = movingaveWgt(x, 2, w);
    print y;

The code above produces the following output:

::

           .
    2.0000000
    4.0000000
    6.0000000
    8.0000000
    10.000000

The first element is missing because there are not enough prior observations for the window.

.. seealso:: Functions :func:`movingave`, :func:`movingaveExpwgt`

