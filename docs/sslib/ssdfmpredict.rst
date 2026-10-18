ssDFMPredict
==============================================

Purpose
----------------

Forecasts every series of a fitted dynamic factor model, and its factors, for the months after the sample, with standard errors.

.. note::
   **New in sslib 2.1.0; GAUSS 26.1.4+.** *horizon* is a keyword argument. The result needs no preceding ``struct ssDFMForecast`` declaration.

Format
----------------
.. function:: fOut = ssDFMPredict(dOut [, horizon])

    :param dOut: An instance of an :class:`ssDFMOut` structure returned by :func:`ssDFM`.
    :type dOut: Struct

    :param horizon: Optional keyword, the number of months to forecast. Default 12.
    :type horizon: Scalar

    :return fOut: An instance of an :class:`ssDFMForecast` structure:

        .. csv-table::
            :widths: auto

            "fOut.period", "horizon x 1, the months forecast: nobs+1 to nobs+horizon."
            "fOut.is_quarter_end", "horizon x 1, 1 in quarter-end months."
            "fOut.forecast", "horizon x k forecasts in original units. A quarterly column is the 1-2-3-2-1 aggregate; read it at quarter ends."
            "fOut.forecast_se", "horizon x k standard errors."
            "fOut.factors", "horizon x factors, factor forecasts in *dOut*'s rotation."
            "fOut.factors_se", "horizon x factors, their standard errors."

    :rtype fOut: Struct

Examples
----------------

See :func:`ssDFM`, whose example nowcasts the last quarter from *dOut.fitted* and forecasts the next two quarters with :func:`ssDFMPredict`.

Remarks
-------

The forecasts start from the smoothed state in the last month, which already uses every observation. A quarter in progress at the end of the sample therefore combines its months already observed with the forecast of the rest. Nowcasts of months inside the sample with missing data -- the ragged edge -- are in *dOut.fitted*, not here.

Standard errors condition on the estimated parameters.

Source
------

ssdfm.src

.. seealso:: Functions :func:`ssDFM`
