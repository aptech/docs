tvpSvFit
========

Purpose
-------
Fit a time-varying-parameter VAR with stochastic volatility.

Format
------

.. function:: result = tvpSvFit(y, p={}, quiet={}, ctl={}, n_draws=5000, n_burn=5000, seed={})

   :param y: Data with at least two model variables. A single date column is excluded from the model.
   :type y: matrix or dataframe

   :param p: Required positive integer lag order. Pass ``p=``; this is not a field of the control.
   :type p: scalar

   :param quiet: Optional keyword, scalar 0 to print or 1 to suppress printing. Default = 0. Overrides *ctl.quiet*, which must also be 0 or 1.
   :type quiet: scalar

   :param ctl: Optional keyword, a ``tvpSvControl`` from ``tvpSvControlCreate()`` or ``{}`` (omitted). Other values or structure types are refused. The control supplies settings such as *const* (0 or 1, default 1), *xreg*, thinning and prior scales. It has no lag-order field.
   :type ctl: struct

   :param n_draws: Optional keyword, number of posterior draws. Default = 5000.
   :type n_draws: scalar

   :param n_burn: Optional keyword, burn-in draws. Default = 5000.
   :type n_burn: scalar

   :param seed: Optional keyword, random seed. Default = 42; overrides the control.
   :type seed: scalar

   :return result: A ``tvpSvResult``. *b_mean* and *b_sd* summarize the terminal coefficient matrix, with equations in columns and rows ordered as constant (when present), lag 1 through lag p in variable order, then exogenous regressors. *sv_mu*, *sv_phi* and *sv_sigma2* summarize the volatility parameters. The result also retains the fitted data and a session-local handle for :func:`tvpSvForecast`.
   :rtype result: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    result = tvpSvFit(data, p=2);
    fc = tvpSvForecast(result, 8);
    print fc.median;

Remarks
-------

The forecast bands from :func:`tvpSvForecast` cover parameter uncertainty
only; they exclude future shocks. Forecast from the fitted result in the
same session.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`tvpSvForecast`, :func:`bvarSvFit`
