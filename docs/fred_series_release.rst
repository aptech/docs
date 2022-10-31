
fred_series_release
==============================================

Purpose
----------------
Get the release for an economic data series.

Format
----------------
.. function:: x = fred_series_release(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end']

Examples
----------------

::

   head(fred_series_release("IRA"));

   
              id             link             name    press_release     realtime_end   realtime_start 
       21.000000 http://www.feder H.6 Money Stock                 1       2022-10-31       2022-10-31 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

