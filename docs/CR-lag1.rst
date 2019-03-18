
lag1
==============================================

Purpose
----------------

Lags a matrix by one time period for time series analysis.

Format
----------------
.. function:: lag1(x)

    :param x: Nx1 column vector or NxK matrix.
    :type x: TODO

    :returns: y (*NxK matrix*), x lagged 1 period.

Examples
----------------

::

    y = { 1.2,
          3.4,
          2.5,
          4.1,
          2.8 };
    y_lag = lag1(y);
    print y_lag;

will return:

::

    . 
        1.2000000 
        3.4000000 
        2.5000000 
        4.1000000

Source
++++++

lag.src

.. seealso:: Functions :func:`lagn`, :func:`ismiss`, :func:`packr`
