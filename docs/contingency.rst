

contingency
==============================================

Purpose
----------------

Computes comprehensive statistics and measures of association for contingency tables, including chi-squared tests, Fisher's exact test, odds ratios, relative risk, and ordinal association measures.

Format
----------------
.. function:: out = contingency(freqTable [, ctl])
              out = contingency(x1, x2 [, ctl])
              out = contingency(data, formula [, ctl])
              out = contingency(filename, formula [, ctl])

    :param freqTable: IxJ matrix of observed cell frequencies.
    :type freqTable: matrix

    :param x1: first categorical variable (row variable).
    :type x1: Nx1 vector

    :param x2: second categorical variable (column variable).
    :type x2: Nx1 vector

    :param data: dataframe containing variables.
    :type data: dataframe

    :param filename: name of dataset.
    :type filename: string

    :param formula: formula string of the form ``"rowvar ~ colvar"``.
    :type formula: string

    :param ctl: Optional argument, instance of a :class:`contingencyControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ctl.output
              - scalar, print results. Default = 1.

                :1: Print results.
                :0: Suppress output.

            * - ctl.ordinal
              - scalar, compute ordinal measures. Default = 1.

                :1: Compute ordinal association measures (Gamma, Tau-b, Tau-c, Somer's D).
                :0: Skip ordinal measures.

    :type ctl: struct

    :return out: instance of :class:`contingencyOut` structure:

        .. csv-table::
            :widths: auto

            "out.table", "IxJ matrix, observed frequency table."
            "out.expected", "IxJ matrix, expected frequencies under independence."
            "out.rowLabels", "Ix1 string array, row category labels."
            "out.colLabels", "Jx1 string array, column category labels."
            "out.nObs", "scalar, total number of observations."
            "out.chiSq", "scalar, Pearson chi-squared statistic."
            "out.chiSqDf", "scalar, degrees of freedom for chi-squared."
            "out.chiSqP", "scalar, p-value for chi-squared test."
            "out.lrChiSq", "scalar, likelihood ratio (G-squared) statistic."
            "out.lrChiSqP", "scalar, p-value for likelihood ratio test."
            "out.yatesChiSq", "scalar, Yates-corrected chi-squared (2x2 only)."
            "out.yatesP", "scalar, p-value for Yates-corrected test."
            "out.mcnemarChiSq", "scalar, McNemar symmetry test (square tables only)."
            "out.mcnemarDf", "scalar, degrees of freedom for McNemar test."
            "out.mcnemarP", "scalar, p-value for McNemar test."
            "out.phi", "scalar, phi coefficient."
            "out.cramersV", "scalar, Cramer's V."
            "out.contingencyCoef", "scalar, Pearson's contingency coefficient."
            "out.spearmanRho", "scalar, Spearman rank correlation."
            "out.kappa", "scalar, Cohen's kappa (square tables only)."
            "out.kappaASE", "scalar, asymptotic standard error for kappa."
            "out.yulesQ", "scalar, Yule's Q (2x2 only)."
            "out.yulesQASE", "scalar, ASE for Yule's Q."
            "out.yulesY", "scalar, Yule's Y (2x2 only)."
            "out.yulesYASE", "scalar, ASE for Yule's Y."
            "out.oddsRatio", "scalar, odds ratio (2x2 only)."
            "out.oddsRatioLo", "scalar, 95% CI lower bound for odds ratio."
            "out.oddsRatioHi", "scalar, 95% CI upper bound for odds ratio."
            "out.relRisk", "scalar, relative risk (2x2 only)."
            "out.relRiskLo", "scalar, 95% CI lower bound for relative risk."
            "out.relRiskHi", "scalar, 95% CI upper bound for relative risk."
            "out.fisherP", "scalar, Fisher's exact test p-value (2x2 only)."
            "out.gamma", "scalar, Goodman-Kruskal gamma."
            "out.gammaASE", "scalar, ASE for gamma."
            "out.tauB", "scalar, Kendall's tau-b."
            "out.tauBASE", "scalar, ASE for tau-b."
            "out.tauC", "scalar, Stuart's tau-c."
            "out.tauCASE", "scalar, ASE for tau-c."
            "out.somersD", "scalar, Somer's D (column dependent)."
            "out.somersDASE", "scalar, ASE for Somer's D."
            "out.lambda", "scalar, Goodman-Kruskal lambda (column dependent)."
            "out.lambdaASE", "scalar, ASE for lambda."
            "out.uncertainty", "scalar, uncertainty coefficient (column dependent)."
            "out.uncertaintyASE", "scalar, ASE for uncertainty coefficient."
            "out.stdResid", "IxJ matrix, standardized (Pearson) residuals."
            "out.adjResid", "IxJ matrix, adjusted residuals."
            "out.diagnostics.minExpected", "scalar, minimum expected cell frequency."
            "out.diagnostics.pctExpectedLt5", "scalar, percent of cells with expected frequency < 5."
            "out.diagnostics.hasZeroCell", "scalar, 1 if any observed cell is zero."
            "out.diagnostics.warnings", "string array, warning messages about assumptions."

    :rtype out: struct

Examples
----------------

Example 1: Frequency table input
++++++++++++++++++++++++++++++++

::

    // Aspirin and heart attack data (Physicians' Health Study)
    // Rows: Placebo, Aspirin
    // Cols: MI, No MI
    x = { 189 10845,
          104 10933 };

    out = contingency(x);

This produces:

::

    Contingency Table Analysis
    Observations: 22071    Table: 2x2

    Tests of Independence
    ------------------------------------------------------------
                         Statistic       Value      df     p-value
               Pearson Chi-Squared     25.0139       1      0.0000
                  Likelihood Ratio     25.1211       1      0.0000

    Risk Measures (2x2)
    ------------------------------------------------------------
                           Measure       Value                  95% CI
                        Odds Ratio      1.8321            [1.4400, 2.3311]
                     Relative Risk      1.8177            [1.4371, 2.2990]
              Fisher Exact p-value      0.0000

Example 2: Two categorical vectors
++++++++++++++++++++++++++++++++++

::

    // Smoking status and lung disease
    smoking = { 1, 1, 1, 2, 2, 2, 1, 1, 2, 2 };   // 1=smoker, 2=non-smoker
    disease = { 1, 1, 2, 2, 2, 2, 1, 2, 2, 2 };   // 1=disease, 2=no disease

    out = contingency(smoking, disease);

Example 3: Dataframe with formula
+++++++++++++++++++++++++++++++++

::

    // Load data
    data = loadd("survey.csv");

    // Test association between education and income level
    out = contingency(data, "education ~ income");

Example 4: Suppress output
++++++++++++++++++++++++++

::

    struct contingencyControl ctl;
    ctl = contingencyControlCreate();
    ctl.output = 0;  // silent mode

    out = contingency(x, ctl);

    // Access specific statistics
    print "Odds ratio: " out.oddsRatio;
    print "95% CI: [" out.oddsRatioLo "," out.oddsRatioHi "]";

Remarks
----------------

- **Chi-squared validity**: The chi-squared approximation may be unreliable when more than 20% of expected cell frequencies are less than 5, or any expected frequency is less than 1. Warnings are issued automatically.

- **Fisher's exact test**: Computed for 2x2 tables. Recommended for small samples where chi-squared may be unreliable.

- **Odds ratio and relative risk**: Only computed for 2x2 tables. Confidence intervals use the Woolf (log-transform) method. Returns missing values if any cell is zero.

- **Ordinal measures**: Gamma, tau-b, tau-c, and Somer's D assume ordinal (ranked) categories. Set ``ctl.ordinal = 0`` to skip these if variables are purely nominal.

- **Cohen's kappa**: Only computed for square tables (same number of rows and columns). Measures agreement beyond chance.

- **Residual analysis**: Adjusted residuals follow approximately a standard normal distribution under independence. Values exceeding |2| suggest significant departure from independence for that cell.

References
----------------

Agresti, Alan. 2002. *Categorical Data Analysis*. 2nd ed. New York: John Wiley and Sons.

Bishop, Yvonne, Stephen Fienberg and Paul Holland. 1975. *Discrete Multivariate Analysis: Theory and Practice*. Cambridge, Mass.: MIT Press.

.. seealso:: Functions :func:`tabulate`, :func:`frequency`, :func:`crossprod`

