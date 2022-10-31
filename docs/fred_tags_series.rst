
fred_tags_series
==============================================

Purpose
----------------

Get the series matching all tags in the tag_names parameter and no tags in the exclude_tag_names parameter. 


Format
----------------
.. function:: x = fred_tags_series(tag_names[, ...])

    :param tag_names: A semicolon delimited list of tag names that series match all of. required, no default value.
         Example value: 'slovenia;food'.  Filter results to series having both tags 'slovenia' and 'food'.See the related request fred/tags.

    :type tag_names: String

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no default value.
         Example value: 'alchohol;quarterly'. 
            Filter results to series having neither tag 'alchohol' nor tag 'quarterly'.

    :type exclude_tag_names: String

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'.
         optional, default: series_id

    :type order_by: One of the following strings: 'series_id'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['exclude_tag_names', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

   head(fred_tags_series());

   Program execute failed


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_tags`, :func:`fred_related_tags`

