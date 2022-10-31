
fred_category_tags
==============================================

Purpose
----------------

Get the FRED tags for a category.

Optionally, filter results by tag name, tag group, or search. 

Series are assigned tags and categories.

Indirectly through series, it is possible to get the tags for a category.

No tags exist for a category that does not have series.  

See the related request :func:`fred_category_related_tags`.


Format
----------------
.. function:: x = fred_category_tags(category_id[, ...])

    :param category_id: The id for a category. required

    :type category_id: integer

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param tag_names: A semicolon delimited list of tag names to only include in the response. See the related request :func:`fred_category_related_tags`. optional, no filtering by tag names by default
         
         Example value: 'trade;goods'.  This value filters results to only include tags 'trade' and 'goods'.

    :type tag_names: String

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

    :param search_text: The words to find matching tags with. optional, no filtering by search words by default.

    :type search_text: String

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'popularity', 'created', 'name', 'group_id'. optional, default: series_count

    :type order_by: One of the following strings: 'series_count'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. optional, default: asc

    :type sort_order: One of the following strings: 'asc', 'desc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

    head(fred_category_tags(125));

    
              created         group_id             name            notes       popularity     series_count 
     2012-02-27 10:18              src              bea                .        78.000000        50.000000 
     2012-02-27 10:18             geot           nation                .        99.000000        50.000000 
     2018-12-17 23:33               cc public domain: c                .        99.000000        50.000000 
     2012-02-27 10:18              geo              usa                .        100.00000        50.000000 
     2012-02-27 10:18              gen          balance                .        48.000000        46.000000 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_category`, :func:`fred_category_children`, :func:`fred_category_related`, :func:`fred_category_series`, :func:`fred_category_related_tags`

