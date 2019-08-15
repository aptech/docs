
eqSolve
==============================================

Purpose
----------------

Solves a system of nonlinear equations.

Format
----------------
.. function:: { x, retcode } = eqSolve(&F, start)

    :param &F: a pointer to a procedure which computes the value at *x* of the equations to be solved and returns them in a column vector.
    :type &F: scalar

    :param start: starting values.
    :type start: Kx1 vector

    :return x: solution.

    :rtype x: Kx1 vector

    :return retcode: the return code:

        .. csv-table::
            :widths: auto

            "1", "Norm of the scaled function value is less than *__Tol*. *x* given is an approximate root of :math:`F(x)` (unless *__Tol* is too large)."
            "2", "The scaled distance between the last two steps is less than the step-tolerance (*_eqs_StepTol*). *x* may be an approximate root of :math:`F(x)`, but it is also possible that the algorithm is making very slow progress and is not near a root, or the step-tolerance is too large."
            "3", "The last global step failed to decrease ``norm2(F(x))`` sufficiently; either *x* is close to a root of :math:`F(x)` and no more accuracy is possible, or an incorrectly coded analytic Jacobian is being used, or the secant approximation to the Jacobian is inaccurate, or the step-tolerance is too large."
            "4", "Iteration limit exceeded."
            "5", "Five consecutive steps of maximum step length have been taken; either ``norm2(F(x))`` asymptotes from above to a finite value in some direction or the maximum step length is too small."
            "6", "*x* seems to be an approximate local minimizer of ``norm2(F(x))`` that is not a root of :math:`F(x)`. To find a root of :math:`F(x)`, restart :func:`eqSolvefrom` a different region."

    :rtype retcode: scalar

Global Input
------------

The following are set by eqSolveSet:

.. data:: \_eqs_JacobianProc

    pointer to a procedure which computes the analytical Jacobian. By default, :func:`eqSolve` will
    compute the Jacobian numerically.

.. data:: \_eqs_MaxIters

    scalar, the maximum number of iterations. Default = 100.

.. data:: \_eqs_StepTol

    scalar, the step tolerance. Default = :math:`\_\_macheps^{\frac{2}{3}}`.

.. data:: \_eqs_TypicalF

    Kx1 vector of the typical :math:`F(x)` values at a point not near a root, used for scaling. This becomes
    important when the magnitudes of the components of :math:`F(x)` are expected to be very different. By default,
    function values are not scaled.

.. data:: \_eqs_TypicalX

    Kx1 vector of the typical magnitude of *x*, used for scaling. This becomes important when the magnitudes
    of the components of *x* are expected to be very different. By default, variable values are not scaled.

.. data:: \_eqs_IterInfo

    scalar, if nonzero, iteration information is printed. Default = 0.

The following are set by :func:`gausset`:

.. data:: \__Tol

    scalar, the tolerance of the scalar function :math:`f = 0.5*\left|\left|F(x)\right|\right|^2`
    required to terminate the algorithm. Default = 1e-5.

.. data:: \__altnam

    Kx1 character vector of alternate names to be used by the printed
    output. By default, the names :code:`X1, X2, X3...` or :code:`X01, X02, X03...`
    (depending on how `\__vpad` is set) will be used.

.. data:: \__output

    scalar. If non-zero, final results are printed.

.. data:: \__title

    string, a custom title to be printed at the top of the iterations
    report. By default, only a generic title will be printed.

.. data:: \__vpad

    scalar. If `\__altnam` is not set, variable names are automatically
    created. Two types of names can be created:

    .. csv-table::
        :widths: auto

        "0", "Variable names are not padded to give them equal length. For example, :code:`X1, X2, ..., X10, ...`"
        "1", "Variable names are padded with zeros to give them an equal number of characters. For example, :code:`X01, X02, ..., X10, ...` This is useful if you want the variable names to sort properly."

Remarks
-------

The equation procedure should return a column vector containing the
result for each equation. For example, consider a two-equation system given by:

.. math:: x_1^2 + x_2^2 - 2 = 0
.. math:: e^{x_1-1} + x_2^3 - 2 = 0


::

   proc (1) = f(var);
      local x1, x2, eqns;

      // Set x1
      x1 = var[1];

      // Set x2
      x2 = var[2];

      // Pre-allocate output vector
      eqns = zeros(2,1);

      // Equation 1
      eqns[1] = x1^2 + x2^2 - 2;

      // Equation 2
      eqns[2] = exp(x1-1) + x2^3 - 2;

      retp(eqns);
   endp;

Note that the first equation in the system is contained in the first row of ``eqns`` and the second equation is in the second row of ``eqns``.

Examples
----------------

::

    // Reset all eqSolve global variables
    eqSolveSet();

    // Procedure to compute nonlinear equations
    proc (1) = f(x);
       local f1, f2, f3;

       // Function one
       f1 = 3*x[1]^3 + 2*x[2]^2 + 5*x[3] - 10;

       // Function two
       f2 = -x[1]^3 - 3*x[2]^2 + x[3] + 5;

       // Function three
       f3 = 3*x[1]^3 + 2*x[2]^2 - 4*x[3];

       retp(f1|f2|f3);
    endp;

    // Procedure to compute Jacobian
    proc (1) = fjc(x);
       local fjc1, fjc2, fjc3;

       fjc1 = 9*x[1]^2 ~ 4*x[2] ~ 5;
       fjc2 = -3*x[1]^2 ~ -6*x[2] ~ 1;
       fjc3 = 9*x[1]^2 ~ 4*x[2] ~ -4;

       retp(fjc1|fjc2|fjc3);
    endp;

    // Starting values
    start = { -1, 12, -1 };

    // Set pointer to Jacobian procedure
    _eqs_JacobianProc = &fjc;

    // Perform estimation and print report
    { x, tcode } = eqSolve(&f, start);

::

    =========================================================
     EqSolve Version 14.0.1              
    =========================================================

    ||F(X)|| at final solution:                   0.93699762
    ---------------------------------------------------------
    Termination Code = 1:

    Norm of the scaled function value is less than __Tol;
    ---------------------------------------------------------

    ---------------------------------------------------------
    VARIABLE     START          ROOTS               F(ROOTS)
    ---------------------------------------------------------
    X1          -1.00000       0.54144351      4.4175402e-006
    X2          12.00000        1.4085912     -6.6263102e-006
    X3          -1.00000        1.1111111      4.4175402e-006
    ---------------------------------------------------------

Source
------

eqsolve.src
