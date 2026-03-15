
inthpControlCreate
==============================================

Purpose
----------------

Creates default :class:`inthpControl` structure.

Format
----------------
.. function:: c = inthpControlCreate()

    :return c: instance of :class:`inthpControl` struct with members set to default values.

    :rtype c: struct

Examples
--------

::

    // Declare structure
    struct inthpControl c;

    // Initialize with default values
    c = inthpControlCreate();

    // Set maximum function evaluations
    c.maxEvaluations = 50000;

    // Set relative error bound
    c.eps = 1e-8;

Source
------

inthp.src

.. seealso:: Functions :func:`inthp1`, :func:`inthp2`, :func:`inthp3`, :func:`inthp4`
