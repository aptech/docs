
sqpSolveMToutCreate
==============================================

Purpose
----------------
Creates an instance of a structure of type :class:`sqpSolveMTout` set to default values.

Include
-------

sqpsolvemt.sdf

Format
----------------
.. function:: sqpSolveMToutCreate()

    :returns: s (*struct*) instance of :class:`sqpSolveMTout` struct.

Examples
----------------

::

    // Declare instance of structure
    struct sqpSolveMTout out;
    
    // Initialize the structure to default values
    out = sqpSolveMToutCreate();

Source
------

sqpsolvemt.src

.. seealso:: Functions :func:`sqpSolve`

