
fred_category_children
==============================================

Purpose
----------------
Get the child categories for a specified parent category.

Format
----------------
.. function:: x = fred_category_children(category_id[, ...])

    :param category_id: The id for a category. default: 0 (root category)

    :type category_id: integer

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

   head(fred_category_children(13));

   
              id             name        parent_id 
       16.000000          Exports        13.000000 
       17.000000          Imports        13.000000 
       3000.0000 Income Payments         13.000000 
       33705.000 International In        13.000000 
       125.00000    Trade Balance        13.000000 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_category`, :func:`fred_category_related`, :func:`fred_category_series`, :func:`fred_category_tags`, :func:`fred_category_related_tags`

