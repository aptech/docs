
eqSolvemtControlCreate
==============================================

Purpose
----------------

Creates default :class:`eqSolvemtControl` structure.

Format
----------------
.. function:: eqSolvemtControlCreate()

    :returns: **c** (*struct*) - instance of :class:`eqSolvemtControl` struct with
        members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be
declared before it can be used.

::

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
