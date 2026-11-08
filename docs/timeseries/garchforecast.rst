garchForecast
=============

Purpose
-------
Forecast the conditional variance, the volatility and the mean of a fitted
GARCH or GJR-GARCH model for the periods after the last observation.

Format
------

.. function:: fc = garchForecast(result)
              fc = garchForecast(result, h)
              fc = garchForecast(result, h, x_future=X_future)

   :param result: a fit from :func:`garchFit`. It holds the data of the fit
                  (*result.y*, *result.x*, *result.dates*), so nothing else
                  about the past is needed.
   :type result: struct

   :param h: Optional, forecast horizon: the number of periods after the last
             observation. Default = 1.
   :type h: positive integer scalar

   :param x_future: Optional keyword, the regressors in each forecast period:
                    one row per period, one column per regressor of the fit,
                    in the order of *result.x_names*. The columns of a
                    dataframe are matched to the regressors by name. Required
                    when the fit has regressors; refused when it has none.
   :type x_future: hxK matrix or dataframe

   :param quiet: Optional keyword, 1 to suppress the printed table. Default =
                 0.
   :type quiet: scalar

   :param on_error: Optional keyword, ``"stop"`` ends the program when the
                    forecast is refused; ``"return"`` returns *fc* with
                    *status* and *status_message* set. Default = ``"stop"``.
   :type on_error: string

   :return fc: A :class:`garchForecastResult` structure containing:

       .. include:: include/garchforecastresult.rst

   :rtype fc: struct

Method
------

Let T be the last observation of the fit. The one-step forecast
:math:`\sigma^2_{T+1|T}` is one more step of the fitted variance recursion,
from the residuals and variances of the fit under its start-up rule. For a
GARCH(1,1),

.. math::

   \sigma^2_{T+1|T} = \omega + \alpha \varepsilon_T^2 + \beta \sigma_T^2 .

For later periods the squared shock is unknown, and its forecast is the
variance forecast itself. A GARCH(1,1) forecast therefore moves toward the
long-run variance :math:`\omega / (1 - \alpha - \beta)` by the factor
:math:`\alpha + \beta` each period:

.. math::

   \sigma^2_{T+j|T} = \omega + (\alpha + \beta)\, \sigma^2_{T+j-1|T}, \qquad j \ge 2 .

For GJR-GARCH the expected squared negative shock is half the variance
forecast, because normal and *t* errors are symmetric, so the factor is
:math:`\alpha + \gamma/2 + \beta`. Higher orders follow the same rule term
by term.

The mean forecast is :math:`\mu` plus the AR terms plus
:math:`x_{T+j}'\delta`, with earlier forecasts in place of the values of *y*
after T.

With AR terms, a shock in T+1 also moves the forecasts of T+2, T+3, ...
through the AR part. The forecast error of *y* in T+j therefore includes the
earlier shocks as well:

.. math::

   \text{Var}(y_{T+j} - \hat y_{T+j|T}) = \sum_{i=0}^{j-1} \psi_i^2 \, \sigma^2_{T+j-i|T},

where :math:`\psi_0 = 1, \psi_1, \psi_2, \ldots` are the coefficients of the
moving-average form of the AR part. *fc.variance* is
:math:`\sigma^2_{T+j|T}`, the variance of the shock, and
*fc.y_error_variance* is this sum. Without AR terms the two are equal, and the
printed table shows only *Variance*; with AR terms it shows both. The total
over the h periods, *fc.total_variance*, adds up the shock variances only:
with AR terms it is the variance of the sum of the shocks, not of the sum of
the returns.

Forecast dates
--------------

When the fit has dates, *fc.forecast_dates* continue them. Annual,
quarterly, monthly, weekly and daily dates step by their own frequency. Dates
that fall only on Monday to Friday, with mostly one-day steps, as for daily
market data, continue on the next weekdays (``fc.freq = "weekdays"``); there
is no holiday calendar. Without dates, or with dates whose frequency is not
one of these, the periods are 1 to h, *fc.freq* is empty, and they print as
T+1, T+2, ...

Warnings
--------

Two warnings are stored in *fc.warning_message*; neither changes
*fc.status*:

- The AR part of the mean is not stationary (largest modulus of the AR
  inverse roots 1 or above). The mean forecasts may not settle at a long-run
  level, and *y_error_variance* grows without bound as *h* increases. Printed
  even when *quiet* is 1.
- The persistence is within 1e-6 of 1. The variance forecasts then approach
  their long-run level very slowly and depend strongly on the estimates.
  Printed unless *quiet* is 1.

A forecast from a fit that did not converge (status 2) is computed from its
estimates, with *fc.status* = 2. With ``on_error="stop"`` a warning is
printed; with ``on_error="return"`` the message is only stored in
*fc.status_message*. A forecast whose values
overflow, for example from a nonstationary AR part at a long horizon, is
refused (status 11); it is never returned with infinite or missing values.

Examples
--------

Forecast volatility over the next 10 days
+++++++++++++++++++++++++++++++++++++++++

The GARCH(1,1) fit to the daily DM/£ returns from the :func:`garchFit`
examples:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    struct garchResult fit;
    fit = garchFit(dm, garch=1, arch=1, quiet=1);

    struct garchForecastResult fc;
    fc = garchForecast(fit, 10);
    print "Long-run variance: " fit.omega / (1 - fit.persistence);
    print "Volatility over the 10 days: " sqrt(fc.total_variance[10]);

::

    GARCH forecasts: GARCH(1,0,1), constant mean, normal errors

              Period             Mean         Variance       Volatility   Total_Variance
                 T+1    -0.0061904139       0.14699258       0.38339611       0.14699258
                 T+2    -0.0061904139       0.15174312       0.38954219       0.29873570
                 T+3    -0.0061904139       0.15629940       0.39534719       0.45503510
                 T+4    -0.0061904139       0.16066936       0.40083583       0.61570447
                 T+5    -0.0061904139       0.16486063       0.40603033       0.78056510
                 T+6    -0.0061904139       0.16888050       0.41095073       0.94944560
                 T+7    -0.0061904139       0.17273600       0.41561520        1.1221816
                 T+8    -0.0061904139       0.17643383       0.42004027        1.2986154
                 T+9    -0.0061904139       0.17998045       0.42424103        1.4785959
                T+10    -0.0061904139       0.18338204       0.42823129        1.6619779
    Long-run variance:       0.26316459
    Volatility over the 10 days:        1.2891772

The sample ends in a calm spell: tomorrow's variance, 0.147, is below the
long-run variance 0.263, and the forecasts rise toward it, closing about 4%
of the gap each day (1 - persistence = 0.041). The standard deviation of the
total return over the next 10 days is the square root of the last
*Total_Variance*, 1.29%. The DM/£ file has no dates, so the periods print as
T+1 to T+10.

Persistence close to 1
++++++++++++++++++++++

With *t* errors the DM/£ fit has persistence 1 to within 6e-8:

::

    struct garchResult fit_t;
    fit_t = garchFit(dm, garch=1, arch=1, dist="t", quiet=1);

    struct garchForecastResult fc_t;
    fc_t = garchForecast(fit_t, 5);

::

    error : garchFit: Warning: persistence is 1 (within 5.9e-08), the edge of the stationary region. Standard errors, p-values and limits assume a fit inside that region and may be unreliable.

    error : garchForecast: Warning: the persistence 0.9999999414 is within 1e-6 of 1, so the variance forecasts approach their long-run level very slowly and depend strongly on the estimates.

    GARCH forecasts: GARCH(1,0,1), constant mean, t errors

              Period             Mean         Variance       Volatility   Total_Variance
                 T+1     0.0021695146       0.13046656       0.36120156       0.13046656
                 T+2     0.0021695146       0.13319546       0.36495953       0.26366203
                 T+3     0.0021695146       0.13592436       0.36867921       0.39958639
                 T+4     0.0021695146       0.13865326       0.37236173       0.53823965
                 T+5     0.0021695146       0.14138216       0.37600819       0.67962180

Each day adds almost exactly *omega* (0.00273) to the variance forecast: with
persistence this close to 1 the forecasts keep rising nearly in a straight
line instead of levelling off within the horizon.

AR terms, regressors and dates
++++++++++++++++++++++++++++++

The monthly S&P 500 model of the :func:`garchFit` examples has an AR(1) term
and two regressors, each lagged one month. Their values for February 2026
are the January 2026 values in the shipped FRED-MD file; for March and April
this example holds them at the same values.

::

    fname = getGAUSSHome("pkgs/timeseries/examples/data/garch_sp500_monthly.csv");
    sp = loadd(fname);

    struct garchResult fit_x;
    fit_x = garchFit(sp, "y ~ x1_spread_lag1 + x2_ipgrowth_lag1", ar=1, garch=1, arch=1, quiet=1);

    // Regressors for February to April 2026: the January 2026 values in the
    // FRED-MD file, held flat for March and April.
    fm = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_md_large.csv"), "T10YFFM + INDPRO");
    n = rows(fm);
    spread = fm[n, "T10YFFM"];
    ipgrowth = 100 * (ln(fm[n, "INDPRO"]) - ln(fm[n-1, "INDPRO"]));
    x_future = ones(3, 1) .* (asmatrix(spread) ~ asmatrix(ipgrowth));

    struct garchForecastResult fc_x;
    fc_x = garchForecast(fit_x, 3, x_future=x_future);

::

    GARCH forecasts: GARCH(1,0,1), constant mean with AR(1) and 2 regressors, normal errors

              Period             Mean         Variance       Volatility   Total_Variance Y_Error_Variance
             2026M02       0.68154343        8.2448014        2.8713762        8.2448014        8.2448014
             2026M03       0.59617730        8.8846037        2.9807052        17.129405        9.2209528
             2026M04       0.57893518        9.4413965        3.0726856        26.570802        9.8175680
    Variance is the conditional variance of the shock; Y_Error_Variance adds the earlier
    shocks carried forward by the AR terms.

The data has monthly dates, so the forecasts are labeled 2026M02 to 2026M04.
In March, *Y_Error_Variance* is the March shock variance plus *ar1*\ :sup:`2`
times the February one: 8.8846 + 0.20198\ :sup:`2` × 8.2448 = 9.2210. Use
*Y_Error_Variance* for an interval around the mean forecast of the return,
and *Variance* or *Volatility* for the risk of the shock itself.
*Total_Variance* adds up the shock variances (8.2448 + 8.8846 = 17.1294 in
March), so with the AR term it is the variance of the summed shocks, not of
the summed returns.

Remarks
-------

The forecasts use the estimates as if they were the true parameters; they do
not include the uncertainty of the estimates.

EGARCH, and so EGARCH forecasts, are planned for a later release.

Refusals and Messages
---------------------

By default a refusal ends the program with its message. With
``on_error="return"``, *fc* is returned with *status* and *status_message*:

.. list-table::
   :header-rows: 1
   :widths: 8 37 55

   * - Status
     - Condition
     - Message
   * - 0
     - Forecast computed
     - (empty)
   * - 1
     - Too few observations after the AR lags
     - ``garchForecast: the fit has n observations after the AR lags;
       forecasts need at least m.``
   * - 2
     - The fit did not converge. The forecast is computed. With
       ``on_error="stop"`` the message is printed as a warning; with
       ``on_error="return"`` it is only stored in *fc.status_message*.
     - ``garchForecast: Warning: the fit did not converge, so these forecasts
       use its best finite run.``
   * - 6
     - A missing or non-finite value in *x_future*, *result.x*, *result.y* or
       the fitted parameters
     - ``garchForecast: x_future has a missing or non-finite value at row 2,
       column 2 (x2_ipgrowth_lag1).``
   * - 7
     - An invalid argument or result. The message names it, for example:
     - ``garchForecast: h must be a positive integer.``,
       ``garchForecast: the model has 2 regressors (x1_spread_lag1,
       x2_ipgrowth_lag1); give their values in each forecast period as
       x_future, a matrix with 3 rows (one per period) and 2 columns.``,
       ``garchForecast: x_future is 2x2; it needs 3 rows (one per forecast
       period) and 2 columns (x1_spread_lag1, x2_ipgrowth_lag1).``,
       ``garchForecast: x_future has no column x1_spread_lag1; its columns must
       be the regressors of the fit (x1_spread_lag1, x2_ipgrowth_lag1).``,
       ``garchForecast: the model has no regressors, so x_future is not used.
       Leave it out.``, ``garchForecast: the fit was refused (status 1), so
       there is no model to forecast from.``, ``garchForecast: result.y is
       empty. Forecasts need a result from garchFit, which stores the data of
       the fit; fit the model again.``
   * - 11
     - The parameters are outside the range forecasts need (for example after
       editing the result), or a forecast overflows
     - ``garchForecast: the fitted parameters or start-up values are outside
       the range forecasts need: omega must be positive, the ARCH, leverage and
       GARCH coefficients nonnegative, the persistence below 1, the t degrees
       of freedom above 2, and the start-up values finite.`` An overflow names
       the output, for example ``garchForecast: the variance forecast
       overflows (is not finite) within the h periods: ...``
   * - 17, 21
     - A model not offered
     - ``garchForecast: EGARCH forecasts are planned for a later release.``
   * - 5, 12, -1
     - Internal errors
     - ``garchForecast: internal error in the numerical library.`` and
       similar. Please report them to Aptech support with the data and the
       call.

References
----------

- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics* 31, 307-327.
- Box, G.E.P., G.M. Jenkins, G.C. Reinsel and G.M. Ljung (2015). *Time Series Analysis: Forecasting and Control*. 5th ed., Wiley. Section 5.1.
- Glosten, L.R., R. Jagannathan and D.E. Runkle (1993). On the relation between the expected value and the volatility of the nominal excess return on stocks. *Journal of Finance* 48, 1779-1801.

Library
-------
timeseries

Source
------
garch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchResults`, :func:`garchDiagnostics`
