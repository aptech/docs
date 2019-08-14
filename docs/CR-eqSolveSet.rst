
eqSolveSet
==============================================

Purpose
----------------

Sets global input used by :func:`eqSolve` to default values.

Format
----------------
.. function:: eqSolveSet

    :returns: **__eqs_TypicalX** (*scalar*) - Set to 0.

    :returns: **__eqs_TypicalF** (*scalar*) - Set to 0.

    :returns: **__eqs_IterInfo** (*scalar*) - Set to 0.

    :returns: **__eqs_JacobianProc** (*scalar*) - Set to 0.

    :returns: **__eqs_MaxIters** (*scalar*) - Set to 100.

    :returns: **__eqs_StepTol** (*scalar*) - Set to :math:`\_\_macheps^{2/3}`

Examples
-----------------

::

    // Set the global control variables
    // used by eqSolve to default values
    eqSolveSet();

Remarks
---------

As shown in the example above, the global control variables are not returned by :func:`eqSolveSet`. These global variables are set inside of :func:`eqSolveSet`.
