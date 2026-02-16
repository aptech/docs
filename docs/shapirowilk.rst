

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

Example 1: Basic usage
+++++++++++++++++++++++

::

    // Generate normal data
    x = rndn(100, 1);

    // Test normality
    struct shapiroWilkOut out;
    out = shapiroWilk(x);

    print "W statistic:" out.w;
    print "p-value:" out.p;

Example 2: Testing non-normal data
+++++++++++++++++++++++++++++++++++

::

    // Generate exponential data (non-normal)
    x = -ln(rndu(100, 1));

    out = shapiroWilk(x);

    if out.p < 0.05;
        print "Reject normality at 5% level";
    endif;

Example 3: With missing values
++++++++++++++++++++++++++++++

::

    // Data with missing values
    x = rndn(100, 1);
    x[1] = miss(0, 0);
    x[50] = miss(0, 0);

    out = shapiroWilk(x);

    // out.n will be 98

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

