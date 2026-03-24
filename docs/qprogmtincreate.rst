
QProgmtInCreate
==============================================

Purpose
----------------
Creates an instance of a structure of type :class:`QProgmtInCreate` with the *maxit* member set to a default value.

Format
----------------
.. function:: s = QProgmtInCreate()

    :return s: instance of :class:`QProgmtIn` struct.

    :rtype s: struct

Examples
--------

::

    // Create and initialize the input structure
    struct qprogMTIn qIn;
    qIn = QProgmtInCreate();

    // Set up the quadratic programming problem
    qIn.q = { 2 0, 0 2 };
    qIn.r = { 1, 1 };
    qIn.start = zeros(2, 1);
    qIn.maxit = 500;

Source
------

qprogmt.src

.. seealso:: Functions :func:`QProgmt`
