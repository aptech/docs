
lagn
==============================================

Purpose
----------------

Lags (or leads) a matrix a specified number of time periods for time series analysis.

Format
----------------
.. function:: y = lagn(x, t[, fill])

    :param x: data
    :type x: NxK matrix

    :param t: number of time periods.
    :type t: scalar or Px1 vector

    :param fill: Optional input, the value to fill the newly missing observations. Default is a missing value, ``.``.
    :type fill: scalar or Px1 vector

    :return y: *x* lagged *t* periods.

    :rtype y: NxK matrix

Examples
----------------

Basic lag
+++++++++

::

    // Set number of lags
    nlags = 2;

    // Define x
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag x, nlags number of lags
    x_lag2 = lagn(x, nlags);

will assign *x_lag2* to equal:

::

             .
             .
           1.4
           2.7
           3.1
           2.9
           3.2

Basic lag with fill value
+++++++++++++++++++++++++

::

    // Specify number of lags
    nlags = 2;

    // Define x vector
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Define fill value for missing values
    fill = 0;

    // Lag x, nlags number of lags
    // and fill missings with 0
    x_lag2 = lagn(x, nlags, fill);

will assign *x_lag2* to equal:

::

             0
             0
           1.4
           2.7
           3.1
           2.9
           3.2

Creating multiple lags
++++++++++++++++++++++

If the number of time periods to lag is a Px1 column vector, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the *nlags* variable from the example above to be a 3x1 column vector like this:

::

    // Specify to compute 1, 2, and 3
    // lags
    nlags = { 1, 2, 3 };

    // Define x vector
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag x 1, 2, and 3 times
    lag_mat = lagn(x, nlags);

will assign *lag_mat* to equal:

::

           .        .        .
         1.4        .        .
         2.7      1.4        .
         3.1      2.7      1.4
         2.9      3.1      2.7
         3.2      2.9      3.1
         2.5      3.2      2.9

Creating multiple lags with different fill values
+++++++++++++++++++++++++++++++++++++++++++++++++

If the fill value and the number of time periods to lag are both Px1 column vectors, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the *nlags* and fill variables from the example above to be a 5x1 column vector like this:

::

    // Specify number of lags
    nlags = { 1, 2, 3, 4, 5 };

    // Specify a different fill value
    // for each number of lags
    fill = {  0.2270,
              0.0488,
              0.6927,
              0.6478,
              0.9160 };

    // Define x to matrix of zeroes
    x = zeros(5, 1);

    // Compute lags of x using
    // fill vector to fill missing values
    lag_mat = lagn(x, nlags, fill);

will assign *lag_mat* to equal:

::

    0.2270   0.0488   0.6927   0.6478   0.9160
         0   0.0488   0.6927   0.6478   0.9160
         0        0   0.6927   0.6478   0.9160
         0        0        0   0.6478   0.9160
         0        0        0        0   0.9160

Remarks
-------

If *t* is positive, :func:`lagn` lags *x* back *t* time periods, so the first *t*
observations of *y* are filled with missing values. If *t* is negative, :func:`lagn`
leads *x* forward *t* time periods, so the last *t* observations of *y* are filled
with missing values.

For higher performance if you plan to trim of the first *nlags* rows, use :func:`lagTrim`.

Source
------

lag.src

.. seealso:: Functions :func:`lagtrim`
