
fred_source_releases
==============================================

Purpose
----------------
Get the releases for a source.

Format
----------------
.. function:: x = fred_source_releases(source_id[, ...])

    :param source_id: The id for a source. required

    :type source_id: integer

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'name', 'press_release', 'realtime_start', 'realtime_end'.
         optional, default: release_id

    :type order_by: One of the following strings: 'release_id'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

   head(fred_source_releases(1));

   
              id             link             name    press_release     realtime_end   realtime_start 
       13.000000 http://www.feder G.17 Industrial         1.0000000       2022-10-28       2022-10-28 
       14.000000 http://www.feder G.19 Consumer Cr        1.0000000       2022-10-28       2022-10-28 
       15.000000 http://www.feder G.5 Foreign Exch        1.0000000       2022-10-28       2022-10-28 
       17.000000 http://www.feder H.10 Foreign Exc        1.0000000       2022-10-28       2022-10-28 
       18.000000 http://www.feder H.15 Selected In        1.0000000       2022-10-28       2022-10-28 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_sources`, :func:`fred_source`

