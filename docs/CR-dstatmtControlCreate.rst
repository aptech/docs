
dstatmtControlCreate
==============================================

Purpose
----------------

Fills a :class:`dstatmtControl` structure with default settings.

Format
----------------
.. function:: c = dstatmtControlCreate()

    :returns: **dctl** (*struct*) - instance of :class:`dstatmtControl` struct with members set to default values.

Examples
----------------

::

    /*
    ** Declare 'dctl' as an instance of a
    ** 'dstatmtControl' structure
    */
    struct dstatmtControl dctl;

    // Apply default values to 'dctl'
    dctl = dstatmtControlCreate();

Source
------

dstatmt.src

.. seealso:: Functions :func:`dstatmt`
