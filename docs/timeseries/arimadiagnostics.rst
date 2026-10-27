arimaDiagnostics
================

Purpose
-------
Compute residual diagnostics for a fitted ARIMA model.

Format
------

.. function:: dres = arimaDiagnostics(result)

   :param result: An instance of an ``arimaResult`` structure returned by :func:`arimaFit` or :func:`autoArima`.
   :type result: struct

   :return dres: An ``arimaDiagResult`` structure containing:

       .. list-table::
          :widths: auto

          * - dres.lb_stat
            - Scalar, Ljung-Box Q statistic for residual autocorrelation.
          * - dres.lb_pval
            - Scalar, Ljung-Box p-value from a chi-square distribution on *lb_lags* - *k* degrees of freedom, where *k* is the sum of the ordinary and seasonal AR and MA orders.
          * - dres.lb_lags
            - Scalar, number of lags selected for the Ljung-Box test.
          * - dres.jb_stat
            - Scalar, Jarque-Bera statistic for residual normality.
          * - dres.jb_pval
            - Scalar, Jarque-Bera p-value from a chi-square distribution on 2 degrees of freedom.
          * - dres.acf
            - Column vector, residual autocorrelations at lags 1 through min(20, *n* - 1), where *n* is the number of nonmissing residuals. Lag zero is not included.

   :rtype dres: struct

Examples
--------

::

    new;
    library timeseries;

    nile_flow = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"), "Flow");
    result = arimaFit(nile_flow, p=1, d=1, q=1, quiet=1);

    dres = arimaDiagnostics(result);
    print dres.lb_stat dres.lb_pval dres.lb_lags;
    print dres.jb_stat dres.jb_pval;

    // Pair each residual autocorrelation with its lag
    residual_lags = seqa(1, 1, rows(dres.acf));
    print (residual_lags ~ dres.acf);

Remarks
-------

The function returns diagnostics without printing a table or plotting. It
takes only the fitted result; additional arguments are refused. To choose
the number of lags for a Ljung-Box test, use :func:`ljungBoxTest` on
*result.residuals* with *n_params* set to the ARMA order sum described below.

**Residuals used.** Diagnostics use *result.residuals*, with missing rows
removed. This excludes the start-up rows that do not contribute to the
likelihood in a differenced model. Internal missing rows are removed too:
the diagnostic lags count positions in the remaining residual vector,
not gaps in the original time index.

**Ljung-Box test.** Let *n* be the number of nonmissing residuals and
:math:`k = p + q + P + Q`, the sum of the ordinary and seasonal AR and MA
orders. Mean, drift, regressor coefficients and differencing orders do not
add to *k*. The selected lag count is

.. math::

   h = \max\{k + 3,\ \min(10,\ n - k - 1)\}.

Thus the lag count can exceed 10. The statistic is

.. math::

   Q = n(n+2)\sum_{j=1}^{h}\frac{r_j^2}{n-j},

where :math:`r_j` is the sample autocorrelation after subtracting the
residual mean. The p-value uses a chi-square distribution on :math:`h-k`
degrees of freedom. If :math:`n < h+1`, both the statistic and p-value are
missing; *dres.lb_lags* still contains the selected lag count.

**Jarque-Bera test.** With residual central moments computed using divisor
*n*, let *S* be skewness and *K* be kurtosis. The statistic is

.. math::

   JB = \frac{n}{6}\left[S^2 + \frac{(K-3)^2}{4}\right].

The p-value uses a chi-square distribution on 2 degrees of freedom. Both
outputs are missing with fewer than 4 residuals. With at least 4 residuals
and a second central moment below :math:`10^{-15}`, the function returns
*jb_stat* = 0 and *jb_pval* = 1.

**Residual ACF.** The returned autocorrelations use the same mean-adjusted
residuals as the Ljung-Box statistic:

.. math::

   r_j = \frac{\sum_{t=j+1}^{n}(e_t-\bar e)(e_{t-j}-\bar e)}
                 {\sum_{t=1}^{n}(e_t-\bar e)^2}.

The ACF and Ljung-Box calculations divide by the residual sum of squares
after centering and have no special case for a zero denominator. The
Jarque-Bera small-variance rule does not apply to them.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`autoArima`, :func:`arimaResults`, :func:`ljungBoxTest`, :func:`etsDiagnostics`
