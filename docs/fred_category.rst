
fred_category
==============================================

Purpose
----------------
Get a category.

Format
----------------
.. function:: x = fred_category(category_id[, ...])

    :param category_id: The id for a category. default: 0 (root category)

    :type category_id: integer

    :return x: Results.
    :rtype x: Dataframe


Examples
----------------

::

   head(fred_category(125));

   
              id             name        parent_id 
       125.00000    Trade Balance               13 


Remarks
-----------

.. include:: remarks_fredapikey.rst
.. include:: remarks_realtime.rst

.. seealso:: :func:`fred_category_children`, :func:`fred_category_related`, :func:`fred_category_series`, :func:`fred_category_tags`, :func:`fred_category_related_tags`

