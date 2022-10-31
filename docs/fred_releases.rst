
fred_releases
==============================================

Purpose
----------------
Get all releases of economic data.

Format
----------------
.. function:: x = fred_releases([, ...])

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optional, default: release_id

    :type order_by: String

    :param sort_order: Sort results in ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

    head(fred_releases());

    
              id             link             name            notes    press_release     realtime_end   realtime_start 
       9.0000000 http://www.censu Advance Monthly  The U.S. Census         1.0000000       2022-10-30       2022-10-30 
       10.000000 http://www.bls.g Consumer Price I                .        1.0000000       2022-10-30       2022-10-30 
       11.000000 http://www.bls.g Employment Cost                 .        1.0000000       2022-10-30       2022-10-30 
       13.000000 http://www.feder G.17 Industrial                 .        1.0000000       2022-10-30       2022-10-30 
       14.000000 http://www.feder G.19 Consumer Cr                .        1.0000000       2022-10-30       2022-10-30 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_releases_dates`, :func:`fred_release`, :func:`fred_release_dates`, :func:`fred_release_series`, :func:`fred_release_sources`, :func:`fred_release_tags`, :func:`fred_release_related_tags`

