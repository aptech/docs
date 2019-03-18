
gmmControlCreate
==============================================

Purpose
----------------

Creates default gmmFitControl structure.

Format
----------------
.. function:: gmmControlCreate()

    :returns: c (*TODO*), instance of gmmFitControl structure with
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

The members of an gmmFitControl structure and default values are described in
the manual entry for gmmFit.

Source
++++++

gmm_est.src

.. seealso:: Functions :func:`gmmFit`, :func:`gmmFitIV`
