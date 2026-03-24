
QNewtonmtOutCreate
==============================================

Purpose
----------------
Creates default :class:`QNewtonmtOut` structure.

Format
----------------
.. function:: c = QNewtonmtOutCreate()

    :return c: instance of :class:`QNewtonmtOut` struct with members set to default values.

    :rtype c: struct

Examples
--------

::

    // Declare output structure
    struct QNewtonmtOut out;

    // Initialize with default values
    out = QNewtonmtOutCreate();

Source
------

qnewtonmt.src

.. seealso:: Functions :func:`QNewtonmt`

