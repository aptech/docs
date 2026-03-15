
QNewtonmtControlCreate
==============================================

Purpose
----------------
Creates default :class:`QNewtonmtControl` structure.

Format
----------------
.. function:: c = QNewtonmtControlCreate()

    :return c: instance of :class:`QNewtonmtControl` struct with members set to default values.

    :rtype c: struct

Examples
--------

::

    // Declare structure
    struct QNewtonmtControl c;

    // Initialize with default values
    c = QNewtonmtControlCreate();

    // Set maximum iterations
    c.MaxIters = 500;

    // Print iteration information
    c.PrintIters = 1;

Source
------

qnewtonmt.src

.. seealso:: Functions :func:`QNewtonmt`

