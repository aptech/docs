
fred_series_search
==============================================

Purpose
----------------

Get economic data series that match search text.


Format
----------------
.. function:: x = fred_series_search(search_text[, ...])

    :param search_text: The words to match against economic data series. required.

    :type search_text: String

    :param search_type: Determines the type of search to perform. One of the following strings: 'full_text', 'series_id'. optional, default: full_text.
         
          - 'full_text' searches series attributes title, units, frequency, and tags by parsing words into stems.  
            This makes it possible for searches like 'Industry' to match series containing related words such as 'Industries'.
            Of course, you can search for multiple words like 'money' and 'stock'.
            Text will be url encoded automatically.

          - 'series_id' performs a substring search on series IDs.  
            Searching for 'ex' will find series containing 'ex' anywhere in a series ID.  
            '\*' can be used to anchor searches and match 0 or more of any character. 
            Searching for 'ex\*' will find series containing 'ex' at the beginning of a series ID.
            Searching for '\*ex' will find series containing 'ex' at the end of a series ID.
            It's also possible to put an '\*' in the middle of a string.  
            'm\*sl' finds any series starting with 'm' and ending with 'sl'.
          

    :type search_type: String

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute.
    
       One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'. optional, default: 
    
       - If the value of search_type is 'full_text' then the default value of order_by is 'search_rank'.  
       - If the value of search_type is 'series_id' then the default value of order_by is 'series_id'.

    :type order_by: String

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: If order_by is equal to 'search_rank' or 'popularity', then the default value of sort_order is 'desc'.  Otherwise, the default sort order is 'asc'.

    :type sort_order: String

    :param filter_variable: The attribute to filter results by. 'units', 'seasonal_adjustment'. optional, no filter by default

    :type filter_variable: On of the following strings: 'frequency'

    :param filter_value: The value of the filter_variable attribute to filter results by. optional, no filter by default

    :type filter_value: String

    :param tag_names: A semicolon delimited list of tag names that series match all of. optional, no filtering by tags by default

         Example value: 'usa;m2'.  Filter results to series having both tags 'usa' and 'm2'. See the related request :func:`fred_tags`.

    :type tag_names: String

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no filtering by tags by default.

         Example value: 'discontinued;m1'. Filter results to series having neither tag 'discontinued' nor tag 'm1'. Parameter *exclude_tag_names* requires that parameter tag_names also be set to limit the number of matching series.

    :type exclude_tag_names: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['search_text', 'search_type', 'realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']

Examples
----------------

::

    fred_series_search("monetary service index");

::
    
       frequency  frequency_short group_popularity               id     last_updated            notes  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title            units      units_short 
         Monthly                M        22.000000            MSIM2 2014-01-17 07:16 The MSI measure        2013-12-01       1967-01-01        22.000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Monetary Service Billions of Doll        Bil. of $ 
         Monthly                M        18.000000          MSIMZMP 2014-01-17 07:16 The MSI measure        2013-12-01       1967-01-01        18.000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Monetary Service Billions of Doll        Bil. of $ 
         Monthly                M        14.000000            OCM2P 2014-01-17 07:16 Preferred benchm       2013-12-01       1967-01-01        14.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Real User Cost I          Percent                % 
         Monthly                M        13.000000          MSIALLP 2014-01-17 07:16 The MSI measure        2013-12-01       1967-01-01        13.000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Monetary Service Billions of Doll        Bil. of $ 
         Monthly                M        10.000000           MSIM2A 2014-01-17 07:16 The MSI measure        2013-12-01       1967-01-01        10.000000       2022-10-31       2022-10-31 Seasonally Adjus               SA Monetary Service Billions of Doll        Bil. of $ 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_load`, :func:`fred_set`

