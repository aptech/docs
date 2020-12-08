
loadFileControlCreate
==============================================

Purpose
----------------

Creates an instance of a structure of type :class:`loadFileControl` set to default values.

Format
----------------
.. function:: ld_ctl = loadFileControlCreate()

    :return ld_ctl: instance of :class:`loadFileControl` struct.

    :rtype ld_ctl: struct

Examples
----------------

::

    // Declare instance of structure
    struct loadFileControl ld_ctl;

    // Initialize the structure to default values
    ld_ctl = loadFileControlCreate();


.. seealso:: Functions :func:`loadd`
