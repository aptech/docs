
qfitControlCreate
==============================================

Purpose
----------------

Creates default :class:`qfitControl` structure.

Format
----------------
.. function:: qfitControlCreate()

    :returns: qctl (*struct*) instance of :class:`qfitControl` struct with members set to default values.

Examples
----------------
Since structures are strongly typed in GAUSS, each structure must be declared before it can be used.

::

    // Declare 'ctl' as an qfitControl structure
    struct qfitControl ctl;
    
    // Initialize structure 'ctl'
    ctl = qfitControlCreate();

The members of the :class:`qfitControl` structure and their default values are described in the
manual entry for :func:`quantileFit`.

Source
------

quantilefit.src

.. seealso:: Functions :func:`quantileFit`, :func:`quantileFitLoc`

