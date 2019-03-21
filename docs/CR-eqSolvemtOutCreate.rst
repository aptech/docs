
eqSolvemtOutCreate
==============================================

Purpose
----------------

Creates default eqSolvemtOut structure.

Format
----------------
.. function:: eqSolvemtOutCreate()

    :returns: c (*TODO*), instance of eqSolvemtOut structure with members
        set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be 
declared before it can be used.

::

    //declare structure
    struct eqSolvemtOut c;
    
    //Initialize structure
    c = eqSolvemtOutCreate();

The members of an eqSolvemtOut structure and default values are described in
the manual entry for eqSolvemt.

Source
------

eqsolvemt.src

.. seealso:: Functions :func:`eqSolvemt`
