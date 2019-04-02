
eqSolvemtOutCreate
==============================================

Purpose
----------------

Creates default :class:`eqSolvemtOut` structure.

Format
----------------
.. function:: eqSolvemtOutCreate()

    :returns: c (*struct*) instance of :class:`eqSolvemtOut` struct with members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be 
declared before it can be used.

::

    //declare structure
    struct eqSolvemtOut c;
    
    //Initialize structure
    c = eqSolvemtOutCreate();

The members of an :class:`eqSolvemtOut` structure and default values are described in
the manual entry for :func:`eqSolvemt`.

Source
------

eqsolvemt.src

.. seealso:: Functions :func:`eqSolvemt`

