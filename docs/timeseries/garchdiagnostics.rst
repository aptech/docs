garchDiagnostics
================

Purpose
-------
Test the standardized residuals of a GARCH fit for remaining ARCH effects
(ARCH-LM test) and for a different response of the variance to negative and
positive shocks (sign-bias test).

Format
------

.. function:: dg = garchDiagnostics(result)
              dg = garchDiagnostics(result, lags=12)

   :param result: a fit returned by :func:`garchFit`.
   :type result: struct

   :param lags: Optional keyword, number of lagged squared residuals in the
                ARCH-LM regression. Default = 12.
   :type lags: positive integer scalar

   :param quiet: Optional keyword, 1 to suppress the printed results.
                 Default = 0.
   :type quiet: scalar

   :param on_error: Optional keyword, ``"stop"`` ends the program when the
                    tests cannot be computed; ``"return"`` returns *dg* with
                    *status* and *status_message* set. Default = ``"stop"``.
   :type on_error: string

   :return dg: A :class:`garchDiagResult` structure containing:

       .. include:: include/garchdiagresult.rst

   :rtype dg: struct

Method
------

Both tests use the standardized residuals :math:`z_t = \varepsilon_t /
\sigma_t` of the fit (*result.residuals*, without the first *ar* rows). If the
model describes the variance well, :math:`z_t^2` is unrelated to the past.

**ARCH-LM** (Engle 1982) regresses :math:`z_t^2` on a constant and
:math:`z_{t-1}^2, \ldots, z_{t-L}^2`, with *L* = *lags*. The statistic is the
number of observations in that regression times its :math:`R^2`, compared
with a chi-squared distribution with *L* degrees of freedom. A small p-value
says the fitted model leaves ARCH effects in the residuals: try a higher
order. On standardized residuals of a fitted GARCH model this chi-squared
distribution is only an approximation, and the test tends to reject less
often than its nominal level (Li and Mak 1994).

**Sign bias** (Engle and Ng 1993) regresses :math:`z_t^2` on a constant and
:math:`S^-_{t-1}`, which is 1 when :math:`z_{t-1} < 0` and 0 otherwise. The
statistic is the *t* statistic of the coefficient on :math:`S^-_{t-1}`, with a
two-sided *t* p-value. A small p-value with a positive coefficient says
negative shocks raise the next variance more than the model allows: try
``model="gjr"``.

Examples
--------

DM/£ returns: no evidence left
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    struct garchResult fit;
    fit = garchFit(dm, garch=1, arch=1, quiet=1);

    struct garchDiagResult dg;
    dg = garchDiagnostics(fit);

::

    GARCH residual diagnostics
    ARCH-LM(12): 9.77121  p-value: 0.636024
    Sign bias t: 1.54186  p-value: 0.123267

Neither test rejects at usual levels: there is no evidence of an ARCH effect
left in 12 lags, nor of an asymmetry, in line with the small *gamma1* of the
GJR fit on the :func:`garchFit` page.

Monthly S&P 500 returns: an asymmetry
+++++++++++++++++++++++++++++++++++++

::

    fname = getGAUSSHome("pkgs/timeseries/examples/data/garch_sp500_monthly.csv");
    sp = loadd(fname);

    struct garchResult fit, fit_gjr;
    struct garchDiagResult dg, dg_gjr;

    // Constant mean, GARCH(1,1)
    fit = garchFit(sp, "y ~ 1", garch=1, arch=1, quiet=1);
    dg = garchDiagnostics(fit);

    // The same mean with GJR
    fit_gjr = garchFit(sp, "y ~ 1", garch=1, arch=1, model="gjr", quiet=1);
    dg_gjr = garchDiagnostics(fit_gjr);

    print fit_gjr.parameter_table;
    print fit.loglik~fit_gjr.loglik;

::

    GARCH residual diagnostics
    ARCH-LM(12): 1.97154  p-value: 0.999448
    Sign bias t: 3.53493  p-value: 0.000431312
    GARCH residual diagnostics
    ARCH-LM(12): 1.70349  p-value: 0.999743
    Sign bias t: 2.44924  p-value: 0.0145294

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu       0.70786028                .                .                .                .                .
               omega        2.3951923                .                .                .                .                .
              alpha1    6.8707004e-08                .                .                .                .                .
              gamma1       0.28063225                .                .                .                .                .
               beta1       0.66187459                .                .                .                .                .
          -2131.8756       -2117.3669

After the GARCH(1,1) fit the sign-bias test rejects clearly (*t* = 3.53):
months after a fall are more volatile than the model predicts. The GJR fit
raises the log likelihood by 14.5 with one more parameter. Its *alpha1* is
essentially 0 and *gamma1* = 0.28: a rise in the index barely moves next
month's variance, while a fall does. With *alpha1* at its bound of 0 the usual
standard errors do not apply, so none are shown (*result.standard_error_status*
is ``"nonregular"``). The sign-bias test after the GJR fit is smaller but still
below 0.05.

Refusals and Messages
---------------------

.. list-table::
   :header-rows: 1
   :widths: 8 37 55

   * - Status
     - Condition
     - Message
   * - 1
     - Too few standardized residuals for *lags*
     - ``garchDiagnostics: 200 standardized residuals; lags=199 needs at least
       201.``
   * - 6
     - A missing or non-finite standardized residual
     - ``garchDiagnostics: standardized residual n is missing or
       non-finite.``
   * - 7
     - *lags* is not a positive integer, or the fit was refused
     - ``garchDiagnostics: lags must be a positive integer.`` or
       ``garchDiagnostics: the fit was refused (status 1), so there are no
       residuals to check.``
   * - 9
     - The squared residuals do not vary
     - ``garchDiagnostics: the auxiliary regressions could not be computed (no
       variation in the squared residuals).``
   * - 5, -1
     - Internal errors
     - ``garchDiagnostics: internal error in the numerical library.`` and
       similar. Please report them to Aptech support.

References
----------

- Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. *Econometrica* 50, 987-1007.
- Engle, R.F. and V.K. Ng (1993). Measuring and testing the impact of news on volatility. *Journal of Finance* 48, 1749-1778.
- Li, W.K. and T.K. Mak (1994). On the squared residual autocorrelations in non-linear time series with conditional heteroskedasticity. *Journal of Time Series Analysis* 15, 627-636.

Library
-------
timeseries

Source
------
garch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchResults`
