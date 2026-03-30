arimaResults
============

Purpose
-------
Reprint the estimation summary table from a fitted ARIMA model.

Format
------

.. function:: arimaResults(result)

   :param result: an instance of an :class:`arimaResult` structure returned by :func:`arimaFit`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline.dat");
    y = loadd(fname, "passengers");

    // Fit with output suppressed
    result = arimaFit(y, season=12, quiet=1);

    // Print results later
    call arimaResults(result);

Remarks
-------

This function prints the same summary table that :func:`arimaFit` prints
by default. Use this to re-display results after fitting with ``quiet=1``.

The table includes:

- Model specification and fit statistics (AIC, AICc, BIC, log-likelihood)
- Coefficient table with standard errors, t-statistics, p-values, and 95% confidence intervals
- Ljung-Box portmanteau test for residual autocorrelation
- Jarque-Bera normality test on residuals

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaCoefTable`
