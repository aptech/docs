
lagTrim
==============================================

Purpose
----------------

Lags (or leads) a vector a specified number of time periods and removes the incomplete rows.

Format
----------------
.. function:: lagTrim(y, t)

    :param y: data
    :type y: Nx1 vector

    :param t: number of time periods.
    :type t: scalar or Px1 vector

    :returns: y (*NxP matrix*), *y* lagged *t* periods.

Remarks
-------

-  If *t* is positive, :func:`lagTrim` lags *y* back *t* time periods, so the first ``maxc(t)`` observations of *y* are removed.

- If *t* is negative, :func:`lagTrim` leads *y* forward *t* time periods, so the last ``maxc(t)`` observations of *y* are removed.

- :func:`lagn` is similar to :func:`lagTrim`, but :func:`lagn`:

    -  Fills the first *t* rows of each column with missing values.
    -  Uses more memory and is slower than :func:`lagTrim`.

Examples
----------------

Single lag
++++++++++

::

    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
    y_lag = lagTrim(y, 2);

will assign *y_lag* to equal:

::

           1.4 
           2.7 
           3.1 
           2.9 
           3.2

Multiple lags
+++++++++++++

If the number of time periods to lag is a Px1 column vector, then the output matrix with be an NxP matrix where each column contains one of the lags. For example, changing the *nlags* variable from the example above to be a 3x1 column vector like this:

::

    nlags = { 1, 2, 3 };
    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
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

    nlags = { -1, -2, 3 };
    y = { 1.4, 2.7, 3.1, 2.9, 3.2, 2.5, 2.8 };
    y_lag = lagTrim(y, nlags);

will assign *lag_mat* to equal:

::

         3.2      2.5      1.4 
         2.5      2.8      2.7

.. seealso:: Functions :func:`lagn`

