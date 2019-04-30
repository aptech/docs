
sqpSolveMTControlCreate
==============================================

Purpose
----------------

Creates an instance of a structure of type 
sqpSolveMTcontrol set to default values.

Format
----------------
.. function:: sqpSolveMTControlCreate()

    :returns: s (*struct*) instance of :class:`sqpSolveMTControl` struct.

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

create struct structure type sqpSolveMTcontrol default value
