etsDiagnostics
==============

Purpose
-------
Compute residual diagnostics for a fitted ETS model.

Format
------

.. function:: dres = etsDiagnostics(result)

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

   :return dres: An :class:`arimaDiagResult` structure with Ljung-Box, Jarque-Bera, and residual ACF fields.
   :rtype dres: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);

    dres = etsDiagnostics(result);
    print dres.lb_stat dres.lb_pval;

Remarks
-------

Use the Ljung-Box output to screen for remaining residual autocorrelation and
the Jarque-Bera output to screen for non-normal residuals.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsResults`, :func:`etsPlotResiduals`
