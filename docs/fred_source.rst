
fred_source
==============================================

Purpose
----------------
Get a source of economic data.

Format
----------------
.. function:: x = fred_source(source_id[, ...])

    :param source_id: The id for a source. required

    :type source_id: integer

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

    head(fred_source(1));

    
              id             link             name     realtime_end   realtime_start 
       1.0000000 http://www.feder Board of Governo       2022-10-31       2022-10-31 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_sources`, :func:`fred_source_releases`

