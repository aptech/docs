
cmlmtControlCreate
==============================================

Purpose
----------------

Creates default cmlmtControl structure.

Format
----------------
.. function:: c = cmlmtControlCreate()

    :return c: instance of :class:`cmlmtControl` struct with members set to default values.

    :rtype c: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared before it can be used.

::

    // Declare 'ctl' as an cmlmtControl structure
    struct cmlmtControl ctl;

    // Initialize structure 'ctl'
    ctl = cmlmtControlCreate();

The members of the :class:`cmlmtControl` structure and their default values are described in the
manual entry for :func:`cmlmt`.

Source
------

cmlmt.src

.. seealso:: Functions :func:`cmlmt`
