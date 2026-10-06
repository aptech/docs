kpssTest
========

Purpose
-------
Kwiatkowski-Phillips-Schmidt-Shin test of the null hypothesis that a series is stationary around a constant or a linear trend.

Format
------

.. function:: kp = kpssTest(y)
              kp = kpssTest(y, trend="c", quiet=0, lags="auto")

   :param y: The series to test. A dataframe may contain one numeric column and one date-typed column, which is removed before testing. At least six finite, nonconstant observations are required. Missing values are errors; no rows are dropped.
   :type y: Nx1 vector or dataframe

   :param trend: Optional keyword, deterministic terms: ``"c"`` (constant) or ``"ct"`` (constant and linear trend). Accepted in any letter case; ``"n"`` is not supported. Default = ``"c"``.
   :type trend: string

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param lags: Optional keyword, Bartlett bandwidth: ``"auto"`` (data-driven), ``"short"``, ``"long"``, or a finite nonnegative integer smaller than *n*. String rules are accepted in any letter case. Default = ``"auto"``. See Remarks for the formulas.
   :type lags: string or scalar

   :return kp: An instance of a :class:`kpssResult` structure containing:

       .. list-table::
          :widths: auto

          * - kp.statistic
            - Scalar, KPSS statistic. Larger values give stronger evidence against stationarity.
          * - kp.p_value
            - Scalar, approximate p-value interpolated from the asymptotic table and bounded at 0.01 and 0.10.
          * - kp.lags
            - Scalar, Bartlett bandwidth actually used.
          * - kp.trend
            - String, canonical lowercase ``"c"`` or ``"ct"``.
          * - kp.crit_values
            - 3x1 vector, asymptotic critical values at 1%, 5%, and 10%.
          * - kp.nobs
            - Scalar, observations used for detrending and residuals; equals *n*.
          * - kp.n
            - Scalar, number of input observations after removing an optional date column.
          * - kp.test_name
            - String, ``"KPSS"``.

   :rtype kp: struct

Examples
--------

Test annual Nile flow using the data-driven bandwidth, then the short rule.

::

    new;
    library timeseries;

    nile_flow = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    struct kpssResult kp;
    kp = kpssTest(nile_flow);
    kp = kpssTest(nile_flow, lags="short");

The output:

::

    KPSS test (H0: stationary)
    ================================================================================
    Deterministic:              constant    Observations:     100 (regression uses 100)
    Bandwidth:                         5    Statistic:                         0.869
    p-value:                      < 0.01    5% critical:                       0.463
    Result: reject stationarity at the 5% level.

    KPSS test (H0: stationary)
    ================================================================================
    Deterministic:              constant    Observations:     100 (regression uses 100)
    Bandwidth:                         4    Statistic:                         0.965
    p-value:                      < 0.01    5% critical:                       0.463
    Result: reject stationarity at the 5% level.

Remarks
-------

The null is level stationarity for ``"c"`` and stationarity around a linear
trend for ``"ct"``. Larger statistics support rejection. This is the
opposite null to :func:`adfTest`, :func:`ppTest`, and :func:`dfglsTest`.
Breaks or level shifts can also lead to rejection.

All *n* input observations are used, so *nobs* equals *n*. Let *e* be the
residuals after removing a mean or an OLS constant and linear trend, and
let :math:`S_t=\sum_{i=1}^t e_i`. The statistic is

.. math::

   \mathrm{KPSS} = \frac{\sum_{t=1}^n S_t^2}{n^2\widehat\omega^2},\qquad
   \widehat\omega^2 = \gamma_0+2\sum_{j=1}^L
   \left(1-\frac{j}{L+1}\right)\gamma_j,

where :math:`\gamma_j=n^{-1}\sum_{t=j+1}^n e_t e_{t-j}`. The kernel is
Bartlett. The bandwidth rules use the full residual count *n*:

- ``"auto"``: the Newey-West (1994) data-driven rule specified below.
- ``"short"``: :math:`\lfloor4(n/100)^{1/4}\rfloor`.
- ``"long"``: :math:`\lfloor12(n/100)^{1/4}\rfloor`.
- An integer sets *L* exactly, including zero, and must be smaller than *n*.

For the automatic rule, the pilot lag is :math:`q=\lfloor n^{2/9}\rfloor`.
Using the detrended residuals, compute

.. math::

   s_0=\gamma_0+2\sum_{j=1}^q\gamma_j,\qquad
   s_1=2\sum_{j=1}^q j\gamma_j,

   L=\min\left(n-1,\left\lfloor1.1447
   \left((s_1/s_0)^2\right)^{1/3}n^{1/3}\right\rfloor\right).

The pilot :math:`\lfloor n^{2/9}\rfloor` is a library convention for the
data-driven rule. The KPSS check inside :func:`autoArima` uses the short
rule, which equals ``kpssTest(y, lags="short")`` for the same series and
deterministic terms.

Critical values are asymptotic values from Kwiatkowski et al. (1992),
Table 1. P-values are linearly interpolated between its 10%, 5%, 2.5%, and
1% entries. They are not finite-sample p-values. The returned p-value is
clipped to 0.01 or 0.10 outside the table; printed output shows ``< 0.01``
or ``> 0.10`` at those ends. A stored 0.01 or 0.10 is a bound, not an exact
tail probability.

Invalid trend or bandwidth keywords, missing or nonfinite values, constant
data, and bandwidths at least as large as *n* give an error. Degenerate
detrended variance, an undefined automatic bandwidth, and nonpositive or
nonfinite long-run variance also give an error.

References
----------

- Kwiatkowski, D., P.C.B. Phillips, P. Schmidt and Y. Shin (1992). "Testing the null hypothesis of stationarity against the alternative of a unit root." *Journal of Econometrics*, 54(1-3), 159-178, Table 1.
- Newey, W.K. and K.D. West (1994). "Automatic lag selection in covariance matrix estimation." *Review of Economic Studies*, 61(4), 631-653.
- Schwert, G.W. (1989). "Tests for unit roots: A Monte Carlo investigation." *Journal of Business & Economic Statistics*, 7(2), 147-159.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`adfTest`, :func:`ppTest`, :func:`engleGrangerTest`, :func:`dfglsTest`, :func:`stationarityTests`
