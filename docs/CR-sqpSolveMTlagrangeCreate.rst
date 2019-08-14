
sqpSolveMTlagrangeCreate
==============================================

Purpose
----------------
Creates an instance of a structure of type :class:`sqpSolveMTlagrange` set to default values.

Include
-------

sqpsolvemt.sdf

Format
----------------
.. function:: s = sqpSolveMTlagrangeCreate()

    :return s: instance of :class:`sqpSolveMTlagrange` struct.

    :type s: struct

Examples
----------------

::

    // Declare instance of structure
    struct sqpSolveMTlagrange sla;
    
    // Initialize the structure to default values
    sla = sqpSolveMTlagrangeCreate();

Source
------

sqpsolvemt.src

.. seealso:: Functions :func:`sqpSolve`

