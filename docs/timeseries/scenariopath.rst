scenarioPath
============

Purpose
-------
Build a scenario path for :func:`condForecast` or :func:`scenarioCompare`: one variable set to assumed values, every other cell free.

Format
------

.. function:: path = scenarioPath(fit, h, variable, values)

   :param fit: result from :func:`bvarFit` or :func:`varFit` (gives the variables).
   :type fit: struct

   :param h: forecast horizon, the number of rows of the path.
   :type h: scalar

   :param variable: the variable, by name or number.
   :type variable: string or scalar

   :param values: the assumed values: one value for every step, or one per step. A missing value (see :func:`miss`) leaves that step free.
   :type values: scalar or hx1 vector

   :return path: the path: the variable's column holds *values*, every other cell is missing (free).
   :rtype path: hxm matrix

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    fit = bvarFit(data, p=3, n_draws=2000, quiet=1);

    // Funds rate held at 1.64% for eight quarters
    hold = scenarioPath(fit, 8, "ffr", 1.64);

    // Cut by a quarter point a quarter through the first year, then held
    cut = scenarioPath(fit, 8, "ffr", 1.64 - (0.25|0.5|0.75|1|1|1|1|1));

    cfc = condForecast(fit, cut);

Classical VAR
+++++++++++++

::

    struct varResult fit_var;
    fit_var = varFit(data, p=3, trend=1, resid_cov="df", quiet=1);
    hold_var = scenarioPath(fit_var, 8, "ffr", 1.64);
    cfc_var = condForecast(fit_var, hold_var);

Remarks
-------

A :func:`vecmToVar` result is refused. This function only builds the
condition matrix; it does not compute forecasts or use a covariance.
When the path is passed to :func:`condForecast` or :func:`scenarioCompare`,
the VAR branch uses *fit.sigma* and continues the fitted trend
automatically. *xreg_future* then contains only the user's regressors.

To fix more than one variable, build the path for one and set the other
column directly, for example ``path[., 2] = values2;``.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`scenarioCompare`, :func:`condForecast`
