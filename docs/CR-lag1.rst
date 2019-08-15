
lag1
==============================================

Purpose
----------------

Lags a matrix by one time period for time series analysis.

Format
----------------
.. function:: y = lag1(x)

    :param x: data
    :type x: Nx1 column vector or NxK matrix

    :return y: *x* lagged 1 period.

    :rtype y: NxK matrix

Remarks
-------

:func:`lag1` lags *x* by one time period, so the first observations of *y* are
missing. :func:`lag1` assumes that each column of the input is a different time
series and that each row is an observation. Therefore if a 1xK row
vector is passed to :func:`lag1`, it will return a 1xK of missing values.


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
------

lag.src

.. seealso:: Functions :func:`lagn`, :func:`ismiss`, :func:`packr`

