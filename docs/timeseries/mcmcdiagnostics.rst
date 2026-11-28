mcmcDiagnostics
===============

Purpose
-------
Check whether the sampler behind a stochastic-volatility BVAR has converged.

Format
------

.. function:: dx = mcmcDiagnostics(result, rhat_threshold=1.01, min_ess=400, quiet=0)

   :param result: An instance of a :class:`bvarSvResult` structure returned by :func:`bvarSvFit`, in the same GAUSS session.
   :type result: struct

   :param rhat_threshold: Optional keyword, strict upper bound on the maximum R-hat for convergence. Controls the convergence flag, warning count and printout. Default = 1.01.
   :type rhat_threshold: scalar

   :param min_ess: Optional keyword, strict lower bound on both minimum bulk and minimum tail effective sample size for convergence. Sets the ESS target for *dx.recommended_draws*. A value of 0 leaves that field empty. Default = 400.
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

The convergence flag is 1 only when the maximum R-hat is strictly below
*rhat_threshold* (default 1.01) and both the minimum bulk ESS and the
minimum tail ESS are strictly above *min_ess* (default 400). The keywords
set the native convergence flag and warning count as well as the printout.
*dx.min_tail_ess* contains the computed minimum tail ESS. A short run often
fails the sample-size checks: run more draws.

To estimate how many kept draws would reach *min_ess*, use *dx.recommended_draws*.
The projection assumes the same sampling efficiency and rounds up
:math:`n_{\mathrm{draws}}\,\mathrm{min\_ess}/\mathrm{smallest\ ESS}`,
where the denominator is the smaller of the minimum bulk and tail ESS.
The field is empty when *min_ess* is 0 or no ESS is measured.

The result must come from :func:`bvarSvFit` in the same session; a result
loaded from a file is refused and must be refit.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`mcmcDiagnosticsPrint`, :func:`bvarSvFit`, :func:`varDiagnostics`
