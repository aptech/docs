dfglsTest
=========

Purpose
-------
Dickey-Fuller GLS test of the null hypothesis that a series has a unit root, after removing a constant or a constant and linear trend by generalized least squares.

Format
------

.. function:: dfg = dfglsTest(y)
              dfg = dfglsTest(y, trend="c", lags={}, max_lags={}, ic="maic", quiet=0)

   :param y: The series to test. A dataframe may contain one numeric column and one date-typed column, which is removed before testing. At least six finite, nonconstant observations are required. Missing values are errors; no rows are dropped.
   :type y: Nx1 vector or dataframe

   :param trend: Optional keyword, deterministic terms: ``"c"`` (constant) or ``"ct"`` (constant and linear trend). Accepted in any letter case; ``"n"`` is not supported. Default = ``"c"``.
   :type trend: string

   :param lags: Optional keyword, exact number of lagged differences. Must be a finite nonnegative integer. Skips lag selection; cannot be supplied with *max_lags*. Default = omitted (automatic selection).
   :type lags: scalar

   :param max_lags: Optional keyword, finite nonnegative integer ceiling for lag selection. Zero searches only lag zero. Cannot be supplied with *lags*. Default = the capped Schwert ceiling described in Remarks.
   :type max_lags: scalar

   :param ic: Optional keyword, ``"maic"`` (modified AIC), ``"aic"``, or ``"bic"``, accepted in any letter case. All use GLS-detrended data. Used only during automatic lag selection. Default = ``"maic"``.
   :type ic: string

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return dfg: An instance of a :class:`dfglsResult` structure containing:

       .. list-table::
          :widths: auto

          * - dfg.statistic
            - Scalar, DF-GLS t-statistic. More negative values give stronger evidence against a unit root.
          * - dfg.p_value
            - Scalar, asymptotic MacKinnon (1994) no-constant Dickey-Fuller p-value for ``"c"``; GAUSS missing for ``"ct"``.
          * - dfg.crit_values
            - 3x1 vector, critical values at 1%, 5%, and 10%. See Remarks for the different constant and trend calibrations.
          * - dfg.lags
            - Scalar, selected or exact number of lagged differences.
          * - dfg.n
            - Scalar, number of input levels after removing an optional date column.
          * - dfg.nobs
            - Scalar, final ADF observations: *n* - *lags* - 1.
          * - dfg.trend
            - String, canonical lowercase GLS deterministic terms: ``"c"`` or ``"ct"``.
          * - dfg.ic
            - String, canonical lowercase selection criterion; ``"none"`` when *lags* is supplied.
          * - dfg.test_name
            - String, ``"Dickey-Fuller GLS"``.

   :rtype dfg: struct

Examples
--------

Test annual Lake Huron levels with the default modified AIC, then include a linear trend. The trend case reports critical values without a p-value.

::

    new;
    library timeseries;

    lake_levels = loadd(getGAUSSHome("pkgs/timeseries/examples/data/lakehuron.csv"));
    struct dfglsResult dfg;
    dfg = dfglsTest(lake_levels);
    dfg = dfglsTest(lake_levels, trend="ct");

The output:

::

    Dickey-Fuller GLS test (H0: unit root)
    ================================================================================
    Deterministic:              constant    Observations:     98 (regression uses 95)
    Lags:                              2    Statistic:                        -2.293
    Criterion:                      maic
    Asymptotic p:                  0.021    5% critical:                      -1.944
    Result: reject a unit root at the 5% level.

    Dickey-Fuller GLS test (H0: unit root)
    ================================================================================
    Deterministic:      constant + trend    Observations:     98 (regression uses 97)
    Lags:                              0    Statistic:                        -3.201
    Criterion:                      maic
    p-value is not available for the trend case.
    5% critical:                  -3.036
    Result: reject a unit root at the 5% level.

Remarks
-------

This is the DF-GLS test of Elliott, Rothenberg and Stock (1996). The null
hypothesis is a unit root. For both specifications, the printed 5% decision
rejects only when the statistic is below the reported 5% critical value.
The constant-case asymptotic p-value does not control that decision.

GLS detrending uses :math:`\alpha=1+\bar c/n`, where :math:`\bar c=-7`
for ``"c"`` and :math:`\bar c=-13.5` for ``"ct"``. Deterministic terms
are a constant or a constant and *t* = 1 to *n*. The first transformed row
is unchanged; each later row subtracts *alpha* times the preceding row.
The fitted deterministic terms are removed from the original levels.
The final ADF regression on these GLS-detrended levels has no constant or
trend and uses *k* lagged differences, with *nobs* = *n* - *k* - 1.

With no exact lag supplied, the default is the Ng-Perron (2001) modified
AIC (MAIC). The default search ceiling is

.. math::

   k_{\max}=\min\left(\left\lceil12(n/100)^{1/4}\right\rceil,
   \left\lfloor n/2\right\rfloor-d-1\right),

with *d* = 1 for ``"c"`` and 2 for ``"ct"``. The input trend sets this
cap even though the final ADF has no deterministic terms. An explicit
*lags* or *max_lags* cannot exceed :math:`\lfloor n/2\rfloor-d-1`.
Ceiling rounding and this cap are library adaptations of the Schwert rule.

All criteria use GLS-detrended data on the same *m* = *n* - 1 - *kmax*
observations. Let :math:`\sigma_k^2=\mathrm{SSR}_k/m`, let *b0* be the
coefficient on the lagged detrended level, and let *yd* denote those
lagged levels on the common sample. Define
:math:`\tau(k)=b_0^2\sum yd^2/\sigma_k^2`. Then

.. math::

   \mathrm{MAIC}(k)=\ln(\sigma_k^2)+2(\tau(k)+k)/m,

   \mathrm{AIC}(k)=\ln(\sigma_k^2)+2(k+1)/m,

   \mathrm{BIC}(k)=\ln(\sigma_k^2)+\ln(m)(k+1)/m.

Exact ties choose the smaller lag. The ADF regression is refit on all
*n* - *k* - 1 usable observations after selection. Giving ``lags=k``
skips selection and sets the returned *ic* to ``"none"``. The criterion
is printed only after automatic selection.

For ``"c"``, critical values and the p-value follow the Dickey-Fuller
no-constant distribution, as the original authors prescribe. This is
asymptotically correct. In small samples the test rejects somewhat more
often than the nominal level. Critical values use the MacKinnon (2010)
finite-sample adjustment for that Dickey-Fuller distribution at final
*nobs*; the p-value uses the asymptotic MacKinnon (1994) approximation.
These do not provide a separate finite-sample DF-GLS calibration, and the
asymptotic p-value can disagree with the critical-value decision near a
cutoff.

For ``"ct"``, critical values use Elliott, Rothenberg and Stock (1996),
Table 1C, at the input length *n*, not *nobs*. The table is

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Input observations
     - 1%
     - 5%
     - 10%
   * - 50
     - -3.77
     - -3.19
     - -2.89
   * - 100
     - -3.58
     - -3.03
     - -2.74
   * - 200
     - -3.46
     - -2.93
     - -2.64
   * - Infinite sample
     - -3.48
     - -2.89
     - -2.57

For *n* <= 50 use the 50 row. Interpolate linearly in *n* between 50 and
100 and between 100 and 200. For *n* > 200 use the infinite-sample row.
This interpolation is a library convention, not a fitted finite-sample
response surface; the change from 200 to 201 is deliberate. No p-value
is available for ``"ct"``: *p_value* is GAUSS missing and printed output
states that it is unavailable.

Invalid trend or lag keywords, missing or nonfinite observations, constant
or exactly or nearly linear series, and infeasible lags give an error.
Rank-deficient, saturated, or degenerate detrending or ADF regressions
also give an error. A failed search candidate stops the test.

References
----------

- Elliott, G., T.J. Rothenberg and J.H. Stock (1996). "Efficient tests for an autoregressive unit root." *Econometrica*, 64(4), 813-836, pp. 824-825 and Table 1C.
- Ng, S. and P. Perron (2001). "Lag length selection and the construction of unit root tests with good size and power." *Econometrica*, 69(6), 1519-1554, Equation (12).
- MacKinnon, J.G. (1994). "Approximate asymptotic distribution functions for unit-root and cointegration tests." *Journal of Business & Economic Statistics*, 12(2), 167-176.
- MacKinnon, J.G. (2010). "Critical values for cointegration tests." Queen's Economics Department Working Paper No. 1227.
- Schwert, G.W. (1989). "Tests for unit roots: A Monte Carlo investigation." *Journal of Business & Economic Statistics*, 7(2), 147-159.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`adfTest`, :func:`ppTest`, :func:`kpssTest`, :func:`engleGrangerTest`, :func:`stationarityTests`
