
fred_series_categories
==============================================

Purpose
----------------
Get the categories for an economic data series.

Format
----------------
.. function:: x = fred_series_categories(series_id[, ...])

    :param series_id: The id for a series. required

    :type series_id: string

    :param realtime_start: The start of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period. For more information, see Remarks. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end']

Examples
----------------

::

    head(fred_series_categories("EXJPUS"));

    
              id             name        parent_id 
       95.000000    Monthly Rates        15.000000 
       275.00000            Japan        158.00000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_series`, :func:`fred_series_observations`, :func:`fred_series_release`, :func:`fred_search`, :func:`fred_series_search_tags`, :func:`fred_series_search_related_tags`, :func:`fred_series_tags`, :func:`fred_series_updates`, :func:`fred_series_vintagedates`

