
fred_release_series
==============================================

Purpose
----------------
Get the series on a release of economic data.

Format
----------------
.. function:: x = fred_release_series(release_id[, ...])

    :param release_id: The id for a release. required

    :type release_id: integer

    :param realtime_start: The start of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_start: YYYY-MM-DD formatted string

    :param realtime_end: The end of the real-time period.  For more information, see Real-Time Periods. optional, default: today's date

    :type realtime_end: YYYY-MM-DD formatted string

    :param limit: The maximum number of results to return. optional, default: 1000

    :type limit: integer between 1 and 1000

    :param offset: Order results by values of the specified attribute. optional, default: 0

    :type offset: non-negative integer

    :param order_by: Order results by values of the specified attribute. 'title', 'units', 'frequency', 'seasonal_adjustment', 'realtime_start', 'realtime_end', 'last_updated', 'observation_start', 'observation_end', 'popularity','group_popularity'.
         optional, default: series_id

    :type order_by: One of the following strings: 'series_id'

    :param sort_order: Sort results is ascending or descending order for attribute values specified by order_by. 'desc'.
         optional, default: asc

    :type sort_order: One of the following strings: 'asc'

    :param filter_variable: The attribute to filter results by. 'units', 'seasonal_adjustment'.
         optional, no filter by default

    :type filter_variable: One of the following strings: 'frequency'

    :param filter_value: The value of the filter_variable attribute to filter results by. optional, no filter by default

    :type filter_value: String

    :param tag_names: A semicolon delimited list of tag names that series match all of. optional, no filtering by tags by default
         Example value: 'japan;imports'.  Filter results to series having both tags 'japan' and 'imports'.See the related request fred/tags.

    :type tag_names: String

    :param exclude_tag_names: A semicolon delimited list of tag names that series match none of. optional, no filtering by tags by default.
         Example value: 'imports;services'. 
            Filter results to series having neither tag 'imports' nor tag 'services'.
          
            Parameter exclude_tag_names requires that parameter tag_names also be set to limit the number of matching series.

    :type exclude_tag_names: String

    :return x: Results.
    :rtype x: Dataframe

.. note:: Supports additional arguments: ['realtime_start', 'realtime_end', 'limit', 'offset', 'order_by', 'sort_order', 'filter_variable', 'filter_value', 'tag_names', 'exclude_tag_names']

Examples
----------------

::

   head(fred_release_series(51));

   
       frequency  frequency_short group_popularity               id     last_updated            notes  observation_end observation_star       popularity     realtime_end   realtime_start seasonal_adjustm seasonal_adjustm            title            units      units_short 
         Monthly                M        1.0000000      BOMTVLM133S 2017-11-03 08:12 Further informat       2017-09-01       1992-01-01        1.0000000       2022-10-28       2022-10-28 Seasonally Adjus               SA U.S. Imports of  Million of Dolla        Mil. of $ 
         Monthly                M        1.0000000      BOMVGMM133S 2014-10-20 09:27 BEA has introduc       2013-12-01       1992-01-01        1.0000000       2022-10-28       2022-10-28 Seasonally Adjus               SA U.S. Imports of  Millions of Doll        Mil. of $ 
         Monthly                M        1.0000000      BOMVJMM133S 2014-10-20 09:26 BEA has introduc       2013-12-01       1992-01-01        1.0000000       2022-10-28       2022-10-28 Seasonally Adjus               SA U.S. Imports of  Millions of Doll        Mil. of $ 
         Monthly                M        1.0000000      BOMVMPM133S 2017-11-03 08:12 Further informat       2017-09-01       1992-01-01        1.0000000       2022-10-28       2022-10-28 Seasonally Adjus               SA U.S. Imports of  Million of Dolla        Mil. of $ 
         Monthly                M        1.0000000      BOMVOMM133S 2014-10-20 09:25 BEA has introduc       2013-12-01       1992-01-01        1.0000000       2022-10-28       2022-10-28 Seasonally Adjus               SA U.S. Imports of  Million of Dolla        Mil. of $ 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_releases`, :func:`fred_releases_dates`, :func:`fred_release`, :func:`fred_release_dates`, :func:`fred_release_sources`, :func:`fred_release_tags`, :func:`fred_release_related_tags`

