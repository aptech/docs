
mlmtControlCreate
==============================================

Purpose
----------------

Creates default mlmtControl structure.

Format
----------------
.. function:: c = mlmtControlCreate()

    :return c: instance of :class:`mlmtControl` struct with members set to default values.

    :rtype c: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared before it can be used.

::

    // Declare 'ctl' as an mlmtControl structure
    struct mlmtControl ctl;

    // Initialize structure 'ctl'
    ctl = mlmtControlCreate();

The members of the :class:`mlmtControl` structure and their default values are described in the
manual entry for :func:`mlmt`.

Source
------

mlmt.src

.. seealso:: Functions :func:`mlmt`
