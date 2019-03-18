
eqSolve
==============================================

Purpose
----------------

Solves a system of nonlinear equations.

Format
----------------
.. function:: eqSolve(&F, start)

    :param &F: a pointer to a procedure which computes the
        value at x of the equations to be solved.
    :type &F: scalar

    :param start: starting values.
    :type start: Kx1 vector

    :returns: x (*Kx1 vector*), solution.

    :returns: retcode (*scalar*), the return code:

    .. csv-table::
        :widths: auto

        "1", "Norm of the scaled function value is less than__Tol. x given is an approximate root of F(x)(unless __Tol is too large)."
        "2", "The scaled distance between the last two steps isless than the step-tolerance (_eqs_StepTol).x may be an approximate root of F(x), but it isalso possible that the algorithm is making very slow progress and is not near a root, or the step-tolerance is too large."
        "3", "The last global step failed to decreasenorm2(F(x)) sufficiently; either x is close to aroot of F(x) and no more accuracy is possible, oran incorrectly coded analytic Jacobian is being used, or the secant approximation to the Jacobianis inaccurate, or the step-tolerance is too large."
        "4", "Iteration limit exceeded."
        "5", "Five consecutive steps of maximum step lengthhave been taken; either norm2(F(x))asymptotes from above to a finite value in some direction or the maximum step length is too small."
        "6", "x seems to be an approximate local minimizer ofnorm2(F(x)) that is not a root of F(x).To find a root of F(x), restart eqSolvefrom a different region."

Examples
----------------

::

    eqSolveSet();
     
    proc (1) = f(x);
       local f1,f2,f3;
       f1 = 3*x[1]^3 + 2*x[2]^2 + 5*x[3] - 10;
       f2 = -x[1]^3 - 3*x[2]^2 + x[3] + 5;
       f3 = 3*x[1]^3 + 2*x[2]^2 - 4*x[3];
       retp(f1|f2|f3);
    endp;
    
    proc (1) = fjc(x);
       local fjc1,fjc2, fjc3;
       fjc1 = 9*x[1]^2 ~ 4*x[2] ~ 5;
       fjc2 = -3*x[1]^2 ~ -6*x[2] ~ 1;
       fjc3 = 9*x[1]^2 ~ 4*x[2] ~ -4;
       retp(fjc1|fjc2|fjc3);
    endp;
     
    start = { -1, 12, -1 };
     
    _eqs_JacobianProc = &fjc;
     
    { x,tcode } = eqSolve(&f,start);

::

    =========================================================
     EqSolve Version 11.0.5              7/17/2015   5:47 pm
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
++++++

eqsolve.src

solve system nonlinear equation
