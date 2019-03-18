
olsmtControlCreate
==============================================

Purpose
----------------

Creates default olsmtControl structure.

Format
----------------
.. function:: olsmtControlCreate()

    :returns: c (*TODO*), instance of an olsmtControl structure
        with members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared 
before it can be used.

::

    // declare 'ctl' as an olsmtControl structure
    struct olsmtControl ctl; 
    
    // initialize structure 'ctl'
    ctl = olsmtControlCreate;

The members of the olsmtControl structure and their default values are described in the
manual entry for olsmt.

Source
++++++

olsmt.src

.. seealso:: Functions :func:`olsmt`

ols least square regression linear struct structure control create
