
fred_series_tags
==============================================

Purpose
----------------

Get the FRED tags for a series.  


Format
----------------
.. function:: x = fred_series_tags(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param order_by: Order results by values of the specified attribute. 'popularity', 'created', 'name', 'group_id'.
         optional, default: series_count

    :type order_by: One of the following strings: 'series_count'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'order_by', 'sort_order']

Examples
----------------

::

   head(fred_series_tags("STLFSI"));

   
         created         group_id             name            notes       popularity     series_count 
2012-02-27 10:18             seas              nsa                .        100.00000        724700.00 
2012-02-27 10:18              geo              usa                .        100.00000        653528.00 
2012-02-27 10:18             geot           nation                .        99.000000        261790.00 
2018-12-17 23:33               cc copyrighted: cit                .        88.000000        206582.00 
2012-02-27 10:18              src          frb stl                .        67.000000        78038.000 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

