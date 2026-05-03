etsResults
==========

Purpose
-------
Print a formatted ETS model summary.

Format
------

.. function:: etsResults(result)

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);

    etsResults(result);

Remarks
-------

The summary reports the selected ``ETS(error, trend, season)`` model label,
log-likelihood, information criteria, smoothing parameters, and basic residual
diagnostics.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsFit`, :func:`autoEts`, :func:`etsCoefTable`
