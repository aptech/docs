
fred_release_tags
==============================================

Purpose
----------------

Get the FRED tags for a release.
Optionally, filter results by tag name, tag group, or search.
Series are assigned tags and releases.
Indirectly through series, it is possible to get the tags for a release.
See the related request :func:`fred_release_related_tags`.


Format
----------------
.. function:: x = fred_release_tags(release_id[, ...])

    :param release_id: The id for a release. required

    :type release_id: integer

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param tag_names: A semicolon delimited list of tag names to only include in the response. See the related request :func:`fred_release_related_tags`. optional, no filtering by tag names by default

         Example value: 'gnp;quarterly'. This value filters results to only include tags 'gnp' and 'quarterly'.

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

    :param order_by: Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count

    :type order_by: String

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'tag_names', 'tag_group_id', 'search_text', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

    head(fred_release_tags(86));

    
              created         group_id             name            notes       popularity     series_count 
     2012-02-27 10:18              gen       commercial                .        59.000000        200.00000 
     2012-03-19 10:40              gen commercial paper                .        42.000000        200.00000 
     2012-02-27 10:18              src              frb                .        79.000000        200.00000 
     2012-02-27 10:18             geot           nation                .        99.000000        200.00000 
     2018-12-17 23:33               cc public domain: c                .        99.000000        200.00000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_releases`, :func:`fred_releases_dates`, :func:`fred_release`, :func:`fred_release_dates`, :func:`fred_release_series`, :func:`fred_release_sources`, :func:`fred_release_related_tags`

