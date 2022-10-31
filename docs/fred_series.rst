
fred_series
==============================================

Purpose
----------------
Get an economic data series.

Format
----------------
.. function:: x = fred_series(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end']

Examples
----------------

::

    head(fred_series("GNPCA"));

    
       frequency  frequency_short               id     last_updated            notes  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title            units      units_short 
          Annual                A            GNPCA 2022-09-29 07:45 BEA Account Code       2021-01-01       1929-01-01        16.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Real Gross Natio Billions of Chai Bil. of Chn. 201 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

