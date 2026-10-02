irfPlotData
===========

Purpose
-------
Return impulse responses as a long-format dataframe for plotting or export.

Format
------

.. function:: df = irfPlotData(irf)
              df = irfPlotData(irf, shock, response)

   :param irf: an instance of an :class:`irfResult` structure from :func:`irfCompute`.
   :type irf: struct

   :param shock: Optional, shock name or number. Give *shock* and *response* together to get one response path.
   :type shock: string or scalar

   :param response: Optional, response variable name or number.
   :type response: string or scalar

   :return df: Dataframe. For all pairs: columns horizon, shock, response, value. For one pair: columns horizon, value. *value* is the point response or the posterior median. For posterior results, lower and upper band columns follow for each level, for example lower_68, upper_68, lower_90, upper_90.
   :rtype df: dataframe

Examples
--------

One response with its bands
+++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = bvarFit(y, p=4, quiet=1);
    irf = irfCompute(fit, 20, quiet=1);

    // GDP growth response to the funds rate shock
    df = irfPlotData(irf, "fed_funds", "gdp_growth");
    plotXY(df[., "horizon"], df[., "value" "lower_68" "upper_68"]);

All pairs
+++++++++

::

    df = irfPlotData(irf);
    print df[1:10, .];

Remarks
-------

In the all-pairs form, *shock* and *response* are numbers; the names are in
*irf.shock_names* and *irf.var_names*. Under sign identification only the
restricted shocks are included.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`plotIrf`
