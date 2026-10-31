diff
==============================================

Purpose
-------

Computes repeated lag differences of each column of a time series.

Format
------

.. function:: y = diff(x, lag=1, order=1, fill={})

    :param x: Data with observations in rows and one series per column.
    :type x: Nx1 vector, NxK matrix or numeric dataframe

    :param lag: Number of periods between observations in each difference. Default is 1.
    :type lag: non-negative integer scalar

    :param order: Number of times to apply the lag difference. Default is 1.
    :type order: non-negative integer scalar

    :param fill: Value for the first ``lag*order`` rows. The default empty value ``{}`` uses missing values. Accepts any finite real scalar or a missing value.
    :type fill: real scalar

    :return y: Differences of *x*, with dataframe column names retained.
    :rtype y: NxK matrix or dataframe

Examples
--------

First differences and alignment
+++++++++++++++++++++++++++++++

::

    x = { 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 };
    y = diff(x);

The result keeps the original rows, so it remains aligned with dates::

    .
    3
    5
    7
    9
    11
    13
    15
    17
    19

Remove the incomplete rows with::

    y = trimr(diff(x), 1, 0);
    // y = { 3, 5, 7, 9, 11, 13, 15, 17, 19 }

Seasonal and repeated differences
+++++++++++++++++++++++++++++++++

::

    // For quarterly data, compare each value with four quarters earlier.
    y = diff(x, lag=4);
    // y = { ., ., ., ., 24, 32, 40, 48, 56, 64 }

    // Difference the first differences.
    y = diff(x, order=2);
    // y = { ., ., 2, 2, 2, 2, 2, 2, 2, 2 }

    // Apply the seasonal difference twice.
    y = diff(x, lag=4, order=2);
    y = trimr(y, 4*2, 0);
    // y = { 32, 32 }

Multiple columns
++++++++++++++++

::

    x = dfname({ 1 10, 4 20, 9 40, 16 80 }, "a"$|"b");
    y = diff(x, fill=0);

The column names are retained::

    a    b
    0    0
    3   10
    5   20
    7   40

Remarks
-------

.. versionadded:: 27.0.0

For ``order=1``, each complete row is ``x[t,.] - x[t-lag,.]``. Higher orders
repeat this operation on the complete differences. Filled rows never enter
later differences. Exactly the first ``lag*order`` rows are filled.
For positive *lag* and *order*, their product must be less than ``rows(x)``.

If *lag* or *order* is zero, *x* is returned unchanged for every valid *fill*.
The argument checks still apply. A missing value in *x* makes each difference
that uses it missing; other differences are unaffected.

Dataframe columns used in differences must be numeric. A date, string or
category column produces an error naming the column. Select the numeric series
before calling :func:`diff`; retain dates separately to align with the default
output. A zero lag or order returns all columns unchanged.

The first ``lag*order`` rows are missing by default. Rows filled with ``fill=0``
contain zeros, which look like real data. Drop incomplete leading rows before
fitting a model with ``trimr(y, lag*order, 0)``. Other fill values, such as
``fill=-1`` or ``fill=miss(0,0)``, are also accepted. String fill values are errors.

The second positional argument is *lag*: ``diff(x, 2)`` and ``diff(x, lag=2)``
are equivalent. For log differences of positive data, use ``diff(ln(x))``.

Source
------

diff.src

.. seealso:: Functions :func:`lagn`, :func:`lagTrim`, :func:`trimr`
