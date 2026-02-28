

shapiroWilk
==============================================

Purpose
----------------

Computes the Shapiro-Wilk W test for univariate normality.

Format
----------------
.. function:: out = shapiroWilk(x)

    :param x: data vector. Missing values are removed automatically.
    :type x: Nx1 vector

    :return out: instance of :class:`shapiroWilkOut` structure:

        .. csv-table::
            :widths: auto

            "out.w", "scalar, W test statistic. Range [0, 1], values near 1 indicate normality."
            "out.p", "scalar, p-value. Probability of observing W this small or smaller under normality."
            "out.n", "scalar, effective sample size after removing missing values."

    :rtype out: struct

Examples
----------------

Example 1: Normal data
+++++++++++++++++++++++

::

    rndseed 42;

    // Generate normal data
    x = rndn(100, 1);

    // Test normality
    struct shapiroWilkOut out;
    out = shapiroWilk(x);

    print "W statistic:" out.w;
    print "p-value:    " out.p;

::

    W statistic:      0.97879310
    p-value:          0.10700545

The p-value (0.107) is above 0.05, so we fail to reject normality — consistent with the data being generated from a normal distribution.

Example 2: Non-normal data
+++++++++++++++++++++++++++++++++++

::

    rndseed 42;

    // Generate exponential data (non-normal)
    x = -ln(rndu(100, 1));

    struct shapiroWilkOut out;
    out = shapiroWilk(x);

    print "W statistic:" out.w;
    print "p-value:    " out.p;

::

    W statistic:      0.91599435
    p-value:       8.6824924e-06

The very small p-value (< 0.001) strongly rejects normality, correctly detecting that exponential data is not normally distributed.

Example 3: With missing values
++++++++++++++++++++++++++++++

::

    rndseed 42;

    // Data with missing values
    x = rndn(100, 1);
    x[1] = miss(0, 0);
    x[50] = miss(0, 0);

    struct shapiroWilkOut out;
    out = shapiroWilk(x);

    print "W statistic:" out.w;
    print "p-value:    " out.p;
    print "n:          " out.n;

::

    W statistic:      0.97858132
    p-value:          0.11011458
    n:                 98.000000

Missing values are automatically removed. The effective sample size (``out.n = 98``) reflects the two removed observations.

Remarks
----------------

- The W statistic ranges from 0 to 1. Values close to 1 indicate the data is consistent with a normal distribution.

- Sample size must satisfy 3 <= N <= 5000.

- Missing values are automatically removed before computation.

- The test uses the Blom approximation for expected normal order statistics and applies Royston's (1992, 1995) transformation for p-value calculation.

- For multivariate normality testing, see :func:`mvnTest`.

References
----------------

Shapiro, S.S. & Wilk, M.B. (1965). "An Analysis of Variance Test for Normality (Complete Samples)." Biometrika, 52(3/4), 591-611.

Royston, J.P. (1995). "Remark AS R94: A Remark on Algorithm AS 181: The W-test for Normality." Applied Statistics, 44(4), 547-551.

.. seealso:: Functions :func:`mvnTest`, :func:`jarqueBera`

