
fred_series_updates
==============================================

Purpose
----------------

    Get economic data series sorted by when observations were updated on the FRED® server (attribute last_updated).  
    Results are limited to series updated within the last two weeks.


Format
----------------
.. function:: x = fred_series_updates([, ...])

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. optional, default: 0

    :type offset: non-negative integer

    :param filter_value: Limit results by geographic type of economic data series; namely 'macro', 'regional', and 'all'. optional, default: 'all' meaning no filter.

        One of the values: 'macro', 'regional', 'all'
         
        - 'macro' limits results to macroeconomic data series. In general, these are series for entire countries that are not subregions of the United States.
        - 'regional' limits results to series for parts of the US; namely, series for US states, counties, and Metropolitan Statistical Areas (MSA).
        - 'all' does not filter results.

    :type filter_value: String

    :param start_time: Start time for limiting results for a time range, can filter down to minutes optional, end_time is required if start_time is set

        Example: 2018-03-02 14:20 would be 201803021420

    :type start_time: YYYYMMDDHhmm formatted string

    :param end_time: End time for limiting results for a time range, can filter down to minutes optional, start_time is required if end_time is set

        Example: 2018-03-02 2:20 would be 201803020220

    :type end_time: YYYYMMDDHhmm formatted string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'filter_value', 'start_time', 'end_time']

Examples
----------------

::

    head(fred_series_updates());

    
       frequency  frequency_short               id     last_updated            notes  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title            units      units_short 
         Monthly                M      FEDMINFRMWG 2022-10-31 14:01 The federal mini       2022-10-01       1967-01-01        30.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Federal Minimum  Dollars per Hour       $ per Hour 
         Monthly                M      FEDMINNFRWG 2022-10-31 14:01 The federal mini       2022-10-01       1938-10-01        52.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Federal Minimum  Dollars per Hour       $ per Hour 
           Daily                D          RRPTTLD 2022-10-31 13:01 This series is c       2022-10-31       2003-02-07        16.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Reverse Repurcha Billions of US D     Bil. of US $ 
           Daily                D          RRPTSYD 2022-10-31 13:01 This series is c       2022-10-31       2003-02-07        29.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Reverse Repurcha Billions of US D     Bil. of US $ 
           Daily                D        RRPONTTLD 2022-10-31 13:01 This series is c       2022-10-31       2003-02-07        59.000000       2022-10-31       2022-10-31 Not Seasonally A              NSA Overnight Revers Billions of US D     Bil. of US $ 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_categories`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_series_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_vintagedates`

