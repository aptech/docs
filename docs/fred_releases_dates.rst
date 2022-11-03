
fred_releases_dates
==============================================

Purpose
----------------

Get release dates for all releases of economic data.


Format
----------------
.. function:: x = fred_releases_dates([...])

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: First day of the current year

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: 9999-12-31 (latest available)

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. One of the following strings: 'release_date', 'release_id', 'release_name'. optional, default: release_date

    :type order_by: String

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :param include_release_dates_with_no_data: Determines whether release dates with no data available are returned. The defalut value 'false' excludes release dates that do not have data. In particular, this excludes future release dates which may be available in the FRED release calendar or the ALFRED release calendar. One of the following strings: 'true', 'false'. optional, default: false

    :type include_release_dates_with_no_data: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'include_release_dates_with_no_data']

Examples
----------------

::

    head(fred_releases_dates());

    
            date       release_id     release_name 
      2022-10-31        488.00000 Brave-Butters-Ke 
      2022-10-31        86.000000 Commercial Paper 
      2022-10-31        72.000000 Daily Treasury I 
      2022-10-31        279.00000 Economic Policy  
      2022-10-31        378.00000 Federal Funds Da 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_releases`, :func:`fred_release`, :func:`fred_release_dates`, :func:`fred_release_series`, :func:`fred_release_sources`, :func:`fred_release_tags`, :func:`fred_release_related_tags`

