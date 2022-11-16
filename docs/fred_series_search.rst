
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

    :param options: Options to pass to the API. See below. These can be set directly when calling the function
        in the form of consecutive (key, value) pairs or via a dataframe constructed with :func:`fred_set`.
        All arguments can be specified in any order. For example:

        ::

            fred_series_search("unemployment", "limit", 10, "sort_order", "desc")

        This function supports the following options:

        .. list-table::
            :widths: 20 80

            * - search_type
              - String. Determines the type of search to perform. One of the following strings: 'full_text', 'series_id'. optional, default: full_text.
                 
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

            * - realtime_start
              - YYYY-MM-DD formatted string. The start of the real-time period. For more information, see Remarks. optional, default: today's date

            * - realtime_end
              - YYYY-MM-DD formatted string. The end of the real-time period. For more information, see Remarks. optional, default: today's date

            * - limit
              - integer between 1 and 1000. The maximum number of results to return. optional, default: 1000

            * - offset
              - non-negative integer. Order results by values of the specified attribute. optional, default: 0

            * - order_by
              - String. Order results by values of the specified attribute.
            
                One of the following strings: 'search_rank', 'series_id', 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity', 'group_popularity'. optional, default: 
            
                - If the value of search_type is 'full_text' then the default value of order_by is 'search_rank'.  
                - If the value of search_type is 'series_id' then the default value of order_by is 'series_id'.

            * - sort_order
              - String. Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: If order_by is equal to 'search_rank' or 'popularity', then the default value of sort_order is 'desc'.  Otherwise, the default sort order is 'asc'.

            * - filter_variable
              - One of the following strings: 'frequency'. The attribute to filter results by. 'units', 'seasonal_adjustment'. optional, no filter by default

            * - filter_value
              - String. The value of the filter_variable attribute to filter results by. optional, no filter by default

            * - tag_names
              - String. A semicolon delimited list of tag names that series match all of. optional, no filtering by tags by default

                Example value: 'usa;m2'.  Filter results to series having both tags 'usa' and 'm2'. See the related request :func:`fred_tags`.

            * - exclude_tag_names
              - String. A semicolon delimited list of tag names that series match none of. optional, no filtering by tags by default.

                Example value: 'discontinued;m1'. Filter results to series having neither tag 'discontinued' nor tag 'm1'. Parameter *exclude_tag_names* requires that parameter tag_names also be set to limit the number of matching series.
                
    :type options: key, value pairs

    :return x: Results.
    :rtype x: Dataframe

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

