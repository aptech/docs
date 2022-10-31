
fred_series_search_tags
==============================================

Purpose
----------------

Get the FRED tags for a series search.  
Optionally, filter results by tag name, tag group, or tag search.   
See the related request fred/series/search/related_tags.


Format
----------------
.. function:: x = fred_series_search_tags(series_search_text[, ...])

    :param series_search_text: The words to match against economic data series. required

    :type series_search_text: string

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param tag_names: A semicolon delimited list of tag names to only include in the response.  See the related request fred/series/search/related_tags. optional, no filtering by tag names by default
         Example value: 'm1;m2'.  This value filters results to only include tags 'm1' and 'm2'.

    :type tag_names: String

    :param tag_group_id: A tag group id to filter tags by type. optional, no filtering by tag group by default.
         
            One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'.
            
             freq = Frequency  
             gen = General or Concept   
             geo = Geography   
             geot = Geography Type  
             rls = Release
             seas = Seasonal Adjustment  
             src = Source

    :type tag_group_id: String

    :param tag_search_text: The words to find matching tags with. optional, no filtering by search words by default.

    :type tag_search_text: String

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'popularity', 'created', 'name', 'group_id'.
         optional, default: series_count

    :type order_by: One of the following strings: 'series_count'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'tag_search_text', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

   head(fred_series_search_tags());

   Program execute failed


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

