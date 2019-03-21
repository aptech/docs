
lagn
==============================================

Purpose
----------------

Lags (or leads) a matrix a specified number of time periods for time series analysis.

Format
----------------
.. function:: lagn(x, t) 
			  lagn(x, t, fill)

    :param x: 
    :type x: NxK matrix

    :param t: number of time periods.
    :type t: scalar or Px1 vector

    :param fill: scalar or Px1 vector, the value to fill the newly missing observations. Default is a missing value, '.'.
    :type fill: Optional input

    :returns: y (*NxK matrix*), x lagged  t periods.

Examples
----------------

Basic lag
+++++++++

::

    nlags = 2;
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
    x_lag2 = lagn(x, nlags);

will assign x_lag2 to equal:

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

    nlags = 2;
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
    fill = 0;
    x_lag2 = lagn(x, nlags, fill);

will assign x_lag2 to equal:

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

If the number of time periods to lag is a Px1 column vector, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the nlags variable from the example above to be a 3x1 column vector like this:

::

    nlags = { 1, 2, 3 };
    x = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
    lag_mat = lagn(x, nlags);

will assign lag_mat to equal:

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

If the fill value and the number of time periods to lag are both Px1 column vectors, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the nlags and fill variables from the example above to be a 5x1 column vector like this:

::

    nlags = { 1, 2, 3, 4, 5 };
    fill = {  0.2270, 
              0.0488, 
              0.6927, 
              0.6478, 
              0.9160 };
    x = zeros(5, 1);
    lag_mat = lagn(x, nlags, fill);

will assign lag_mat to equal:

::

    0.2270   0.0488   0.6927   0.6478   0.9160 
         0   0.0488   0.6927   0.6478   0.9160 
         0        0   0.6927   0.6478   0.9160 
         0        0        0   0.6478   0.9160 
         0        0        0        0   0.9160

Remarks
+++++++

If t is positive, lagn lags x back t time periods, so the first t
observations of y are filled with missing values. Ift is negative, lagn
lags x forwardt time periods, so the lastt observations of y are filled
with missing values.

For higher performance if you plan to trim of the first nlags rows, use
lagTrim.

Source
++++++

lag.src

.. seealso:: Functions :func:`lagtrim`
