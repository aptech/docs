
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

Examples
----------------

Basic lag
+++++++++

::

    // Define y vector
    y = { 1.2,
          3.4,
          2.5,
          4.1,
          2.8 };

    // Take first lag of y
    y_lag = lag1(y);

    // Print output
    print y_lag;

will return:

::

                .
        1.2000000
        3.4000000
        2.5000000
        4.1000000

Multiple Columns
++++++++++++++++

::

  // Define y vector
  y_mat = { 1.2 4.3,
        3.4 0.97,
        2.5 1.4,
        4.1 0.7,
        2.8 4.1};

  // Take first lag of y
  y_lag = lag1(y_mat);

  // Print output
  print y_lag;


will return:

::

            .                .
    1.2000000        4.3000000
    3.4000000       0.97000000
    2.5000000        1.4000000
    4.1000000       0.70000000

Remarks
-------

:func:`lag1` lags *x* by one time period, so the first observations of *y* are
missing. :func:`lag1` assumes that each column of the input is a different time
series and that each row is an observation. Therefore if a 1xK row
vector is passed to :func:`lag1`, it will return a 1xK of missing values.


Source
------

lag.src

.. seealso:: Functions :func:`lagn`, :func:`ismiss`, :func:`packr`

