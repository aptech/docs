
eqSolveSet
==============================================

Purpose
----------------

Sets global input used by :func:`eqSolve` to default values.

Format
----------------
.. function:: eqSolveset

    :returns: **__eqs_TypicalX** (*scalar*) - Set to 0.

    :returns: **__eqs_TypicalF** (*scalar*) - Set to 0.

    :returns: **__eqs_IterInfo** (*scalar*) - Set to 0.

    :returns: **__eqs_JacobianProc** (*scalar*) - Set to 0.

    :returns: **__eqs_MaxIters** (*scalar*) - Set to 100.

    :returns: **__eqs_StepTol** (*scalar*) - Set to :math:`\_\_macheps^{2/3}`
