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

The default inverse-gamma priors for the drift variances have shape 6
and base scale 0.01. For coefficient drift, the sampler divides each
equation's OLS residual variance (floored at 0.01) by its usable sample
size. It limits this multiplier to the interval [0.000001, 10] and applies
it to *q_b_scale*. For drift in the contemporaneous relationships, the
sampler uses *q_u_scale* directly.

These defaults assume data in percent or growth-rate units. For series
in levels, use smaller drift scales, especially when large lagged values
can turn a small coefficient change into a large change in the fitted
series. Set *q_b_scale* and *q_u_scale* in the control returned by
:func:`tvpSvControlCreate`.

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
