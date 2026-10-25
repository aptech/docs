varFitInspect
=============

Purpose
-------
Summarize a fitted VAR, VECM or Bayesian VAR: the sample, the lag order, the largest root of the companion matrix and whether the model is stable.

Format
------

.. function:: inspection = varFitInspect(result)
              inspection = varFitInspect(result, name="VAR(4)", details=1)
              inspection = varFitInspect(result, quiet=1)

   :param result: An instance of a :class:`varResult` structure returned by :func:`varFit` or :func:`vecmToVar`, or of a :class:`bvarResult` structure returned by :func:`bvarFit`.
   :type result: struct

   :param name: Optional keyword, title of the printed summary. Default = "Model".
   :type name: string

   :param details: Optional keyword, set to 1 to also print the coefficients in *inspection.coefficients*, one column per equation, and the mean and root mean square of each equation's residuals. Default = 0.
   :type details: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return inspection: An instance of a :class:`varFitInspection` structure containing:

       .. include:: include/varfitinspection.rst

   :rtype inspection: struct

Examples
--------

Least-Squares VAR and Bayesian VAR
++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    data = data[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    ols = varFit(y, p=5, quiet=1);
    call varFitInspect(ols, name="VAR(5), least squares");

    // Prior centre of each variable's own first lag: 0 for GDP growth,
    // 1 for the other three
    bvar = bvarFit(y, p=5, lag1_prior_mean=0|1|1|1, overall_tightness=0.2, quiet=1);
    call varFitInspect(bvar, name="BVAR(5), Minnesota prior");

The least-squares VAR's summary:

::

    VAR(5), least squares
    ================================================================================
    Sample:                1960Q1-2019Q4    Lags:                                  5
    Observations:                    240    Used after lags:                     235
    Intercept:                       yes    Regressors:                            0
    Trend:                            no
    Coefficients:        21 per equation    Largest root:                     0.9402
    Stable:                          yes

The Bayesian VAR's summary adds the prior settings and the draws:

::

    BVAR(5), Minnesota prior
    ================================================================================
    Sample:                1960Q1-2019Q4    Lags:                                  5
    Observations:                    240    Used after lags:                     235
    Intercept:                       yes    Regressors:                            0
    Coefficients:        21 per equation    Largest root:                     0.9614
    Stable:                          yes    Overall tightness:                   0.2
    Posterior draws:               5,000    Exogenous scale:                       1
    Seed:                             42

    Largest root and stability refer to the posterior-mean coefficients.

Both largest roots are below 1, so both fitted models are stable.

Coefficient Table and Residual Summary
++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    data = data[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    ols = varFit(y, p=2, quiet=1);
    call varFitInspect(ols, name="VAR(2), least squares", details=1);

The printout:

::

    VAR(2), least squares
    ================================================================================
    Sample:                1960Q1-2019Q4    Lags:                                  2
    Observations:                    240    Used after lags:                     238
    Intercept:                       yes    Regressors:                            0
    Trend:                            no
    Coefficients:         9 per equation    Largest root:                     0.9651
    Stable:                          yes

    OLS coefficients, one column per equation

                      gdp_growth  inflation  unemployment  fed_funds
    ----------------------------------------------------------------
    gdp_growth(-1)        0.1568    -0.0091       -0.0199     0.0518
    inflation(-1)        -0.1431     0.4786        0.0058    -0.0262
    unemployment(-1)     -1.4559    -0.9221        1.3947    -0.4424
    fed_funds(-1)        -0.0500     0.7207        0.0131     1.0824
    gdp_growth(-2)        0.1526    -0.1200       -0.0187     0.0066
    inflation(-2)        -0.0882     0.1657       -0.0023     0.1078
    unemployment(-2)      1.6837     0.9051       -0.4345     0.4189
    fed_funds(-2)         0.0826    -0.5557        0.0023    -0.1521
    Constant              1.3875     0.9569        0.2594     0.0085

    Residuals (descriptive summary)

                    Mean     RMS
    ----------------------------
    gdp_growth    0.0000  2.8813
    inflation     0.0000  1.7771
    unemployment  0.0000  0.2194
    fed_funds     0.0000  0.7953

Each column is one equation: the inflation equation's coefficient on the
first lag of the funds rate is 0.7207.

Check Stability in a Program
++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    data = data[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");

    bvar = bvarFit(y, p=5, lag1_prior_mean=0|1|1|1, overall_tightness=0.2, quiet=1);

    // Nothing printed; read the result instead
    inspection = varFitInspect(bvar, quiet=1);
    if inspection.is_stationary;
        print "Stable, largest root " $+ sprintf("%.4f", inspection.max_eigenvalue);
    else;
        print "Not stable, largest root " $+ sprintf("%.4f", inspection.max_eigenvalue);
    endif;
    print inspection.stability_label;

The printout:

::

    Stable, largest root 0.9614
    Stability of posterior-mean coefficient matrix only (not every draw)

VECM Written as a VAR
+++++++++++++++++++++

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/canada.csv"));
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);
    var_result = vecmToVar(vr);

    inspection = varFitInspect(var_result, name="VECM, rank 1, as a VAR(2) in levels");
    print inspection.coefficient_label;

The printout:

::

    VECM, rank 1, as a VAR(2) in levels
    ================================================================================
    Sample:                    rows 1-84    Lags:                                  2
    Observations:                     84    Used after lags:                      82
    Intercept:                       yes    Regressors:                            0
    Trend:                            no
    Coefficients:         9 per equation    Largest root:                     1.0000
    Stable:                           no

    VECM coefficients written as a VAR in levels

With one cointegrating relation among four variables, the VAR in levels has
unit roots, so it is not stable.

Remarks
-------

**What is reported.** varFitInspect reads the fit; it estimates nothing.
The summary gives the sample (row numbers when the data are not dated), the
lag order, the number of observations before and after the lags, whether
the model has an intercept, the number of regressors (*xreg*), the number of
coefficients per equation, the largest root and whether the model is
stable. For a :func:`varFit` or :func:`vecmToVar` result it also shows
whether the model has a trend; for a :func:`bvarFit` result, the overall tightness, the number of
posterior draws, the exogenous scale and the seed. The structure is returned
whether or not anything is printed.

**Stability.** A VAR(p) is stable when every eigenvalue of its companion
matrix (see :func:`varCompanion`) is less than 1 in modulus (Lutkepohl
2005, section 2.1.1). Its forecasts then settle towards the mean instead
of exploding. *inspection.max_eigenvalue* is the largest modulus. For a
:func:`varFit` or :func:`vecmToVar` result, the root and the flag are the
result's own, *result.max_eigenvalue* and *result.is_stationary*.

**VECM written as a VAR.** For a :func:`vecmToVar` result the coefficients
are those of the VECM written as a VAR in levels, not least-squares
estimates, and *inspection.coefficient_label* and
*inspection.stability_label* say so. When the cointegrating rank is less
than the number of variables, the VAR in levels has unit roots: the largest
root is 1, up to rounding, and the model is reported as not stable.

**Bayesian VAR fits.** The root and the flag are evaluated at the posterior
mean of the coefficients, *result.b_post*. When the fit computed them
(*ctl.stability_check* = 1) varFitInspect reports the fit's values;
otherwise it computes them from *result.companion_mean*, by the fit's
rule: stable when the largest modulus is below :math:`1 - 10^{-10}`. They
describe that one coefficient matrix only: some posterior draws can be
unstable even when the posterior mean is stable. The residuals and fitted values
are the fit's, also at *result.b_post*.
The coefficient table and *inspection.coefficients* hold *result.b_post* as
well. It is exact: it does not depend on the seed, unlike *result.b_mean*,
the average of the posterior coefficient draws.

**Residual summary.** With *details* = 1, varFitInspect prints each
equation's residual mean and root mean square (the square root of the sum
of squared residuals divided by T-p). It is descriptive only;
:func:`varDiagnostics` tests the residuals of a least-squares VAR.

**Other results.** varFitInspect takes the results of :func:`varFit`,
:func:`vecmToVar` and :func:`bvarFit`. Other result structures, such as
those of :func:`bvarSvFit` and :func:`vecmFit`, stop with an error. Every
error message starts with "varFitInspect:".

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

Library
-------
timeseries

Source
------
forecast_compare.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`vecmToVar`, :func:`varCompanion`, :func:`varDiagnostics`
