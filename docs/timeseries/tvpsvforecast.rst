tvpSvForecast
=============

Purpose
-------
Forecast from a time-varying-parameter VAR with stochastic volatility.
The bands cover parameter uncertainty only. No future shocks are simulated.

Format
------

.. function:: dfc = tvpSvForecast(result, h, mode={}, n_paths={}, seed={}, level={}, quiet=0, ctl={})

   :param result: A ``tvpSvResult`` from ``tvpSvFit`` in the current session.
   :type result: struct

   :param h: Number of forecast steps.
   :type h: scalar

   :param mode: Optional keyword, ``"mean_path"`` only. This is the default with or without a shared control. Simulation forecasts are not supported.
   :type mode: string

   :param n_paths: Optional keyword, must remain at the shared control's default of 100. Simulation path counts are not supported.
   :type n_paths: scalar

   :param seed: Optional keyword, must remain at the shared control's default of 42. This forecast does not simulate future shocks.
   :type seed: scalar

   :param level: Optional keyword, ascending central masses: 0.68, 0.90, or both. Default = ``{ 0.68, 0.90 }``. The headline interval uses *level[1]*.
   :type level: scalar or vector

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an :class:`svForecastControl` from :func:`svForecastControlCreate`. Its empty *mode* resolves to ``"mean_path"``. Keywords override the matching control fields. Leave *store_draws* at 0.
   :type ctl: struct

   *ctl* must be a ``svForecastControl`` structure or ``{}`` (omitted).
   Other values or structure types are refused.

   :return dfc: A :class:`densityForecastResult` containing:

       .. include:: include/densityforecastresult.rst

   :rtype dfc: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    fit = tvpSvFit(data, p=2);
    fctl = svForecastControlCreate();
    fc = tvpSvForecast(fit, 8, ctl=fctl);
    print fc.median;

Remarks
-------

The bands summarize the spread of the parameter-dependent forecast paths.
They exclude future shocks and are not full predictive intervals. This
limitation applies until simulation forecasts are supported.
*dfc.mean* is the arithmetic mean of those paths; *dfc.median* is their
pointwise median. They need not be equal.

The log-volatility summaries, quantile arrays and raw draws are empty for
this forecast. Use *dfc.bands* for the 68% and 90% parameter-only intervals.
An explicit ``mode="simulate"``, a nondefault *n_paths* or *seed*, or
``ctl.store_draws=1`` is refused.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`svForecastControlCreate`, :func:`bvarSvForecast`
