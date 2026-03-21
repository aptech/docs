svForecastControlCreate
=======================

Purpose
-------
Create an :class:`svForecastControl` structure with default values for SV-BVAR density forecasting.

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

    fctl = svForecastControlCreate();

    // Switch to simulation mode for proper density
    fctl.mode = "simulate";
    fctl.n_paths = 500;

    // Custom quantiles for risk management
    fctl.quantile_levels = 0.01|0.05|0.50|0.95|0.99;

    // Use with bvarSvForecast
    dfc = bvarSvForecast(result, 12, fctl);

Library
-------
timeseries

Source
------
forecast.src

.. seealso:: Functions :func:`bvarSvForecast`
