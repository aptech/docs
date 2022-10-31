
fred_series_vintagedates
==============================================

Purpose
----------------

Get the dates in history when a series' data values were revised or new data values were released.
Vintage dates are the release dates for a series excluding release dates when the data for the series did not change.


Format
----------------
.. function:: x = fred_series_vintagedates(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: 1776-07-04 (earliest available)

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: 9999-12-31 (latest available)

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 10000

    :type limit: integer between 1 and 10000

    :param offset: Sort results is ascending or descending vintage_date order. optional, default: 0

    :type offset: non-negative integer

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order']

Examples
----------------

::

    head(fred_series_vintagedates("GNPCA"));

    
     vintage_dates_1 
          1958-12-21 
          1959-02-19 
          1959-07-19 
          1960-02-16 
          1960-07-22 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`

