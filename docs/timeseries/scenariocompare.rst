scenarioCompare
===============

Purpose
-------
Compare two scenario forecasts on the same fitted model: each scenario's forecast, the model's own forecast, and the difference between the scenarios with bands.

Format
------

.. function:: sc = scenarioCompare(fit, baseline, alternative)
              sc = scenarioCompare(fit, baseline, alternative, names="Hold" $| "Cut", variable="defl" $| "gdp")

   :param fit: result from :func:`bvarFit` (posterior draws) or :func:`varFit` (coefficients fixed at their least-squares estimates).
   :type fit: struct

   :param baseline: path of the first scenario: a finite entry fixes that variable at that step, a missing value leaves it free, as for :func:`condForecast`. :func:`scenarioPath` builds one by variable name.
   :type baseline: hxm matrix

   :param alternative: path of the second scenario, the same size as *baseline*.
   :type alternative: hxm matrix

   :param names: Optional keyword, the two scenario names. Default = "Baseline" $| "Alternative".
   :type names: 2x1 string array

   :param variable: Optional keyword, the variables to print, by name or number. Default = all. Every variable is in the result either way.
   :type variable: string, string array or vector

   :param units: Optional keyword, units shown in the printed titles.
   :type units: string

   :param label: Optional keyword, title of the printed tables. Default = "Scenario comparison".
   :type label: string

   :param level: Optional keyword, central mass of each band. Default = 0.68|0.90. *levels* is accepted as another name for it.
   :type level: scalar or vector

   :param n_draws: Optional keyword, as for :func:`condForecast`.
   :type n_draws: scalar

   :param seed: Optional keyword, seed for the simulated shocks. Default = 42.
   :type seed: scalar

   :param store_draws: Optional keyword, 1 to keep every draw's difference in *sc.difference_draws*. Default = 0.
   :type store_draws: scalar

   :param xreg_future: Optional keyword, future values of the exogenous regressors. Required when the model was fit with *xreg*.
   :type xreg_future: hxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return sc: An instance of a :class:`scenarioComparison` structure containing:

       .. include:: include/scenariocomparison.rst

   :rtype sc: struct

Examples
--------

Hold the Funds Rate or Cut It
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Seven quarterly US series, 1960Q1-2019Q4; the last is the funds rate
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    fit = bvarFit(data, p=3, n_draws=2000, quiet=1);

    hold = scenarioPath(fit, 8, "ffr", 1.64);
    cut = scenarioPath(fit, 8, "ffr", 1.64 - (0.25|0.5|0.75|1|1|1|1|1));

    sc = scenarioCompare(fit, hold, cut, names="Hold" $| "Cut",
        variable="defl" $| "gdp", label="Cut minus hold");

For each variable named, the printout shows the model's own forecast with no
assumed path, each scenario's median, and the difference (cut minus hold)
with its 68% band.

Remarks
-------

**Pairing.** Both scenarios are run on the same fit, so they use the same
posterior draws in the same order. For each draw the difference is taken
between the two expected paths (the scenario effects of
:func:`condForecast`), so the bands describe uncertainty about the
coefficients and the error covariance, not simulated shocks. With fixed
coefficients (:func:`varFit`) the difference has no uncertainty, every band
equals it, and the printout says so. Medians and bands use type-7 quantiles
(linear between order statistics), as elsewhere in the library.

**What a scenario answers.** Every future shock may move to deliver an
assumed path, so each scenario is the forecast the model expects when the
conditioned variables follow that path, not the effect of deciding the path.
See :func:`condForecast`.

**No path.** The model's own forecast comes from :func:`bvarForecast` (the
median of simulated paths, from the same posterior draws and seed, with its
own simulated shocks) for a :func:`bvarFit` result, and from
:func:`varForecast` (the point forecast) for a :func:`varFit` result.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`scenarioPath`, :func:`condForecast`, :func:`bvarForecast`
