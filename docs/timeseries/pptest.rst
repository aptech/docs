ppTest
======

Purpose
-------
Phillips-Perron test of the null hypothesis that a series has a unit root, with a correction for serial correlation.

Format
------

.. function:: pp = ppTest(y)
              pp = ppTest(y, trend="c", quiet=0, lags="auto")

   :param y: The series to test. A dataframe may contain one numeric column and one date-typed column, which is removed before testing. At least six finite, nonconstant observations are required. Missing values are errors; no rows are dropped.
   :type y: Nx1 vector or dataframe

   :param trend: Optional keyword, deterministic terms: ``"n"`` (none), ``"c"`` (constant), or ``"ct"`` (constant and linear trend). Accepted in any letter case. Default = ``"c"``.
   :type trend: string

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param lags: Optional keyword, Bartlett bandwidth: ``"auto"``, ``"short"``, ``"long"``, or a finite nonnegative integer smaller than *n* - 1. String rules are accepted in any letter case. Default = ``"auto"``. See Remarks for the formulas.
   :type lags: string or scalar

   :return pp: An instance of a :class:`ppResult` structure containing:

       .. list-table::
          :widths: auto

          * - pp.statistic
            - Scalar, Phillips-Perron Z(t) statistic.
          * - pp.p_value
            - Scalar, asymptotic p-value for Z(t).
          * - pp.lags
            - Scalar, Bartlett bandwidth actually used.
          * - pp.trend
            - String, canonical lowercase ``"n"``, ``"c"``, or ``"ct"``.
          * - pp.crit_values
            - 3x1 vector, finite-sample Z(t) critical values at 1%, 5%, and 10%.
          * - pp.z_alpha
            - Scalar, Phillips-Perron Z(alpha), also called Z(rho), statistic.
          * - pp.z_alpha_pvalue
            - Scalar, asymptotic p-value for Z(alpha).
          * - pp.z_alpha_crit
            - 3x1 vector, finite-sample Z(alpha) critical values at 1%, 5%, and 10%.
          * - pp.nobs
            - Scalar, regression and residual observations: *n* - 1.
          * - pp.n
            - Scalar, number of input observations after removing an optional date column.
          * - pp.test_name
            - String, ``"Phillips-Perron"``.

   :rtype pp: struct

Examples
--------

Test annual Nile flow with the default bandwidth, then with the long bandwidth rule.

::

    new;
    library timeseries;

    nile_flow = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    struct ppResult pp;
    pp = ppTest(nile_flow);
    pp = ppTest(nile_flow, lags="long");

The output:

::

    Phillips-Perron test (H0: unit root)
    ================================================================================
    Deterministic:              constant    Observations:     100 (regression uses 99)
    Bandwidth:                         3    Z(t):                             -5.654
    p-value:                     < 0.001    5% critical:                      -2.891
    Z(alpha):                    -48.815    Z(alpha) p-value:                < 0.001
    Result: reject a unit root at the 5% level (Z(t)).

    Phillips-Perron test (H0: unit root)
    ================================================================================
    Deterministic:              constant    Observations:     100 (regression uses 99)
    Bandwidth:                        11    Z(t):                             -6.310
    p-value:                     < 0.001    5% critical:                      -2.891
    Z(alpha):                    -65.704    Z(alpha) p-value:                < 0.001
    Result: reject a unit root at the 5% level (Z(t)).

Remarks
-------

The null hypothesis is a unit root. More negative Z(t) or Z(alpha) values
give stronger evidence against it. Printed decisions use the Z(t) p-value.
Z(alpha) has its own reference distribution; use its corresponding
p-value and critical values.

The level regression uses *nobs* = *n* - 1 observations and the chosen
deterministic terms. It has no lagged differences. Instead, the statistics
use the serial-correlation correction in Hamilton (1994, Section 17.6).
If *u* denotes its residuals, the long-run variance uses Bartlett weights
:math:`1-j/(L+1)` and residual products divided by *nobs*, with no
degrees-of-freedom adjustment to those products.

Here *m* = *nobs* = *n* - 1 is the residual count. The bandwidth rules are

- ``"auto"``: :math:`\max(1,\lfloor4(m/100)^{2/9}\rfloor)`.
- ``"short"``: :math:`\lfloor4(m/100)^{1/4}\rfloor`.
- ``"long"``: :math:`\lfloor12(m/100)^{1/4}\rfloor`.
- An integer sets *L* exactly, including zero, and must be smaller than *m*.

The default rule has a minimum bandwidth of one. The bandwidth controls
residual autocovariances, not the number of lagged differences.

Both p-values use asymptotic MacKinnon (1994) approximations. Z(t) critical
values use MacKinnon (2010). Z(alpha) uses a separate MacKinnon finite-sample
critical-value response surface. Both critical-value surfaces are
evaluated at *nobs*, for one series and the chosen deterministic terms.
P-values are asymptotic even though critical values depend on sample size;
they can give different decisions near a cutoff.

At least six input observations are required, or seven for ``trend="ct"``.
Invalid trend or bandwidth keywords, missing or nonfinite values, constant
data, and bandwidths at least as large as the residual sample give an error.
Degenerate residual or long-run variance and failed regressions also give
an error.

References
----------

- Phillips, P.C.B. and P. Perron (1988). "Testing for a unit root in time series regression." *Biometrika*, 75(2), 335-346.
- Hamilton, J.D. (1994). *Time Series Analysis*. Princeton University Press, Section 17.6.
- MacKinnon, J.G. (1994). "Approximate asymptotic distribution functions for unit-root and cointegration tests." *Journal of Business & Economic Statistics*, 12(2), 167-176.
- MacKinnon, J.G. (2010). "Critical values for cointegration tests." Queen's Economics Department Working Paper No. 1227.
- Newey, W.K. and K.D. West (1994). "Automatic lag selection in covariance matrix estimation." *Review of Economic Studies*, 61(4), 631-653.
- Schwert, G.W. (1989). "Tests for unit roots: A Monte Carlo investigation." *Journal of Business & Economic Statistics*, 7(2), 147-159.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`adfTest`, :func:`kpssTest`, :func:`engleGrangerTest`, :func:`dfglsTest`, :func:`stationarityTests`
