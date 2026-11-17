svForecastControlCreate
=======================

Purpose
-------
Create an :class:`svForecastControl` structure with default values for SV-BVAR and TVP-SV forecasting. The empty mode uses each function's default: ``"simulate"`` for :func:`bvarSvForecast`, ``"mean_path"`` for
:func:`tvpSvForecast`.

Format
------

.. function:: ctl = svForecastControlCreate()

   :return ctl: An instance of an :class:`svForecastControl` structure with the following default values:

       .. include:: include/svforecastcontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    result = bvarSvFit(data, p=1, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    struct svForecastControl fctl;
    fctl = svForecastControlCreate();
    // Empty mode resolves to simulate; request a 90% central band.
    fctl.level = 0.90;
    dfc = bvarSvForecast(result, 12, ctl=fctl);

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarSvForecast`, :func:`tvpSvForecast`
