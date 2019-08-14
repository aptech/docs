
olsmtControlCreate
==============================================

Purpose
----------------

Creates default olsmtControl structure.

Format
----------------
.. function:: c = olsmtControlCreate()

    :return c: instance of :class:`olsmtControl` struct with members set to default values.

    :type c: struct

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared 
before it can be used.

::

    // declare 'ctl' as an olsmtControl structure
    struct olsmtControl ctl; 
    
    // initialize structure 'ctl'
    ctl = olsmtControlCreate;

The members of the :class:`olsmtControl` structure and their default values are described in the
manual entry for :func:`olsmt`.

Source
------

olsmt.src

.. seealso:: Functions :func:`olsmt`

