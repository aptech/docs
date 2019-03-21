
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

Global Input
------------

The following are set by eqSolveSet:

+-----------------+-----------------------------------------------------+
| \_eqs_JacobianP | pointer to a procedure which computes the           |
| roc             | analytical Jacobian. By default, eqSolve will       |
|                 | compute the Jacobian numerically.                   |
+-----------------+-----------------------------------------------------+
| \_eqs_MaxIters  | scalar, the maximum number of iterations. Default = |
|                 | 100.                                                |
+-----------------+-----------------------------------------------------+
| \_eqs_StepTol   | scalar, the step tolerance. Default =               |
|                 | \__macheps\ 2/3.                                    |
+-----------------+-----------------------------------------------------+
| \_eqs_TypicalF  | Kx1 vector of the typical F(x) values at a point    |
|                 | not near a root, used for scaling. This becomes     |
|                 | important when the magnitudes of the components of  |
|                 | F(x) are expected to be very different. By default, |
|                 | function values are not scaled.                     |
+-----------------+-----------------------------------------------------+
| \_eqs_TypicalX  | Kx1 vector of the typical magnitude of x, used for  |
|                 | scaling. This becomes important when the magnitudes |
|                 | of the components of x are expected to be very      |
|                 | different. By default, variable values are not      |
|                 | scaled.                                             |
+-----------------+-----------------------------------------------------+
| \_eqs_IterInfo  | scalar, if nonzero, iteration information is        |
|                 | printed. Default = 0.                               |
+-----------------+-----------------------------------------------------+

The following are set by gausset:

\__Tol



scalar, the tolerance of the scalar function f = 0.5\*\|\|F(x)|\|2
required to terminate the algorithm. Default = 1e-5.

\__altnam

Kx1 character vector of alternate names to be used by the printed
output. By default, the names "X1, X2,X3..." or "X01,X02,X03..."
(depending on how \__vpad is set) will be used.

\__output

scalar. If non-zero, final results are printed.

\__title

string, a custom title to be printed at the top of the iterations
report. By default, only a generic title will be printed.

\__vpad

scalar. If \__altnam is not set, variable names are automatically
created. Two types of names can be created:

 

0

Variable names are not padded to give them equal length. For example,
X1, X2,...,X10,...

 

1

Variable names are padded with zeros to give them an equal number of
characters. For example, X01,X02,...,X10,... This is useful if you want
the variable names to sort properly.
Remarks
-------

The equation procedure should return a column vector containing the
result for each equation. For example:

::

   Equation 1:   x12 + x22 - 2 = 0
   Equation 2:   exp(x1-1) + x23 - 2 = 0

::

   proc (1) = f(var);
      local x1,x2,eqns;
      x1 = var[1];
      x2 = var[2];
      eqns[1] = x1^2 + x2^2 - 2;       /* Equation 1 */
      eqns[2] = exp(x1-1) + x2^3 - 2;  /* Equation 2 */
      retp(eqns);
   endp;


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
------

eqsolve.src

solve system nonlinear equation
