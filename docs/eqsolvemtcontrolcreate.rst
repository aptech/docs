
eqSolvemtControlCreate
==============================================

Purpose
----------------

Fills an :class:`eqSolvemtControl` structure with default settings.

Format
----------------
.. function:: c = eqSolvemtControlCreate()

    :return c: instance of :class:`eqSolvemtControl` struct with
        members set to default values.

    :rtype c: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be
declared before it can be used.

::

    new;

    /*
    ** Declare 'c' as an
    ** eqSolvemtControl structure
    */
    struct eqSolvemtControl c;

    // Initialize structure c
    c = eqSolvemtControlCreate();

The members of an :class:`eqSolvemtControl` structure and default values are described in
the manual entry for :func:`eqSolvemt`.

Source
------

eqsolvemt.src

.. seealso:: Functions :func:`eqSolvemt`
