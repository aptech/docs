tvpSvForecast
=============

Purpose
-------
Generate density forecasts from a fitted TVP-SV-VAR model with time-varying volatility propagation.

Format
------

.. function:: dfc = tvpSvForecast(result, h)
              dfc = tvpSvForecast(result, h, level)
              dfc = tvpSvForecast(result, h, fctl)

   :param result: an instance of a :class:`tvpSvResult` structure returned by :func:`tvpSvFit`.
   :type result: struct

   :param h: forecast horizon (number of steps ahead).
   :type h: scalar

   :param level: Optional input, credible band level (e.g., 0.90 or 0.95). Default = 0.95. Ignored when *fctl* is provided.
   :type level: scalar

   :param fctl: Optional input, an instance of an :class:`svForecastControl` structure. An instance is initialized by calling :func:`svForecastControlCreate` and the following members can be set:

       .. include:: include/svforecastcontrol.rst

   :type fctl: struct

   :return dfc: An instance of a :class:`densityForecastResult` structure containing:

       .. include:: include/densityforecastresult.rst

   :rtype dfc: struct

Examples
--------

Basic Forecast
++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = tvpSvFit(y, 2, 5000, 5000);

    // 12-step-ahead density forecast
    dfc = tvpSvForecast(result, 12);

    print "Median forecast:";
    print dfc.fc_median;

The printed output shows median forecasts with 68% and 90% credible bands:

::

    ================================================================================
    TVP-SV Density Forecast: 12 steps
    Draws: 5000
    ================================================================================

    gdp_growth
      h     Median     [16%     84%]     [5%      95%]
    ------------------------------------------------------------
      1      2.145     1.203    3.087     0.541    3.749
      2      2.038     0.892    3.184     0.134    3.942
        ...

Custom Credible Level
+++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = tvpSvFit(y);

    // 80% credible bands
    dfc = tvpSvForecast(result, 8, 0.80);

    // Access bands
    print "80% lower:";
    print dfc.bands[1].lower;
    print "80% upper:";
    print dfc.bands[1].upper;

Remarks
-------

**Forecast with time-varying parameters:**
Unlike constant-parameter BVAR forecasts, the TVP-SV-VAR forecast uses the terminal
(last-period) parameter estimates :math:`B_T` and :math:`U_T` from each posterior
draw. This means the forecast reflects the most recent structural relationships
in the data, which is critical for policy analysis during regime changes.

**Credible bands:**
The forecast returns 68% and 90% credible bands by default, computed as pointwise
quantiles across posterior draws. When a scalar *level* is provided instead of
*fctl*, it replaces the outer band level (the 68% inner band is always included).

**Point forecasts:**
The median forecast (*dfc.fc_median*) is generally preferred over the mean forecast
(*dfc.fc_mean*) for asymmetric predictive distributions, which are common with
stochastic volatility. Both are computed across posterior draws.

**Volatility propagation:**
The log-volatility :math:`h_{i,t}` is propagated forward using the estimated AR(1)
dynamics:

.. math::

   h_{i,T+s} = \mu_i + \phi_i (h_{i,T+s-1} - \mu_i) + \sigma_i \eta_{i,T+s}

When persistence :math:`\phi_i` is near 1, volatility shocks at the forecast origin
decay slowly, producing wider forecast bands at longer horizons.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`tvpSvFit`, :func:`svForecastControlCreate`, :func:`bvarSvForecast`, :func:`bvarForecast`
