
kmeansControlCreate
==============================================

Purpose
----------------

Fills a :class:`kmeansControl` structure with default settings.

Format
----------------
.. function:: kctl = kmeansControlCreate()

    :return kctl: instance of :class:`kmeansControl` struct with members set to default values.

    :rtype kctl: struct

Examples
----------------

::

    /*
    ** Declare 'kctl' as an instance of a
    ** 'kmeansControl' structure
    */
    struct kmeansControl kctl;

    // Apply default values to 'kctl'
    kctl = kmeansControlCreate();

Source
------

dstatmt.src

.. seealso:: Functions :func:`kmeansFit`
