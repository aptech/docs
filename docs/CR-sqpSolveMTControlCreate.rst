
sqpSolveMTControlCreate
==============================================

Purpose
----------------

Creates an instance of a structure of type :class:`sqpSolveMTcontrol` set to default values.

Include
-------

sqpsolvemt.sdf

Format
----------------
.. function:: s = sqpSolveMTControlCreate()

    :return s: instance of :class:`sqpSolveMTControl` struct.

    :type s: struct

Examples
----------------

::

    // Declare instance of structure
    struct sqpSolveMTControl s;
    
    // Initialize the structure to default values
    s = sqpSolveMTControlCreate();

Source
------

sqpsolvemt.src

.. seealso:: Functions :func:`sqpSolve`

