
fred_sources
==============================================

Purpose
----------------
Get all sources of economic data.

Format
----------------
.. function:: x = fred_sources([, ...])

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'name', 'realtime_start', 'realtime_end'.
         optional, default: source_id

    :type order_by: One of the following strings: 'source_id'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order']

Examples
----------------

::

   head(fred_sources());

   
              id             link             name     realtime_end   realtime_start 
       1.0000000 http://www.feder Board of Governo       2022-10-31       2022-10-31 
       3.0000000 https://www.phil Federal Reserve        2022-10-31       2022-10-31 
       4.0000000 http://www.stlou Federal Reserve        2022-10-31       2022-10-31 
       6.0000000 http://www.ffiec Federal Financia       2022-10-31       2022-10-31 
       11.000000 http://www.dowjo Dow Jones & Comp       2022-10-31       2022-10-31 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_source`, :func:`fred_source_releases`

