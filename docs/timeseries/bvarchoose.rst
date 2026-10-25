bvarChoose
==========

Purpose
-------
Mark a prior setting to be chosen by the prior search, in a call to :func:`bvarFit`, :func:`bvarPriorSelect`, :func:`bvarRollingOrigin` or :func:`bvarMacroForecast`.

Format
------

.. function:: c = bvarChoose()
              c = bvarChoose(start)

   :param start: Optional input, the value the search starts from: a positive number, or for *residual_variances* a vector with one value per series. Default = {}, the setting's own start: its value in the control structure (or, in :func:`bvarMacroForecast`, the spec) when one is passed, otherwise its default (0.2 for *overall_tightness*); for *residual_variances*, the values *residual_variance_policy* gives; for *soc_tightness* and *sur_tightness*, 1 when the value is 0 (0 means the prior is off and cannot start a search).
   :type start: scalar or Mx1 vector

   :return c: An instance of a :class:`bvarChoice` structure holding the start. Pass it as the value of the setting's keyword.
   :rtype c: struct

Examples
--------

Choose the Tightness and the Residual Variances
+++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Seven quarterly US series, 1959Q1-2008Q4 (the data of Giannone,
    // Lenza and Primiceri 2015)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    // Choose the overall tightness, starting at 0.2, and the residual
    // variances, starting at their autoregression values
    ps = bvarPriorSelect(data, p=5, overall_tightness=bvarChoose(0.2),
        residual_variances=bvarChoose());

    // Fit at the values found
    fit = bvarFit(data, ctl=ps.fit_settings);

Choose and Fit in One Call
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    // The overall tightness is chosen first, then the model is fitted at it
    fit = bvarFit(data, p=5, overall_tightness=bvarChoose());

    print "Tightness chosen: " fit.prior_search.overall_tightness;

Hold One Setting, Choose Others
+++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/glp_2015_datasw.csv"));

    // A plain number holds the lag decay at 2; the overall tightness and
    // the residual variances are chosen
    ps = bvarPriorSelect(data, p=5, lag_decay=2, overall_tightness=bvarChoose(),
        residual_variances=bvarChoose());

Remarks
-------

A prior setting given as a plain number is held at that value. Given as
``bvarChoose(x)``, it is chosen by marginal likelihood, and the search starts
at *x*; ``bvarChoose()`` starts at the setting's own value (see *start*).

The settings that can be chosen are *overall_tightness*,
*residual_variances*, *lag_decay*, *soc_tightness* and *sur_tightness* in
:func:`bvarFit` and :func:`bvarPriorSelect`. :func:`bvarRollingOrigin` and
:func:`bvarMacroForecast` choose *overall_tightness* and
*residual_variances* only. The combinations available, the search range of
each setting and what happens when nothing is marked are listed on the
:func:`bvarPriorSelect` page. A start outside its search range is refused.

A control structure (:class:`bvarControl`) or a spec
(:class:`bvarMacroForecastSpec`) holds values only. What is chosen is
marked in the call, never stored in the structure. A value in the structure
is where ``bvarChoose()`` starts.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`bvarPriorSelect`, :func:`bvarFit`, :func:`bvarRollingOrigin`, :func:`bvarMacroForecast`, :func:`bvarControlCreate`
