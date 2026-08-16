arimaControlCreate
==================

Purpose
-------
Create an :class:`arimaControl` structure with default values.

Format
------

.. function:: ctl = arimaControlCreate()

   :return ctl: An instance of an :class:`arimaControl` structure with the following default values:

       .. include:: include/arimacontrol.rst

   :rtype ctl: struct

Examples
--------

::

    new;
    library timeseries;

    // Create control structure with defaults
    ctl = arimaControlCreate();

    // Customize automatic search: BIC selection and ML estimation
    ctl.ic = "bic";
    ctl.method = "ml";

    // Use with autoArima
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");
    result = autoArima(y, period=12, ctl=ctl);

Remarks
-------

The search bounds, information criterion, and stepwise setting apply only to
:func:`autoArima`. Estimation, output, optimizer, and Box-Cox settings apply to
both :func:`autoArima` and :func:`arimaFit`. The *include* overrides apply only
to :func:`arimaFit`; :func:`autoArima` requires ``ctl.include = "auto"``.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`autoArima`, :func:`arimaFit`
