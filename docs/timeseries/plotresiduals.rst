plotResiduals
=============

Purpose
-------
Plot residual diagnostics: time series plot, autocorrelation function (ACF),
and histogram. Three panels per variable.

Format
------

.. function:: plotResiduals(result)

   :param result: Estimation result containing residuals.
   :type result: struct varResult

Examples
--------

VAR Residual Diagnostics
++++++++++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    rv = varFit(data, p=4, quiet=1);

    // 3 diagnostic panels per variable
    plotResiduals(rv);

Remarks
-------

**Three panels per variable:**

1. **Time plot** — residuals over time with a zero line. Look for patterns,
   structural breaks, or volatility clustering. If the residuals look random,
   the model captures the serial dependence.

2. **ACF** — autocorrelation at lags 1 through 20. The red dashed lines show
   the 95% significance bounds (:math:`\pm 1.96 / \sqrt{T}`). Spikes beyond
   these bounds indicate remaining autocorrelation that the model didn't capture.

3. **Histogram** — distribution of residuals. Should look approximately normal
   and centered at zero. Heavy tails suggest outliers or non-normality.

**Multivariate:** For models with m > 1 variables, each variable opens a
separate plot window with its own 3-panel diagnostic display.

**What to look for:**

- ACF spikes at seasonal lags (12, 24 for monthly data) → add seasonal terms
- Volatility clustering in the time plot → consider :func:`bvarSvFit`
- Skewed histogram → model may be misspecified for extreme observations

.. seealso:: Functions :func:`varFit`, :func:`varDiagnostics`
