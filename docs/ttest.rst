

ttest
==============================================

Purpose
----------------

Performs two-sample and paired t-tests for comparing means between groups.

Format
----------------
.. function:: out = ttest(y1, y2 [, ctl])
              out = ttest(data, formula [, ctl])
              out = ttest(filename, formula [, ctl])

    :param y1: first sample.
    :type y1: Nx1 vector

    :param y2: second sample.
    :type y2: Mx1 vector

    :param data: dataframe containing variables.
    :type data: dataframe

    :param filename: name of dataset.
    :type filename: string

    :param formula: formula string of the form ``"y ~ group"``.
    :type formula: string

    :param ctl: Optional argument, instance of a :class:`ttestControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ctl.output
              - scalar, print results. Default = 1.

                :1: Print results.
                :0: Suppress output.

            * - ctl.paired
              - scalar, test type. Default = 0.

                :0: Independent samples t-test.
                :1: Paired samples t-test.

            * - ctl.alternative
              - scalar, alternative hypothesis. Default = 0.

                :0: Two-sided (mean1 != mean2).
                :1: Greater (mean1 > mean2).
                :-1: Less (mean1 < mean2).

            * - ctl.mu
              - scalar, null hypothesis difference in means. Default = 0.

            * - ctl.varEqual
              - scalar, variance assumption. Default = 0.

                :0: Welch t-test (unequal variances).
                :1: Pooled variance (equal variances assumed).

            * - ctl.confLevel
              - scalar, confidence level for confidence interval. Default = 0.95.

            * - ctl.miss
              - scalar, missing value handling. Default = 0.

                :0: Error if missing values present.
                :1: Listwise deletion of missing values.

    :type ctl: struct

    :return out: instance of :class:`ttestOut` structure:

        .. csv-table::
            :widths: auto

            "out.groups", "2x1 string array, group labels."
            "out.mean", "2x1 vector, group means."
            "out.sd", "2x1 vector, group standard deviations."
            "out.n", "2x1 vector, group sample sizes."
            "out.meanDiff", "scalar, difference in means (group1 - group2)."
            "out.tEq", "scalar, t-statistic assuming equal variances."
            "out.dfEq", "scalar, degrees of freedom (equal variances)."
            "out.pEq", "scalar, p-value (equal variances)."
            "out.tWelch", "scalar, t-statistic (Welch)."
            "out.dfWelch", "scalar, degrees of freedom (Satterthwaite approximation)."
            "out.pWelch", "scalar, p-value (Welch)."
            "out.fStat", "scalar, F-statistic for variance equality test."
            "out.dfF", "2x1 vector, numerator and denominator df for F-test."
            "out.pF", "scalar, p-value for F-test of equal variances."
            "out.ci", "1x2 vector, confidence interval for mean difference."
            "out.confLevel", "scalar, confidence level used."

    :rtype out: struct

Examples
----------------

Example 1: Two-sample t-test with vectors
+++++++++++++++++++++++++++++++++++++++++

::

    // Two independent samples
    y1 = { 23, 25, 28, 22, 24 };
    y2 = { 30, 32, 29, 35, 31 };

    // Perform t-test
    out = ttest(y1, y2);

::

    Two-Sample t-test

    Descriptive Statistics
    ------------------------------------------------------------
              Group         N        Mean     Std Dev
            Group 1         5     24.4000      2.3022
            Group 2         5     31.4000      2.3022

    Mean Difference:      -7.0000

    Test of Means
    ------------------------------------------------------------
                  Method         t        df     p-value
     Welch (unequal var)   -4.8076       8.0      0.0013
      Pooled (equal var)   -4.8076         8      0.0013

    Test of Variances
    ------------------------------------------------------------
                                 F        df     p-value
                  F-test    1.0000     4,  4      1.0000

     95% Confidence Interval: [  -10.3576,    -3.6424]

The small p-value (0.0013) indicates a statistically significant difference between the two groups.

Example 2: Paired t-test
++++++++++++++++++++++++

::

    // Before and after measurements
    before = { 120, 125, 118, 130, 122 };
    after = { 115, 120, 112, 125, 118 };

    struct ttestControl ctl;
    ctl = ttestControlCreate();
    ctl.paired = 1;

    out = ttest(before, after, ctl);

::

    Paired Samples t-test

    Descriptive Statistics
    ------------------------------------------------------------
              Group         N        Mean     Std Dev
            Group 1         5    123.0000      4.6904
            Group 2         5    118.0000      4.9497

    Mean Difference:       5.0000

    Paired t-test
    ------------------------------------------------------------
                                 t        df     p-value
                  Paired   15.8114         4      0.0001

     95% Confidence Interval: [    4.1220,     5.8780]

Example 3: One-sided test
+++++++++++++++++++++++++

::

    y1 = { 23, 25, 28, 22, 24 };
    y2 = { 30, 32, 29, 35, 31 };

    struct ttestControl ctl;
    ctl = ttestControlCreate();
    ctl.alternative = 1;  // test if group1 > group2

    out = ttest(y1, y2, ctl);

The one-sided p-value (0.9993) is large because group 1's mean (24.4) is actually *less than* group 2's mean (31.4), contradicting the alternative hypothesis that group 1 > group 2.

Example 4: Using dataframe with formula
+++++++++++++++++++++++++++++++++++++++

::

    // Load data
    data = loadd(getGAUSSHome("examples/auto2.dta"), "mpg + foreign");

    // Test if mpg differs by origin
    struct ttestControl ctl;
    ctl = ttestControlCreate();

    out = ttest(data, "mpg ~ foreign", ctl);

::

    Two-Sample t-test

    Descriptive Statistics
    ------------------------------------------------------------
              Group         N        Mean     Std Dev
            Group 1        52     19.8269      4.7433
            Group 2        22     24.7727      6.6112

    Mean Difference:      -4.9458

    Test of Means
    ------------------------------------------------------------
                  Method         t        df     p-value
     Welch (unequal var)   -3.1797      30.5      0.0034
      Pooled (equal var)   -3.6308        72      0.0005

    Test of Variances
    ------------------------------------------------------------
                                 F        df     p-value
                  F-test    1.9427    21, 51      0.0549

     95% Confidence Interval: [   -8.1201,    -1.7716]

Foreign cars average 4.9 more mpg than domestic. The Welch test (p = 0.0034) confirms the difference is statistically significant.

Remarks
----------------

- By default, performs Welch's t-test which does not assume equal variances. Set ``ctl.varEqual = 1`` for the pooled variance version.

- The output includes both equal-variance and Welch statistics for comparison.

- An F-test for equality of variances is automatically computed.

- For paired tests, both samples must have the same length.

.. seealso:: Functions :func:`ttestControlCreate`, :func:`contingency`, :func:`mvnTest`, :func:`shapiroWilk`

