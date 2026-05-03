etsCoefTable
============

Purpose
-------
Return fitted ETS smoothing parameters and summary fields as a dataframe.

Format
------

.. function:: df = etsCoefTable(result)

   :param result: An instance of an :class:`etsResult` structure returned by :func:`etsFit` or :func:`autoEts`.
   :type result: struct

   :return df: Dataframe with ``Parameter`` and ``Value`` columns.
   :rtype df: dataframe

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    result = autoEts(y);

    df = etsCoefTable(result);
    print df;

Remarks
-------

The table includes ``alpha`` and any fitted ``beta``, ``gamma``, and ``phi``
parameters, followed by ``sigma2`` and ``AICc``.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`etsResults`, :func:`etsFit`, :func:`autoEts`
