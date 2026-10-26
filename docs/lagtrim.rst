
lagTrim
==============================================

Purpose
----------------

Lags (or leads) a vector, matrix or dataframe a specified number of time periods and removes the incomplete rows.

Format
----------------
.. function:: y = lagTrim(y, t)

    :param y: data
    :type y: Nx1 vector, NxK matrix or dataframe

    :param t: number of time periods. NOTE: If `y` has multiple columns, `t` must be a scalar.
    :type t: scalar or Px1 vector

    :return y: *y* lagged *t* periods.

    :rtype y: NxP matrix

Examples
----------------

Single lag vector
+++++++++++++++++++++

::

    // Specify number of lags
    nlags = 2;

    // Define y matrix
    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag y nlags number of lags
    // and trim missing values
    y_lag = lagTrim(y, nlags);

will assign *y_lag* to equal:

::

           1.4
           2.7
           3.1
           2.9
           3.2

Multiple lags with a vector
++++++++++++++++++++++++++++++

If the number of time periods to lag is a Px1 column vector, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the *nlags* variable from the example above to be a 3x1 column vector like this:

::

    // Specify to compute the 1, 2, and 3 lags
    nlags = { 1, 2, 3 };

    // Define y vector
    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Compute the 1, 2, and 3 lags of y
    // and trim missing values
    y_lag = lagTrim(y, nlags);

will assign *lag_mat* to equal:

::

         3.1      2.7      1.4
         2.9      3.1      2.7
         3.2      2.9      3.1
         2.5      3.2      2.9

Multiple leads
++++++++++++++

If the number of time periods to lag is a Px1 column vector, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the *nlags* variable from the example above to be a 3x1 column vector like this:

::

    // Specify nlags to find
    // the 1st and 2nd lead
    // and 3rd lag of y
    nlags = { -1, -2, 3 };

    // Define y vector
    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };

    // Lag y using nlags
    y_lag = lagTrim(y, nlags);

will assign *lag_mat* to equal:

::

         3.2      2.5      1.4
         2.5      2.8      2.7


Single lag with multi-column dataframe
++++++++++++++++++++++++++++++++++++++++

::

    // Get the first 10 observations of 'price' and 'rep78'
    // from the auto dataset
    auto = loadd(getGAUSSHome() $+ "examples/auto2.dta");
    auto = auto[1:10,"price" "rep78"];

    // Specify number of lags
    nlags = 2;

    // Lag both variables in 'auto', 
    // nlags number of lags
    // and trim missing values
    auto_lag = lagTrim(auto, nlags);

will assign *auto_lag* to equal the matrix below. It doesn't keep the variable names, and *rep78* holds its category keys (3 for Average, 4 for Good):

::

       4099.0000        3.0000000
       4749.0000        3.0000000
       3799.0000                .
       4816.0000        3.0000000
       7827.0000        4.0000000
       5788.0000        3.0000000
       4453.0000                .
       5189.0000        3.0000000

Remarks
----------

- If *t* is positive, :func:`lagTrim` lags *y* back *t* time periods, so the first ``maxc(t)`` observations of *y* are removed.

- If *t* is negative, :func:`lagTrim` leads *y* forward *t* time periods, so the last ``abs(minc(t))`` observations of *y* are removed.

- Each element of *t* is truncated to a whole number of periods, and must not be a missing value or an infinity. *y* must have more rows than the span of the truncated lags, ``maxc(trunc(t)|0) - minc(trunc(t)|0)``, so that at least one row remains. Otherwise :func:`lagTrim` gives an error. An empty *y* is returned unchanged.

- :func:`lagn` is similar to :func:`lagTrim`, but :func:`lagn`:

    -  Fills the first *t* rows of each column with missing values.
    -  Uses more memory and is slower than :func:`lagTrim`.

.. seealso:: Functions :func:`lagn`
