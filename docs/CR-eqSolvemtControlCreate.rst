
eqSolvemtControlCreate
==============================================

Purpose
----------------

Creates default eqSolvemtControl structure.

Format
----------------
.. function:: eqSolvemtControlCreate()

    :returns: c (*TODO*), instance of eqSolvemtControl structure with
        members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be 
declared before it can be used.

::

    //declare 'c' as an 
    //eqSolvemtControl structure 
    struct eqSolvemtControl c;
    
    //initialize structure c
    c = eqSolvemtControlCreate();

The members of an eqSolvemtControl structure and default values are described in
the manual entry for eqSolvemt.

Source
++++++

eqsolvemt.src

.. seealso:: Functions :func:`eqSolvemt`

solve system nonlinear equation struct structure control create
