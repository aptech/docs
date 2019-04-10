
gmmControlCreate
==============================================

Purpose
----------------

Creates default gmmFitControl structure.

Format
----------------
.. function:: gmmControlCreate()

    :returns: c (*struct*) instance of :class:`gmmFitControl` struct with
        members set to default values.

Examples
----------------

Since structures are strongly typed in GAUSS, each structure must be 
declared before it can be used.

::

    //declare 'c' as an 
    //gmmFitControl structure 
    struct gmmFitControl c;
    
    //initialize structure c
    c = gmmControlCreate();

The members of an :class:`gmmFitControl` structure and default values are described in
the manual entry for :func:`gmmFit`.

Source
------

gmm_est.src

.. seealso:: Functions :func:`gmmFit`, :func:`gmmFitIV`

