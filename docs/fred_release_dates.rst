
fred_release_dates
==============================================

Purpose
----------------

Get release dates for a release of economic data.


Format
----------------
.. function:: x = fred_release_dates([...])

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: 1776-07-04 (earliest available)

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: 9999-12-31 (latest available)

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 10000

    :type limit: integer between 1 and 10000

    :param offset: Sort results is ascending or descending release date order. optional, default: 0

    :type offset: non-negative integer

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc

    :type sort_order: String

    :param include_release_dates_with_no_data: Determines whether release dates with no data available are returned. One of the following strings: 'true', 'false'. The default value 'false' excludes release dates that do not have data.
        In particular, this excludes future release dates which may be available in the FRED release calendar or the ALFRED release calendar. optional, default: false

    :type include_release_dates_with_no_data: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'sort_order', 'include_release_dates_with_no_data']

Examples
----------------

::

    head(fred_release_dates(82));

    
            date       release_id 
      1997-02-10        82.000000 
      1998-02-10        82.000000 
      1999-02-04        82.000000 
      2000-02-10        82.000000 
      2001-01-16        82.000000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_releases`, :func:`fred_releases_dates`, :func:`fred_release`, :func:`fred_release_series`, :func:`fred_release_sources`, :func:`fred_release_tags`, :func:`fred_release_related_tags`

