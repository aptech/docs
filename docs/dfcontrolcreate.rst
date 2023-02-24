
dfControlCreate
==============================================

Purpose
----------------

Fills a :class:`dfControl` structure with default settings.

Format
----------------
.. function:: dfc = dfControlCreate()

    :return kctl: instance of :class:`dfControl` struct with members set to default values.

    :rtype kctl: struct

Examples
----------------

::

    /*
    ** Declare 'dfc' as an instance of a
    ** 'kmeansControl' structure
    */
    struct dfControl kctl;

    // Apply default values to 'dfc'
    dfc = dfControlCreate();

Source
------

decision_forest.src

.. seealso:: Functions :func:`decForestCFit`, :func:`decForestRFit`
