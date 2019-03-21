
sqpSolve
==============================================

Purpose
----------------
Solves the nonlinear programming problem using a sequential quadratic programming method.

Format
----------------
.. function:: sqpSolve(&fct, start)

    :param &fct: pointer to a procedure that computes the function to be minimized. This procedure must have one input
        argument, a vector of parameter values, and one output argument, the value of the function evaluated
        at the input vector of parameter values.
    :type &fct: TODO

    :param start: 
    :type start: Kx1 vector of start values

    :returns: x (*TODO*), Kx1 vector of parameters at minimum.

    :returns: f (*scalar*), function evaluated at x.

    :returns: lagr (*vector*), created using vput. Contains the Lagrangean
        for the constraints. They may be extracted with the
        vread command using the following strings:

    .. csv-table::
        :widths: auto

        ""lineq"", "Lagrangeans of linear equality constraints,"
        ""nlineq"", "Lagrangeans of nonlinear equality constraints"
        ""linineq"", "Lagrangeans of linear inequality constraints"
        ""nlinineq"", "Lagrangeans of nonlinear inequality constraints"
        ""bounds"", "Lagrangeans of bounds"
        "Whenever a constraint is active, its associated Lagrangean will be nonzero."

    :returns: retcode (*TODO*), return code:

    .. csv-table::
        :widths: auto

        "0", "normal convergence"
        "1", "forced exit"
        "2", "maximum number of iterations exceeded"
        "3", "function calculation failed"
        "4", "gradient calculation failed"
        "5", "Hessian calculation failed"
        "6", "line search failed"
        "7", "error with constraints"

Remarks
-------

Pressing C on the keyboard will terminate iterations, and pressing P
will toggle iteration output.

sqpSolve is recursive, that is, it can call itself with another function
and set of global variables,


Examples
----------------

::

    //Reset all sqpSolve global variables
                    
    sqpSolveSet;
     
    proc fct(x);
      retp( (x[1] + 3*x[2] + x[3])^2 + 4*(x[1] - x[2])^2);
    endp;
     
    proc ineqp(x);
     retp(6*x[2] + 4*x[3] - x[1]^3 - 3);
    endp;
     
    proc eqp(x);
     retp(1-sumc(x));
    endp;
     
    _sqp_Bounds = { 0 1e256 };
     
    start = { .1, .7, .2 };
     
    _sqp_IneqProc = &ineqp;
    _sqp_EqProc = &eqp;
     
    { x,f,lagr,ret } = sqpSolve(&fct,start);

Source
------

sqpsolve.src

solve nonlinear programming problem sequential quadratic
