condForecast
============

Purpose
-------
Forecast a VAR or Bayesian VAR given assumed future values of some variables (a scenario forecast).

Format
------

.. function:: cfc = condForecast(fit, path)
              cfc = condForecast(fit, path, averages=avg, average_of=var)
              cfc = condForecast(fit, path, level=0.90, n_draws=5000, seed=42)

   :param fit: result from :func:`bvarFit` (one simulated path per posterior draw) or :func:`varFit` (coefficients fixed at their least-squares estimates and the residual covariance at its maximum likelihood value, divisor *T*, as in :func:`varForecast`).
   :type fit: struct

   :param path: the forecast horizon is the number of rows. A finite entry fixes that variable at that step; a missing value (see :func:`miss`) leaves it free.
   :type path: hxm matrix

   :param averages: Optional keyword, conditions on averages, one row per condition: first step, last step, value. The average of the variable over steps *first* to *last* must equal *value*.
   :type averages: Nx3 matrix

   :param average_of: Optional keyword, the variable of each *averages* row, by name or number: one for every row, or one per row.
   :type average_of: string, string array or vector

   :param level: Optional keyword, central mass of each pointwise band. Default = 0.68|0.90. *levels* is accepted as another name for it.
   :type level: scalar or vector

   :param n_draws: Optional keyword. For a :func:`bvarFit` result, the number of posterior draws to use (default and maximum: all stored draws). For a :func:`varFit` result, the number of simulated paths (default 5000).
   :type n_draws: scalar

   :param seed: Optional keyword, seed for the simulated future shocks. Default = 42.
   :type seed: scalar

   :param store_draws: Optional keyword, 1 to keep every simulated path in *cfc.draws* and every draw's scenario effect in *cfc.effect_draws*. Default = 0.
   :type store_draws: scalar

   :param xreg_future: Optional keyword, future values of the exogenous regressors. Required when the model was fit with *xreg*.
   :type xreg_future: hxK matrix

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return cfc: An instance of a :class:`condForecastResult` structure containing:

       .. include:: include/condforecastresult.rst

   :rtype cfc: struct

Examples
--------

Hold the Funds Rate for Two Years
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Seven quarterly US series, 1960Q1-2019Q4; the last is the funds rate
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    fit = bvarFit(data, p=3, n_draws=2000, quiet=1);

    // Eight quarters; only the funds rate (column 7) is fixed
    path = miss(zeros(8, 7), 0);
    path[., 7] = 1.64 * ones(8, 1);

    cfc = condForecast(fit, path);

The printout shows the median forecast of every variable and the scenario
effect: the expected path with the condition minus the expected path
without it.

Compare Two Rate Paths
++++++++++++++++++++++

Both calls below use the same posterior draws in the same order, so the
difference of their stored effects is, draw by draw, the difference between
the two expected paths:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    fit = bvarFit(data, p=3, n_draws=2000, quiet=1);

    hold = miss(zeros(8, 7), 0);
    hold[., 7] = 1.64 * ones(8, 1);
    cut = hold;
    cut[., 7] = 1.64 - (0.25|0.5|0.75|1|1|1|1|1);

    a = condForecast(fit, hold, store_draws=1, quiet=1);
    b = condForecast(fit, cut, store_draws=1, quiet=1);

    // Inflation (column 4): one row per draw, one column per quarter
    d = reshape(b.effect_draws[., 4] - a.effect_draws[., 4], a.n_draws, 8);
    print "Cut minus hold, inflation: median and 68% band";
    print quantile(d, 0.5|0.16|0.84)';

Condition on Yearly Averages
++++++++++++++++++++++++++++

A monthly model can be given a yearly assumption: here the funds rate must
average 16.38% in the first twelve months and 12.26% in the next twelve,
without fixing any single month. The coefficients are fixed at their
least-squares estimates:

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/waggoner_zha_1999_monthly.csv"));
    fit = varFit(data[1:264, .], p=13, quiet=1);

    path = miss(zeros(24, 6), 0);
    avg = { 1 12 16.38,
           13 24 12.26 };

    cfc = condForecast(fit, path, averages=avg, average_of="FFR");

Remarks
-------

**What a scenario forecast answers.** Every future shock may move to
deliver the assumed path, so the result is the forecast the model expects
when the conditioned variables follow that path. It is not the effect of
deciding the path: if, in the data, a variable rose when the economy was
strong, a high assumed path comes with a strong economy in the forecast.

**Conditions.** Fixed cells in *path* and rows of *averages* can be
combined. Every simulated path meets every condition exactly. Conditions
must not be redundant: an average together with every value it covers is
refused.

**Averages over calendar periods.** An *averages* row covers forecast steps
only. If the forecast starts part way through a year and the assumption is
for that year's average, subtract the months already observed: with *k*
months observed and an assumed yearly average *a*, the remaining
12 - *k* steps must average (12 *a* - sum of the observed months) / (12 - *k*).

**Scenario effect.** For each parameter draw the effect is the expected
path given the conditions minus the expected path without them. It does
not include simulated shocks, so with a :func:`varFit` result it is the
same for every path and its bands collapse onto it.

**Parameter uncertainty.** With a :func:`bvarFit` result each simulated
path uses its own posterior draw. The conditions do not update the
posterior: the draws are those of the fit. That suits a hypothetical
scenario, which should not change what the model believes about the
economy. When the conditioning values are information (for example data
that have since been published), Waggoner and Zha (1999) argue that they
should also update the coefficients; they do so with a Gibbs sampler
(their Algorithm 1), which this function does not use.

Model
-----

Write the future values as the forecast without shocks plus the effect of
the future structural shocks :math:`e` (orthogonalized with the Cholesky
factor of :math:`\Sigma`), :math:`y = \tilde{y} + M e`,
:math:`e \sim N(0, I)`. Each condition is one row of :math:`C y = c`, so
the shocks must satisfy :math:`R e = r` with :math:`R = C M` and
:math:`r = c - C \tilde{y}`. Given the parameters, the shocks are then
normal with mean :math:`R'(RR')^{-1} r` and variance
:math:`I - R'(RR')^{-1} R` (Waggoner and Zha 1999, Proposition 2). The
mean part, :math:`M R'(RR')^{-1} r`, is the scenario effect. The
distribution does not depend on the order of the variables (Waggoner and
Zha 1999, Proposition 1).

Algorithm
---------

For each simulated path:

1. Take the parameter draw (or the least-squares estimates).
2. Compute the forecast without shocks and the orthogonalized impulse responses.
3. Build :math:`R` and :math:`r` from the conditions; factor :math:`R` by a singular value decomposition.
4. Draw the shocks from their distribution given the conditions and propagate them through the VAR.

Quantiles are pointwise, across the simulated paths.

References
----------

- Waggoner, D.F. and T. Zha (1999). "Conditional forecasts in dynamic multivariate models." *Review of Economics and Statistics*, 81(4), 639-651.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarFit`, :func:`varFit`, :func:`bvarForecast`
