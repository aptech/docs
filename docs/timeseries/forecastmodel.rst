forecastModel
=============

Purpose
-------
Names one model for :func:`forecastEval`: a fitted VAR, BVAR or VECM whose settings are refitted at every start date, or a model specification such as ``"AR(bic)"``.

Format
------

.. function:: md = forecastModel(model)
              md = forecastModel(model, name="Minnesota BVAR")
              md = forecastModel(bvar_fit, point="posterior_mean")
              md = forecastModel(vecm_fit, rank=0)

   :param model: a :func:`varFit`, :func:`bvarFit` or :func:`vecmFit` result, or a specification string accepted by :func:`forecastEval` (``"AR(bic)"``, ``"naive"``, ``"ARIMA(1,0,0)"``, ...).
   :type model: struct or string

   :param name: Optional keyword, label used in the tables. Default = the specification, ``"VAR(p)"``, ``"BVAR(p)"`` (``"BVAR(p), posterior mean"`` with ``point="posterior_mean"``), ``"VECM(p), rank r"``, ``"VAR in differences (rank 0, p=p)"`` or ``"VAR in levels (rank M, p=p)"``. Here *p* is the levels lag order and *r* is the cointegration rank.
   :type name: string

   :param point: Optional keyword, the point forecast of a BVAR. ``"predictive"``: the mean of the predictive draws, with bands. ``"posterior_mean"``: iterated from the posterior-mean coefficients; no draws are made, so the model has no bands. Only for a :func:`bvarFit` result. Default = ``"predictive"``.
   :type point: string

   :param rank: Optional keyword for a :func:`vecmFit` result. ``{}`` keeps the fitted rank. An explicit rank must be a whole number from 0 to M, where M is the number of variables. ``rank=0`` fits a VAR in differences, with forecasts cumulated to levels. Default = ``{}``.
   :type rank: scalar

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
user regressors (*xreg* or ``ctl.xreg``) are not supported yet.

**VECM models.** Pass the :func:`vecmFit` result, including a result with
seasonal dummies. A :func:`vecmToVar` result cannot be refitted as a VECM
because it does not retain the rank, deterministic case and seasonal frequency.
The VECM descriptor stores those settings, the lag order *p* in levels and the
variable names. Its coefficients and residual covariance are re-estimated at
every start date; its rank is held fixed and rank selection is not repeated.
Fits with user regressors in ``ctl.xreg``, unfitted results and
``point="posterior_mean"`` are refused.

With ``rank=0``, the model has no error-correction term. Johansen (1995),
chapter 5, gives these remaining terms in the equation for differences:
Cases I and II, none; Cases III and IV, a constant; Case V, a constant and
linear trend. Seasonal dummies are included when fitted. The default name is
``"VAR in differences (rank 0, p=p)"``, with the fitted lag order substituted
for the last *p*. Forecasts and bands are in levels. For ranks 1 through M-1 the default
name is ``"VECM(p), rank r"``.

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
     - String, ``"spec"``, ``"var"``, ``"bvar"`` or ``"vecm"``.
   * - spec
     - String, the specification ("" for a fitted model).
   * - var_names
     - String array, the variables of a fitted model.
   * - p, const
     - Scalars, lag order in levels and constant flag of a fitted model.
   * - rank
     - Scalar, VECM rank held fixed at every start date; 0 gives a VAR in differences.
   * - det_case
     - Scalar, VECM Johansen deterministic case (1 to 5).
   * - season
     - Scalar, VECM seasonal frequency (0 for none; otherwise at least 2).
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

- Johansen, S. (1995). *Likelihood-Based Inference in Cointegrated Vector Autoregressive Models*, chapter 5.
- Banbura, M., D. Giannone and L. Reichlin (2010). "Large Bayesian vector auto regressions." *Journal of Applied Econometrics*, 25(1), 71-92.

Library
-------
timeseries

Source
------
forecast_eval.src

.. seealso:: Functions :func:`forecastEval`, :func:`varFit`, :func:`bvarFit`, :func:`vecmFit`

An explicit ``rank=M`` is accepted, just as ``rank={}`` retains a fitted full
rank. This model is a VAR in levels and its default name says so. It should
not be described as a cointegrated model. TSMT offers no adjusted test
for a VECM against rank zero: its added regressor is I(1) under the null.
The derivation of :func:`cwTest` in Clark and West (RWP 05-05, section 3)
assumes stationary predictors; it applies to nested stationary models,
such as a VAR against a smaller VAR. See their `working paper
<https://www.kansascityfed.org/documents/5368/pdf-RWP05-05.pdf>`_.
