forecastModel
=============

Purpose
-------
Names one model for :func:`forecastEval`: a fitted VAR or BVAR whose settings are refitted at every start date, or a model specification such as ``"AR(bic)"``.

Format
------

.. function:: md = forecastModel(model)
              md = forecastModel(model, name="Minnesota BVAR")
              md = forecastModel(bvar_fit, point="posterior_mean")

   :param model: a :func:`varFit` or :func:`bvarFit` result, or a specification string accepted by :func:`forecastEval` (``"AR(bic)"``, ``"naive"``, ``"ARIMA(1,0,0)"``, ...).
   :type model: struct or string

   :param name: Optional keyword, label used in the tables. Default = the specification, ``"VAR(p)"`` or ``"BVAR(p)"`` (``"BVAR(p), posterior mean"`` with ``point="posterior_mean"``).
   :type name: string

   :param point: Optional keyword, the point forecast of a BVAR. ``"predictive"``: the mean of the predictive draws, with bands. ``"posterior_mean"``: iterated from the posterior-mean coefficients; no draws are made, so the model has no bands. Only for a :func:`bvarFit` result. Default = ``"predictive"``.
   :type point: string

   :return md: An instance of a :class:`forecastModel` structure. Join several with ``|`` to pass them to :func:`forecastEval`.
   :rtype md: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/fred_qd_medium_dated.csv"));
    y = y[., "date" "gdp" "defl" "ffr"];

    v = varFit(y, p=2, quiet=1);
    b = bvarFit(y, p=2, overall_tightness=0.2, lag1_prior_mean="zero", quiet=1);

    // Three models in one list: the VAR, the BVAR and a random walk
    models = forecastModel(v)
           | forecastModel(b, name="Minnesota BVAR")
           | forecastModel("naive", name="Random walk");

    fe = forecastEval(y, models, target="defl", train_end="2009-Q4", h=4,
        benchmark="AR(bic)", quiet=1);
    print fe.model_names;

The output is:

::

              VAR(2)
      Minnesota BVAR
         Random walk
             AR(bic)

Remarks
-------

A fitted model is a recipe. :func:`forecastEval` keeps its lag order and
constant, a VAR's trend and residual covariance choice, and a BVAR's prior
and prior settings, and re-estimates it at every start date on the data
available then; its estimates are not used. Models with
exogenous regressors (*xreg*) are not supported yet.

Each model in a list needs a different *name*.

**Point forecast of a BVAR.** By default a BVAR's forecast at each start
date is simulated: coefficients and shocks are drawn, and the mean of the
draws is scored. With ``point="posterior_mean"`` the forecast is computed
once from the posterior-mean coefficients, iterated forward, as in Banbura,
Giannone and Reichlin (2010). One month or quarter ahead the two agree
apart from simulation noise; further ahead they can differ, usually little
under a tight prior. The posterior-mean forecast needs no draws, so it is
exact, fast and usable for systems too large to simulate at every start
date, but it gives no bands. The same fit can be listed both ways to
compare them.

forecastModel
+++++++++++++

.. list-table::
   :widths: auto

   * - name
     - String, label in the tables.
   * - kind
     - String, ``"spec"``, ``"var"`` or ``"bvar"``.
   * - spec
     - String, the specification ("" for a fitted model).
   * - var_names
     - String array, the variables of a fitted model.
   * - p, const
     - Scalars, lag order and constant flag of a fitted model.
   * - trend
     - Scalar, 1 if a fitted VAR has a linear trend.
   * - resid_cov
     - String, ``"df"`` or ``"ml"``, the residual covariance choice of a fitted VAR.
   * - point
     - String, ``"predictive"`` or ``"posterior_mean"``, the point forecast of a fitted BVAR.
   * - bvar_settings
     - :class:`bvarControl` structure, the controls of a fitted BVAR.

References
----------

- Banbura, M., D. Giannone and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.

Library
-------
timeseries

Source
------
forecast_eval.src

.. seealso:: Functions :func:`forecastEval`, :func:`varFit`, :func:`bvarFit`
