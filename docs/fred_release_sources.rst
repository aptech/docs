
fred_release_sources
==============================================

Purpose
----------------
Get the sources for a release of economic data.

Format
----------------
.. function:: x = fred_release_sources(release_id[, ...])

    :param release_id: The id for a release. required

    :type release_id: integer

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end']

Examples
----------------

::

   head(fred_release_sources(51));

   
              id             link             name     realtime_end   realtime_start 
       19.000000 http://www.censu U.S. Census Bure       2022-10-31       2022-10-31 
       18.000000 http://www.bea.g U.S. Bureau of E       2022-10-31       2022-10-31 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_releases`, :func:`fred_releases_dates`, :func:`fred_release`, :func:`fred_release_dates`, :func:`fred_release_series`, :func:`fred_release_tags`, :func:`fred_release_related_tags`

