adfTest
=======

Purpose
-------
Augmented Dickey-Fuller test of the null hypothesis that a series has a unit root.

Format
------

.. function:: adf = adfTest(y)
              adf = adfTest(y, max_lags={}, trend="c", quiet=0, lags={}, ic="aic")

   :param y: The series to test. A dataframe may contain one numeric column and one date-typed column, which is removed before testing. At least six finite, nonconstant observations are required. Missing values are errors; no rows are dropped.
   :type y: Nx1 vector or dataframe

   :param max_lags: Optional keyword, finite nonnegative integer ceiling for lag selection. Zero searches only lag zero. Cannot be supplied with *lags*. Default = the capped Schwert ceiling described in Remarks.
   :type max_lags: scalar

   :param trend: Optional keyword, deterministic terms: ``"n"`` (none), ``"c"`` (constant), or ``"ct"`` (constant and linear trend). Accepted in any letter case. Default = ``"c"``.
   :type trend: string

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param lags: Optional keyword, exact number of lagged differences. Must be a finite nonnegative integer. Skips lag selection; cannot be supplied with *max_lags*. Default = omitted (automatic selection).
   :type lags: scalar

   :param ic: Optional keyword, ``"aic"`` or ``"bic"``, accepted in any letter case. Used only during automatic lag selection. Default = ``"aic"``.
   :type ic: string

   :return adf: An instance of a :class:`adfResult` structure containing:

       .. list-table::
          :widths: auto

          * - adf.statistic
            - Scalar, ADF t-statistic. More negative values give stronger evidence against a unit root.
          * - adf.p_value
            - Scalar, asymptotic MacKinnon (1994) p-value.
          * - adf.lags
            - Scalar, selected or exact number of lagged differences.
          * - adf.trend
            - String, canonical lowercase ``"n"``, ``"c"``, or ``"ct"``.
          * - adf.crit_values
            - 3x1 vector, finite-sample critical values at 1%, 5%, and 10%, in that order.
          * - adf.nobs
            - Scalar, final regression observations: *n* - *lags* - 1.
          * - adf.n
            - Scalar, number of input observations after removing an optional date column.
          * - adf.test_name
            - String, ``"Augmented Dickey-Fuller"``.

   :rtype adf: struct

Examples
--------

Test annual Lake Huron levels with a constant, then with a constant and a linear trend. Both choose the lag automatically.

::

    new;
    library timeseries;

    lake_levels = loadd(getGAUSSHome("pkgs/timeseries/examples/data/lakehuron.csv"));
    struct adfResult adf;
    adf = adfTest(lake_levels);
    adf = adfTest(lake_levels, trend="ct");

The output:

::

    Augmented Dickey-Fuller test (H0: unit root)
    ================================================================================
    Deterministic:              constant    Observations:     98 (regression uses 96)
    Lags:                              1    Statistic:                        -3.898
    p-value:                       0.002    5% critical:                      -2.892
    Result: reject a unit root at the 5% level.

    Augmented Dickey-Fuller test (H0: unit root)
    ================================================================================
    Deterministic:      constant + trend    Observations:     98 (regression uses 96)
    Lags:                              1    Statistic:                        -4.154
    p-value:                       0.005    5% critical:                      -3.457
    Result: reject a unit root at the 5% level.

Remarks
-------

The null hypothesis is a unit root. Rejection supports stationarity around
the specified deterministic terms. The printed 5% decision uses the p-value.

The regression includes the lagged level and *k* lagged first differences,
with the constant and trend chosen by *trend*. The statistic is the
t-statistic on the lagged level.

With no exact lag supplied, the default is AIC selection over *k* = 0 to
*kmax*. For *n* input levels, the default search ceiling is

.. math::

   k_{\max} = \min\left(\left\lceil12(n/100)^{1/4}\right\rceil,
   \left\lfloor n/2\right\rfloor-d-1\right),

where *d* is 0, 1, or 2 for ``"n"``, ``"c"``, or ``"ct"``. An explicit
*lags* or *max_lags* cannot exceed :math:`\lfloor n/2\rfloor-d-1`.

Every candidate uses the same *m* = *n* - *kmax* - 1 observations. For
residual sum of squares SSR and *r* = *d* + *k* + 1 regression coefficients,
AIC is :math:`m\ln(\mathrm{SSR}/m)+2r` and BIC is
:math:`m\ln(\mathrm{SSR}/m)+\ln(m)r`. Exact ties choose the smaller lag.
The selected regression is then refit using all *n* - *k* - 1 usable
observations. Giving ``lags=k`` fits that final sample directly.

P-values use the asymptotic MacKinnon (1994) approximation. Critical values
use MacKinnon (2010) finite-sample response surfaces at the final *nobs*,
with one series and the requested deterministic terms. An asymptotic
p-value and a finite-sample critical value can give different decisions
near a cutoff.

Invalid trend or lag keywords, missing or nonfinite values, constant data,
and infeasible lags give an error. A singular or saturated regression, or
residual variance too small to distinguish from numerical rounding, also
gives an error. A failed search candidate stops the test; it is not skipped.

References
----------

- MacKinnon, J.G. (1994). "Approximate asymptotic distribution functions for unit-root and cointegration tests." *Journal of Business & Economic Statistics*, 12(2), 167-176.
- MacKinnon, J.G. (2010). "Critical values for cointegration tests." Queen's Economics Department Working Paper No. 1227.
- Schwert, G.W. (1989). "Tests for unit roots: A Monte Carlo investigation." *Journal of Business & Economic Statistics*, 7(2), 147-159.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`ppTest`, :func:`kpssTest`, :func:`engleGrangerTest`, :func:`dfglsTest`, :func:`stationarityTests`
