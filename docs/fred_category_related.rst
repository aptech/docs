
fred_category_related
==============================================

Purpose
----------------
Get the related categories for a category. A related category is a one-way relation between 2 categories that is not part of a parent-child category hierarchy. 
Most categories do not have related categories.

Format
----------------
.. function:: x = fred_category_related(category_id[, ...])

    :param category_id: The id for a category. required

    :type category_id: integer

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

    head(fred_category_related(32073));

    
              id             name        parent_id 
       149.00000         Arkansas        27281.000 
       150.00000         Illinois        27281.000 
       151.00000          Indiana        27281.000 
       152.00000         Kentucky        27281.000 
       153.00000      Mississippi        27281.000 


Remarks
-----------

.. include:: include/remarks_fredapikey.rst
.. include:: include/remarks_realtime.rst

.. seealso:: :func:`fred_category`, :func:`fred_category_children`, :func:`fred_category_series`, :func:`fred_category_tags`, :func:`fred_category_related_tags`

