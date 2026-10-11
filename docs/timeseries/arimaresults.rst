arimaResults
============

Purpose
-------
Reprint the estimation summary table from a fitted ARIMA model.

Format
------

.. function:: arimaResults(result)

   :param result: an instance of an :class:`arimaResult` structure returned by
                  :func:`arimaFit` or :func:`autoArima`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv"), "value");

    // Fit with output suppressed
    result = autoArima(y, period=12, quiet=1);

    // Print results later
    call arimaResults(result);

Remarks
-------

This function prints the same summary table that :func:`arimaFit` and
:func:`autoArima` print by default. Use it to re-display results after fitting
with ``quiet=1``.

The table includes:

- Model specification and fit statistics (AIC, AICc, BIC, log-likelihood)
- "Sigma^2 (df-adj.)", the degrees-of-freedom-adjusted innovation variance
  *result.sigma2_bc* that the forecast intervals use. The maximum-likelihood
  value is in *result.sigma2*.
- "Obs. used", the number of observations that enter the likelihood, when
  differencing or missing values make it smaller than the number of rows
- For a model selected by :func:`autoArima`, the search type, the criterion
  and the number of candidate models
- Coefficient table with standard errors, t-statistics, p-values, and 95% confidence intervals.
  The constant is labelled "Mean" when the model has no differencing and
  "Drift" when it has any, ordinary or seasonal.
- A note when an AR or MA coefficient is held at the estimation limit
- Ljung-Box portmanteau test for residual autocorrelation
- Jarque-Bera normality test on residuals

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`autoArima`, :func:`arimaFit`, :func:`arimaCoefTable`
