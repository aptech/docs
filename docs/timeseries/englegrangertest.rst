engleGrangerTest
================

Purpose
-------
Engle-Granger residual test of the null hypothesis that the supplied I(1) series are not cointegrated.

Format
------

.. function:: eg = engleGrangerTest(y, x)
              eg = engleGrangerTest(y, x, trend="c", lags={}, max_lags={}, ic="aic", quiet=0)

   :param y: Dependent series, with at least six finite, nonconstant observations. A dataframe may include one date-typed column, which is removed. Missing values are errors; no rows are dropped.
   :type y: Nx1 vector or dataframe

   :param x: One to five regressor series in the same row order as *y*. Must have the same number of rows and contain only finite, non-missing values. A dataframe may include one date-typed column, which is removed. Regressors must be linearly independent jointly with the deterministic terms.
   :type x: NxK matrix or dataframe, K = 1 to 5

   :param trend: Optional keyword, deterministic terms in the static cointegrating regression: ``"c"`` (constant) or ``"ct"`` (constant and linear trend). Accepted in any letter case; ``"n"`` is not supported. Default = ``"c"``.
   :type trend: string

   :param lags: Optional keyword, exact number of lagged differences. Must be a finite nonnegative integer. Skips lag selection; cannot be supplied with *max_lags*. Default = omitted (automatic selection).
   :type lags: scalar

   :param max_lags: Optional keyword, finite nonnegative integer ceiling for lag selection. Zero searches only lag zero. Cannot be supplied with *lags*. Default = the capped Schwert ceiling described in Remarks.
   :type max_lags: scalar

   :param ic: Optional keyword, ``"aic"`` or ``"bic"``, accepted in any letter case. Used only during automatic lag selection. Default = ``"aic"``.
   :type ic: string

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return eg: An instance of a :class:`egResult` structure containing:

       .. list-table::
          :widths: auto

          * - eg.statistic
            - Scalar, residual ADF t-statistic. More negative values give stronger evidence for cointegration.
          * - eg.p_value
            - Scalar, asymptotic MacKinnon (1994) cointegration p-value.
          * - eg.crit_values
            - 3x1 vector, finite-sample cointegration critical values at 1%, 5%, and 10%.
          * - eg.lags
            - Scalar, selected or exact number of lagged residual differences.
          * - eg.n
            - Scalar, number of input observations after removing optional date columns.
          * - eg.nobs
            - Scalar, final residual ADF observations: *n* - *lags* - 1.
          * - eg.trend
            - String, canonical lowercase static-regression trend: ``"c"`` or ``"ct"``.
          * - eg.coefficients
            - (K+d)x1 vector of static OLS coefficients: constant, linear trend if present, then the *x* coefficients in column order. Here *d* is 1 for ``"c"`` and 2 for ``"ct"``.
          * - eg.test_name
            - String, ``"Engle-Granger"``.

   :rtype eg: struct

Examples
--------

Test whether log real consumption and log real GDP share a long-run path, with a constant and then with a constant and trend.

::

    new;
    library timeseries;

    macro_path = getGAUSSHome("pkgs/timeseries/examples/data/engle_granger_macrodata.csv");
    macro_levels = asMatrix(loadd(macro_path, "realcons + realgdp"));
    log_consumption = ln(macro_levels[.,1]);
    log_gdp = ln(macro_levels[.,2]);

    struct egResult eg;
    eg = engleGrangerTest(log_consumption, log_gdp);
    eg = engleGrangerTest(log_consumption, log_gdp, trend="ct");

The output:

::

    Engle-Granger test (H0: no cointegration)
    ================================================================================
    Deterministic:              constant    Observations:     203 (regression uses 202)
    Lags:                              0    Statistic:                        -3.535
    p-value:                       0.029    5% critical:                      -3.367
    Result: reject no cointegration at the 5% level.

    Engle-Granger test (H0: no cointegration)
    ================================================================================
    Deterministic:      constant + trend    Observations:     203 (regression uses 202)
    Lags:                              0    Statistic:                        -3.537
    p-value:                       0.091    5% critical:                      -3.828
    Result: cannot reject no cointegration at the 5% level.

Remarks
-------

This test assumes that *y* and each column of *x* are I(1): their first
differences are stationary. The null is no cointegration. Rejection
supports a stationary long-run combination of the supplied series.
The printed 5% decision uses the cointegration p-value.

First, OLS fits *y* on *x* and the requested deterministic terms. For
``"ct"``, the linear trend is *t* = 1 to *n*. Next, an ADF regression
tests the fitted residuals, with no constant or trend in that second
regression. The returned *coefficients* describe the static regression
of *y* on *x*. They are not a normalized cointegrating vector; its
coefficients on the stochastic series are :math:`(1,-b_1,\ldots,-b_K)`.

With no exact lag supplied, AIC selects *k* from 0 through *kmax*. The
default ceiling is

.. math::

   k_{\max}=\min\left(\left\lceil12(n/100)^{1/4}\right\rceil,
   \left\lfloor n/2\right\rfloor-1\right).

The cap uses no deterministic terms because the residual ADF has none,
regardless of the static regression's *trend*. An explicit *lags* or
*max_lags* cannot exceed :math:`\lfloor n/2\rfloor-1`. All candidates
use *m* = *n* - *kmax* - 1 observations. AIC is
:math:`m\ln(\mathrm{SSR}/m)+2(k+1)` and BIC is
:math:`m\ln(\mathrm{SSR}/m)+\ln(m)(k+1)` for the residual regression.
Exact ties choose the smaller lag. The selected regression is refit on
all *nobs* = *n* - *k* - 1 usable residual observations.

Critical values use MacKinnon (2010) finite-sample cointegration response
surfaces evaluated at final *nobs*. P-values use the asymptotic MacKinnon
(1994) cointegration approximation. Both use the static regression's
deterministic terms and *N* = *K* + 1 stochastic series (2 to 6).
These are cointegration calibrations, not the ordinary single-series
Dickey-Fuller distribution. An asymptotic p-value and a finite-sample
critical value can give different decisions near a cutoff.

A constant or a constant and trend with one to five regressors are the
supported specifications. Other trends or regressor counts, mismatched
row counts, missing or nonfinite inputs, constant *y*, invalid keywords,
and infeasible lags give an error. Collinear regressors or deterministics,
a saturated regression, and degenerate cointegrating or residual variance
also give an error. A failed lag-search candidate stops the test.

References
----------

- Engle, R.F. and C.W.J. Granger (1987). "Co-integration and error correction: Representation, estimation, and testing." *Econometrica*, 55(2), 251-276.
- MacKinnon, J.G. (1994). "Approximate asymptotic distribution functions for unit-root and cointegration tests." *Journal of Business & Economic Statistics*, 12(2), 167-176.
- MacKinnon, J.G. (2010). "Critical values for cointegration tests." Queen's Economics Department Working Paper No. 1227.
- Schwert, G.W. (1989). "Tests for unit roots: A Monte Carlo investigation." *Journal of Business & Economic Statistics*, 7(2), 147-159.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`adfTest`, :func:`ppTest`, :func:`kpssTest`, :func:`dfglsTest`, :func:`stationarityTests`, :func:`vecmFit`
