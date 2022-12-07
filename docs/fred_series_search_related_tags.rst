
fred_series_search_related_tags
==============================================

Purpose
----------------

Get the related FRED tags for one or more FRED tags matching a series search. Optionally, filter results by tag group or tag search. 

FRED tags are attributes assigned to series. For this request, related FRED tags are the tags assigned to series that match all tags 
in the tag_names parameter, no tags in the *exclude_tag_names* parameter, and the search words set by the *series_search_text* parameter. 
See the related request :func:`fred_series_search_tags`.

Format
----------------
.. function:: x = fred_series_search_related_tags(series_search_text, tag_names[, ...])

    :param series_search_text: The words to match against economic data series. required

    :type series_search_text: string

    :param tag_names: A semicolon delimited list of tag names that series match all of. See the related request :func:`fred_series_search_tags`. required, no default value.

         Example value: '30-year;frb'. Find the related tags for series having both tags '30-year' and 'frb'.

    :type tag_names: String

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no default value.

         Example value: 'discontinued;monthly'. Find the related tags for series having neither tag 'discontinued' nor tag 'monthly'.

    :type exclude_tag_names: String

    :param tag_group_id: A tag group id to filter tags by type. optional, no filtering by tag group by default.
         
        One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'.
       
        - freq = Frequency  
        - gen = General or Concept   
        - geo = Geography   
        - geot = Geography Type  
        - rls = Release
        - seas = Seasonal Adjustment  
        - src = Source

    :type tag_group_id: String

    :param tag_search_text: The words to find matching tags with. optional, no filtering by search words by default.

    :type tag_search_text: String

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count

    :type order_by: String

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'exclude_tag_names', 'tag_group_id', 'tag_search_text', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

    head(fred_series_search_related_tags("mortgage rate", "30-year;frb"));

    
              created         group_id             name            notes       popularity     series_count 
     2012-02-27 10:18              gen     conventional                .        26.000000        2.0000000 
     2012-02-27 10:18              gen     discontinued                .        65.000000        2.0000000 
     2012-08-16 15:21              rls              h15                .        58.000000        2.0000000 
     2012-02-27 10:18              gen         interest                .        73.000000        2.0000000 
     2012-05-29 10:14              gen    interest rate                .        72.000000        2.0000000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_search`, :func:`fred_series_search_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

