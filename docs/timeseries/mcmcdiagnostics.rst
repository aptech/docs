mcmcDiagnostics
===============

Purpose
-------
Check whether the sampler behind a stochastic-volatility BVAR has converged.

Format
------

.. function:: dx = mcmcDiagnostics(result)
              dx = mcmcDiagnostics(result, rhat_threshold=1.01, min_ess=1000)

   :param result: An instance of a :class:`bvarSvResult` structure returned by :func:`bvarSvFit`, in the same GAUSS session.
   :type result: struct

   :param rhat_threshold: Optional keyword, largest R-hat shown as PASS in the printout. Default = 1.05.
   :type rhat_threshold: scalar

   :param min_ess: Optional keyword, smallest bulk effective sample size shown as PASS in the printout. Default = 400.
   :type min_ess: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return dx: An instance of an :class:`mcmcDiagResult` structure containing:

       .. include:: include/mcmcdiagresult.rst

   :rtype dx: struct

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = data[., "gdp_growth" "inflation" "fed_funds"];

    result = bvarSvFit(y, p=2, n_draws=2000, quiet=1);
    dx = mcmcDiagnostics(result);

Remarks
-------

The checks use split R-hat and bulk effective sample size of the VAR
coefficients and R-hat of the volatility parameters. *rhat_threshold* and
*min_ess* only set the PASS/FAIL labels of the printout; *dx.converged*
comes from the library's own thresholds (R-hat below 1.05 and bulk effective
sample size above 400). A short run often fails the sample-size check: run
more draws.

The result must come from :func:`bvarSvFit` in the same session; a result
loaded from a file is refused and must be refit.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`mcmcDiagnosticsPrint`, :func:`bvarSvFit`, :func:`varDiagnostics`
