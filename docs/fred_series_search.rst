
fred_series_search
==============================================

Purpose
----------------


Get economic data series that match search text.



Format
----------------
.. function:: x = fred_series_search([, ...])

    :param search_text: The words to match against economic data series. 'series_id'.
         
            'full_text' searches series attributes title, units, frequency, and tags by parsing words into stems.  
            This makes it possible for searches like 'Industry' to match series containing related words such as 'Industries'.
            Of course, you can search for multiple words like 'money' and 'stock'.
            Remember to url encode spaces (e.g. 'money%20stock').
          
            'series_id' performs a substring search on series IDs.  
            Searching for 'ex' will find series containing 'ex' anywhere in a series ID.  
            '*' can be used to anchor searches and match 0 or more of any character. 
            Searching for 'ex*' will find series containing 'ex' at the beginning of a series ID.
            Searching for '*ex' will find series containing 'ex' at the end of a series ID.
            It's also possible to put an '*' in the middle of a string.  
            'm*sl' finds any series starting with 'm' and ending with 'sl'.
          optional, default: full_text.

    :type search_text: One of the following strings: 'full_text'

    :param search_type: Determines the type of search to perform. 'series_id'.
         
            'full_text' searches series attributes title, units, frequency, and tags by parsing words into stems.  
            This makes it possible for searches like 'Industry' to match series containing related words such as 'Industries'.
            Of course, you can search for multiple words like 'money' and 'stock'.
            Remember to url encode spaces (e.g. 'money%20stock').
          
            'series_id' performs a substring search on series IDs.  
            Searching for 'ex' will find series containing 'ex' anywhere in a series ID.  
            '*' can be used to anchor searches and match 0 or more of any character. 
            Searching for 'ex*' will find series containing 'ex' at the beginning of a series ID.
            Searching for '*ex' will find series containing 'ex' at the end of a series ID.
            It's also possible to put an '*' in the middle of a string.  
            'm*sl' finds any series starting with 'm' and ending with 'sl'.
          optional, default: full_text.

    :type search_type: One of the following strings: 'full_text'

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 
            One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'.
          
            optional, default: If the value of search_type is 'full_text' then the default value of order_by is 'search_rank'.  
            If the value of search_type is 'series_id' then the default value of order_by is 'series_id'.

    :type order_by: 

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: If order_by is equal to 'search_rank' or 'popularity', then the default value of sort_order is 'desc'.  Otherwise, the default sort order is 'asc'.

    :type sort_order: One of the following strings: 'asc'

    :param filter_variable: The attribute to filter results by. 'units', 'seasonal_adjustment'.
         optional, no filter by default

    :type filter_variable: On of the following strings: 'frequency'

    :param filter_value: The value of the filter_variable attribute to filter results by. optional, no filter by default

    :type filter_value: String

    :param tag_names: A semicolon delimited list of tag names that series match all of. optional, no filtering by tags by default
         Example value: 'usa;m2'.  Filter results to series having both tags 'usa' and 'm2'.See the related request fred/tags.

    :type tag_names: String

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no filtering by tags by default.
         Example value: 'discontinued;m1'. 
            Filter results to series having neither tag 'discontinued' nor tag 'm1'.
          
            Parameter exclude_tag_names requires that parameter tag_names also be set to limit the number of matching series.

    :type exclude_tag_names: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['search_text', 'search_type', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']

Examples
----------------

::

   head(fred_series_search());

   Program execute failed


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

