

mvnTest
==============================================

Purpose
----------------

Tests multivariate normality using one or more methods: Henze-Zirkler (default), Mardia's skewness/kurtosis, Doornik-Hansen, or Royston.

Format
----------------
.. function:: out = mvnTest(X [, ctl])
              out = mvnTest(data, formula [, ctl])
              out = mvnTest(filename, formula [, ctl])

    :param X: data matrix with K >= 2 variables.
    :type X: NxK matrix

    :param data: dataframe containing variables.
    :type data: dataframe

    :param filename: name of dataset.
    :type filename: string

    :param formula: formula string specifying variables, e.g., ``"x1 + x2 + x3"``.
    :type formula: string

    :param ctl: Optional argument, instance of an :class:`mvnTestControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ctl.output
              - scalar, print results. Default = 1.

                :1: Print results.
                :0: Suppress output.

            * - ctl.miss
              - scalar, missing value handling. Default = 0.

                :0: Error if missing values present.
                :1: Listwise deletion of rows with missing values.

            * - ctl.method
              - string, test method to use. Default = ``"hz"``.

                :``"hz"``: Henze-Zirkler test (recommended omnibus test).
                :``"mardia"``: Mardia skewness and kurtosis tests.
                :``"dh"``: Doornik-Hansen test.
                :``"royston"``: Royston test (based on Shapiro-Wilk).
                :``"all"``: Run all four methods.

    :type ctl: struct

    :return out: instance of :class:`mvnTestOut` structure:

        .. csv-table::
            :widths: auto

            "out.n", "scalar, sample size after any listwise deletion."
            "out.k", "scalar, number of variables."
            "out.skewStat", "scalar, Mardia normalized skewness statistic (approx N(0,1))."
            "out.skewP", "scalar, p-value for skewness test."
            "out.kurtStat", "scalar, Mardia normalized kurtosis statistic (approx N(0,1))."
            "out.kurtP", "scalar, p-value for kurtosis test."
            "out.combStat", "scalar, Mardia combined chi-squared statistic."
            "out.combP", "scalar, p-value for combined test (chi-sq df=2)."
            "out.hzStat", "scalar, Henze-Zirkler test statistic."
            "out.hzP", "scalar, Henze-Zirkler p-value (lognormal approximation)."
            "out.hzBeta", "scalar, Henze-Zirkler smoothing parameter."
            "out.dhStat", "scalar, Doornik-Hansen chi-squared statistic."
            "out.dhP", "scalar, Doornik-Hansen p-value."
            "out.dhDf", "scalar, Doornik-Hansen degrees of freedom (2*k)."
            "out.royStat", "scalar, Royston H statistic."
            "out.royP", "scalar, Royston p-value."
            "out.royDf", "scalar, Royston equivalent degrees of freedom."

    :rtype out: struct

Examples
----------------

Example 1: Basic usage with matrix input
+++++++++++++++++++++++++++++++++++++++++

::

    // Generate multivariate normal data
    X = rndn(100, 3);

    // Test normality using default Henze-Zirkler method
    out = mvnTest(X);

Example 2: Using dataframe with formula
+++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    data = loadd("mydata.csv");

    // Test specific variables
    out = mvnTest(data, "income + age + education");

Example 3: Run all tests with control structure
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create control structure
    struct mvnTestControl ctl;
    ctl = mvnTestControlCreate();
    ctl.method = "all";

    // Run all four tests
    out = mvnTest(X, ctl);

    // Check individual results
    if out.hzP < 0.05;
        print "Henze-Zirkler rejects normality";
    endif;

Remarks
----------------

- The Henze-Zirkler test is recommended as the default because it has good power against a wide range of alternatives and is affine invariant.

- For the Henze-Zirkler test, observations are limited to 5000 due to O(N^2) memory requirements.

- The Royston test requires 4 <= N <= 2000 observations.

- The Doornik-Hansen test requires N >= 8 observations.

- All tests require at least 2 variables (K >= 2).

- Fields in the output structure are set to missing (.) for methods not run.

References
----------------

Henze, N. & Zirkler, B. (1990). "A Class of Invariant Consistent Tests for Multivariate Normality." Communications in Statistics - Theory and Methods, 19(10), 3595-3617.

Mardia, K.V. & Foster, K. (1983). "Omnibus Tests of Multinormality Based on Skewness and Kurtosis." Communications in Statistics - Theory and Methods, 12(2), 207-221.

Doornik, J.A. & Hansen, H. (2008). "An Omnibus Test for Univariate and Multivariate Normality." Oxford Bulletin of Economics and Statistics, 70, 927-939.

Royston, J.P. (1992). "Approximating the Shapiro-Wilk W-Test for Non-Normality." Statistics and Computing, 2, 117-119.

.. seealso:: Functions :func:`mvnTestControlCreate`, :func:`shapiroWilk`

