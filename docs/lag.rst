
lag
==============================================

Purpose
----------------

Lags a matrix by one or more time periods for time series analysis.

Format
----------------
.. function:: y = lag(x[, n_lags[, fill]])

    :param x: data
    :type x: NxK matrix or dataframe

    :param n_lags: Optional, number of time periods to lag. Default = 1.
    :type n_lags: scalar

    :param fill: Optional, the value to fill newly missing observations. Default is a missing value, ``.``.
    :type fill: scalar

    :return y: *x* lagged *n_lags* periods.

    :rtype y: NxK matrix

Examples
----------------

Lag by one period
++++++++++++++++++

::

    x = { 1.2,
          3.4,
          2.5,
          4.1,
          2.8 };

    // Default: lag by one period
    y = lag(x);

After the above code, *y* will be:

::

                .
        1.2000000
        3.4000000
        2.5000000
        4.1000000

Lag by multiple periods
++++++++++++++++++++++++

::

    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag by 3 periods
    y = lag(x, 3);

After the above code, *y* will be:

::

             .
             .
             .
           1.4
           2.7
           3.1
           2.9

Lag with a fill value
++++++++++++++++++++++

::

    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag by 2, fill missing with 0
    y = lag(x, 2, 0);

After the above code, *y* will be:

::

             0
             0
           1.4
           2.7
           3.1
           2.9
           3.2

Use in formula strings
+++++++++++++++++++++++

Because :func:`lag` accepts a single required argument, it can be used
directly as a data transformation in formula strings:

::

    // Regress y on one lag of x
    call olsmt(df, "y ~ lag(x)");

Remarks
-------

If *n_lags* is positive, :func:`lag` shifts *x* back by *n_lags* time periods,
so the first *n_lags* observations of *y* are filled with the *fill* value.

:func:`lag` is equivalent to :func:`lag1` when called with one argument, and
equivalent to :func:`lagn` when called with two or three arguments. It is
provided as a convenience, particularly for use in formula strings where
only single-argument functions are supported.

Source
------

lag.src

.. seealso:: Functions :func:`lag1`, :func:`lagn`, :func:`lagTrim`
