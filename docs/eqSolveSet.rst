
eqSolveSet
==============================================

Purpose
----------------

Sets global input used by :func:`eqSolve` to default values.

Format
----------------
.. function:: eqSolveSet

    :return __eqs_TypicalX: Set to 0.

    :rtype __eqs_TypicalX: scalar

    :return __eqs_TypicalF: Set to 0.

    :rtype __eqs_TypicalF: scalar

    :return __eqs_IterInfo: Set to 0.

    :rtype __eqs_IterInfo: scalar

    :return __eqs_JacobianProc: Set to 0.

    :rtype __eqs_JacobianProc: scalar

    :return __eqs_MaxIters: Set to 100.

    :rtype __eqs_MaxIters: scalar

    :return __eqs_StepTol: Set to :math:`\_\_macheps^{2/3}`

    :rtype __eqs_StepTol: scalar

Examples
-----------------

::

    // Set the global control variables
    // used by eqSolve to default values
    eqSolveSet();

Remarks
---------

As shown in the example above, the global control variables are not returned by :func:`eqSolveSet`. These global variables are set inside of :func:`eqSolveSet`.
