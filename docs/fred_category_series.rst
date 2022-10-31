
fred_category_series
==============================================

Purpose
----------------
Get the series in a category.

Format
----------------
.. function:: x = fred_category_series(category_id[, ...])

    :param category_id: The id for a category. required

    :type category_id: integer

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. One of the following strings: 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'. optional, default: series_id

    :type order_by: String

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :param filter_variable: The attribute to filter results by. On of the following strings: 'frequency', 'units', 'seasonal_adjustment'. optional, no filter by default

    :type filter_variable: String

    :param filter_value: The value of the filter_variable attribute to filter results by. optional, no filter by default

    :type filter_value: String

    :param tag_names: A semicolon delimited list of tag names that series match all of. optional, no filtering by tags by default

         Example value: 'income;bea'. Filter results to series having both tags 'income' and 'bea'. See the related request :func:`fred_tags`.

    :type tag_names: String

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no filtering by tags by default.

         Example value: 'discontinued;annual'. Filter results to series having neither tag 'discontinued' nor tag 'annual'.          
         Parameter *exclude_tag_names* requires that parameter tag_names also be set to limit the number of matching series.

    :type exclude_tag_names: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']

Examples
----------------

::

    head(fred_category_series(125));

    
       frequency  frequency_short group_popularity               id     last_updated            notes  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title            units      units_short 
         Monthly                M        31.000000          AITGCBN 2022-10-26 07:31 This advance est       2022-09-01       2022-09-01        3.0000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Advance U.S. Int Millions of Doll        Mil. of $ 
         Monthly                M        31.000000          AITGCBS 2022-10-26 07:31 This advance est       2022-09-01       2022-09-01        31.000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Advance U.S. Int Millions of Doll        Mil. of $ 
       Quarterly                Q        11.000000           BOPBCA 2014-06-18 08:41 This series has        2014-01-01       1960-01-01        9.0000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Balance on Curre Billions of Doll        Bil. of $ 
          Annual                A        11.000000          BOPBCAA 2014-06-18 08:41 This series has        2013-01-01       1960-01-01        3.0000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Balance on Curre Billions of Doll        Bil. of $ 
       Quarterly                Q        11.000000          BOPBCAN 2014-06-18 08:41 This series has        2014-01-01       1960-01-01        1.0000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Balance on Curre Billions of Doll        Bil. of $ 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_category`, :func:`fred_category_children`, :func:`fred_category_related`, :func:`fred_category_tags`, :func:`fred_category_related_tags`

