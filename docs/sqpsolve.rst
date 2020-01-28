
sqpSolve
==============================================

Purpose
----------------
Solves the nonlinear programming problem using a sequential quadratic programming method.

Format
----------------
.. function:: { x, f, lagr, retcode } = sqpSolve(&fct, start)

    :param &fct: pointer to a procedure that computes the function to be minimized. This procedure must have one input
        argument, a vector of parameter values, and one output argument, the value of the function evaluated
        at the input vector of parameter values.
    :type &fct: function pointer

    :param start: start values
    :type start: Kx1 vector

    :return x: of parameters at minimum.

    :rtype x: Kx1 vector

    :return f: function evaluated at *x*.

    :rtype f: scalar

    :return lagr: created using :func:`vput`. Contains the Lagrangian
        for the constraints. They may be extracted with the :func:`vread` command using the following strings:

        ============== ===============================================
        ``"lineq"``     Lagrangians of linear equality constraints
        ``"nlineq"``    Lagrangians of nonlinear equality constraints
        ``"linineq"``   Lagrangians of linear inequality constraints
        ``"nlinineq"``  Lagrangians of nonlinear inequality constraints
        ``"bounds"``    Lagrangians of bounds
        ============== ===============================================

        Whenever a constraint is active, its associated Lagrangian will be nonzero.

    :rtype lagr: vector

    :return retcode: return code:

        == ====================================
        0  normal convergence
        1  forced exit
        2  maximum number of iterations exceeded
        3  function calculation failed
        4  gradient calculation failed
        5  Hessian calculation failed
        6  line search failed
        7  error with constraints
        == ====================================

    :rtype retcode: scalar

Global Input
------------

.. data:: \_sqp_A

    MxK matrix, linear equality constraint coefficients.

.. data:: \_sqp_B

    Mx1 vector, linear equality constraint constants. These globals are used to specify
    linear equality constraints of the following type:

    .. math:: \_sqp\_A * x = \_sqp\_B

    where *x* is the Kx1 unknown parameter vector.

.. data:: \_sqp_EqProc

    scalar, pointer to a procedure that computes the nonlinear equality constraints. For example, the statement:

    ::

        _sqp_EqProc = &eqproc;

    tells :func:`sqpSolve` that nonlinear equality constraints
    are to be placed on the parameters and where the
    procedure computing them is to be found. The
    procedure must have one input argument, the Kx1
    vector of parameters, and one output argument, the
    Rx1 vector of computed constraints that are to be
    equal to zero. For example, suppose that you wish
    to place the following constraint:

    ::

        p[1] * p[2] = p[3]

    The procedure for this is:

    ::

        proc eqproc(p);
            retp(p[1]*p[2]-p[3]);
        endp;

.. data:: \_sqp_C

    MxK matrix, linear inequality constraint coefficients.

.. data:: \_sqp_D

    Mx1 vector, linear inequality constraint constants. These globals are used to
    specify linear inequality constraints of the following type:

    .. math:: \_sqp\_C * X \geq \_sqp\_D

    where *x* is the Kx1 unknown parameter vector.

.. data:: \_sqp\_IneqProc

    scalar, pointer to a procedure that computes the nonlinear inequality constraints. For example the statement:

    ::

        _sqp_EqProc = &ineqproc;

    tells :func:`sqpSolve` that nonlinear equality constraints are to be placed on the parameters and
    where the procedure computing them is to be found. The procedure must have one input argument,
    the Kx1 vector of parameters, and one output argument, the Rx1 vector of computed constraints that
    are to be equal to zero. For example, suppose that you wish to place the following constraint:

    .. math:: p[1] * p[2] \geq p[3]

    The procedure for this is:

    ::

        proc ineqproc(p);
            retp(p[1]*[2]-p[3]);
        endp;

.. data:: \_sqp_Bounds

    Kx2 matrix, bounds on parameters. The first column contains the lower bounds, and the second
    column the upper bounds. If the bounds for all the coefficients are the same, a 1x2 matrix may
    be used. Default is:

    ::

        [1] -1e256     [2] 1e256

.. data:: \_sqp_GradProc

    scalar, pointer to a procedure that computes the gradient of the function with respect to the parameters. For example, the statement:

    ::

        _sqp_GradProc = &gradproc;

    tells :func:`sqpSolve` that a gradient procedure exists and where to find it. The user-provided
    procedure has two input arguments, a Kx1 vector of parameter values and an NxP matrix of data.
    The procedure returns a single output argument, an NxK matrix of gradients of the log-likelihood
    function with respect to the parameters evaluated at the vector of parameter values.

    Default = 0, i.e., no gradient procedure has been provided.

.. data:: \_sqp_HessProc

    scalar, pointer to a procedure that computes the Hessian, i.e., the matrix of second order
    partial derivatives of the function with respect to the parameters. For example, the instruction:

    ::

        _sqp_HessProc = &hessproc;

    will tell :func:`sqpSolve` that a procedure has been provided for the computation of the Hessian and
    where to find it. The procedure that is provided by the user must have two input arguments,
    a Px1 vector of parameter values and an NxK data matrix. The procedure returns a single output
    argument, the PxP symmetric matrix of second order derivatives of the function evaluated at the parameter values.

.. data:: \_sqp_MaxIters

    scalar, maximum number of iterations. Default = 1e+5. Termination can be forced by pressing :kbd:`C` on the keyboard.

.. data:: \_sqp_DirTol

    scalar, convergence tolerance for gradient of estimated coefficients. Default = 1e-5.
    When this criterion has been satisfied, :func:`sqpSolve` will exit the iterations.

.. data:: \_sqp_ParNames

    Kx1 character vector, parameter names.

.. data:: \_sqp_PrintIter

    scalar, if nonzero, prints iteration information. Default = 0. Can be toggled during iterations by pressing :kbd:`P` on the keyboard.

.. data:: \_sqp_FeasibleT

    scalar, if nonzero, parameters are tested for est feasibility before computing function in line search.
    If function is defined outside inequality boundaries, then this test can be turned off.

.. data:: \_sqp_RandRadius

    scalar, if zero, no random search is attempted. If nonzero it is the radius of random search
    which is invoked whenever the usual line search fails. Default = .01.

.. data:: \__output

    scalar, if nonzero, results are printed. Default = 0.


Examples
----------------

::

    // Reset all sqpSolve global variables

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

Remarks
-------

Pressing :kbd:`C` on the keyboard will terminate iterations, and pressing :kbd:`P` will toggle iteration output.

:func:`sqpSolve` is recursive, that is, it can call itself with another function and set of global variables,


Source
------

sqpsolve.src
