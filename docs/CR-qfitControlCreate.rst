
qfitControlCreate
==============================================

Purpose
----------------

Creates default qfitControl structure.

Format
----------------
.. function:: qfitControlCreate()

    :returns: qctl (*TODO*), instance of an qfitControl structure
        with members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared
before it can be used.

::

    // Declare 'ctl' as an qfitControl structure
    struct qfitControl ctl;
    
    // Initialize structure 'ctl'
    ctl = qfitControlCreate();

The members of the qfitControl structure and their default values are described in the
manual entry for quantileFit.

Source
++++++

quantilefit.src

.. seealso:: Functions :func:`quantileFit`, :func:`quantileFitLoc`
