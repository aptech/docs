
gmmControlCreate
==============================================

Purpose
----------------

Creates default :class:`gmmFitControl` structure.

Format
----------------
.. function:: c = gmmControlCreate()

    :return c: instance of :class:`gmmFitControl` struct with
        members set to default values.

    :rtype c: struct

Examples
----------------

Since structures are strongly typed in GAUSS, each structure must be
declared before it can be used.

::

    /*
    ** Declare 'c' as an
    ** gmmFitControl structure
    */
    struct gmmFitControl c;

    // Initialize structure c
    c = gmmControlCreate();

The members of an :class:`gmmFitControl` structure and default values are described in
the manual entry for :func:`gmmFit`.

Source
------

gmm_est.src

.. seealso:: Functions :func:`gmmFit`, :func:`gmmFitIV`
