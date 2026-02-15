
minimize
==============================================

Purpose
----------------

Minimizes a function using the L-BFGS-B algorithm for bound-constrained optimization.

Format
----------------
.. function:: out = minimize(&fct, x0)
              out = minimize(&fct, x0, ctl)
              out = minimize(&fct, x0, ...)
              out = minimize(&fct, x0, ..., ctl)

    :param &fct: pointer to a procedure that computes the objective function to be minimized.
        The procedure receives the parameter vector *x* as its first argument, plus any additional
        data arguments passed to :func:`minimize`.
    :type &fct: function pointer

    :param x0: Kx1 vector, starting values for the parameters.
    :type x0: vector

    :param ...: Optional extra arguments. These arguments are passed untouched to the user-provided objective function.
    :type ...: any

    :param ctl: Optional input. Instance of a :class:`minimizeControl` structure. Normally an instance
        is initialized by calling :func:`minimizeControlCreate` and members of this instance can be
        set to other values by the user. For an instance named *ctl*, the members are:

        .. csv-table::
            :widths: auto

            "ctl.m", "scalar, number of L-BFGS corrections to store. Default = 10."
            "ctl.maxIters", "scalar, maximum number of iterations. Default = 1000."
            "ctl.factr", "scalar, function convergence tolerance factor. Convergence occurs when ``|f_k - f_{k+1}| < factr * machine_epsilon``. Use 1e12 for low accuracy, 1e7 for moderate accuracy (default), 1e1 for high accuracy."
            "ctl.pgtol", "scalar, projected gradient tolerance. Default = 1e-5."
            "ctl.printLevel", "scalar, output level: 0 = silent (default), 1 = final summary, 2 = each iteration."
            "ctl.lb", "scalar or Kx1 vector, lower bounds on parameters. If scalar, applies to all parameters. Default = -1e300 (effectively unbounded)."
            "ctl.ub", "scalar or Kx1 vector, upper bounds on parameters. If scalar, applies to all parameters. Default = 1e300 (effectively unbounded)."

    :type ctl: struct

    :return out: an instance of a :class:`minimizeOut` structure. For an instance named *out*, the members are:

        .. list-table::
            :widths: auto

            * - out.par
              - Kx1 vector, solution parameter values.
            * - out.fct
              - scalar, objective function value at solution.
            * - out.gradient
              - Kx1 vector, gradient at solution.
            * - out.retcode
              - scalar, return code:

                  :0: Converged successfully.
                  :1: Maximum iterations exceeded.
                  :2: Abnormal termination (search direction too small).
                  :3: Error in problem setup or evaluation.

            * - out.iterations
              - scalar, number of iterations used.
            * - out.fnEvals
              - scalar, number of function evaluations.
            * - out.retmsg
              - string, message describing convergence status.

    :rtype out: struct

Examples
----------------

Example 1: Basic unconstrained minimization
++++++++++++++++++++++++++++++++++++++++++++

::

    // Rosenbrock function
    proc (1) = rosenbrock(x);
        retp((1 - x[1])^2 + 100*(x[2] - x[1]^2)^2);
    endp;

    // Starting point
    x0 = { -1, 1 };

    // Minimize
    struct minimizeOut out;
    out = minimize(&rosenbrock, x0);

    print "Solution: " out.par';
    print "Objective: " out.fct;

Example 2: With data arguments
++++++++++++++++++++++++++++++++++++++++++++

::

    // OLS objective function
    proc (1) = ols_objective(beta, Y, X);
        local resid;
        resid = Y - X * beta;
        retp(resid'resid);
    endp;

    // Generate sample data
    X = ones(100, 1) ~ rndn(100, 2);
    beta_true = { 1, 2, -1 };
    Y = X * beta_true + 0.5*rndn(100, 1);

    // Starting values
    x0 = zeros(3, 1);

    // Minimize - pass Y and X as data arguments
    struct minimizeOut out;
    out = minimize(&ols_objective, x0, Y, X);

    print "Estimated coefficients:";
    print out.par';

Example 3: Bound-constrained optimization
++++++++++++++++++++++++++++++++++++++++++++

::

    proc (1) = myfunc(x);
        retp(sumc(x.^2));
    endp;

    x0 = { 5, 5, 5 };

    // Set bounds: all parameters in [0, 10]
    struct minimizeControl ctl;
    ctl = minimizeControlCreate();
    ctl.lb = 0;
    ctl.ub = 10;

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

    print "Solution: " out.par';

Example 4: Variable-specific bounds
++++++++++++++++++++++++++++++++++++++++++++

::

    proc (1) = myfunc(x);
        retp((x[1] - 2)^2 + (x[2] - 3)^2);
    endp;

    x0 = { 0, 0 };

    // x[1] >= 0, x[2] in [0, 2]
    struct minimizeControl ctl;
    ctl = minimizeControlCreate();
    ctl.lb = { 0, 0 };
    ctl.ub = { 1e300, 2 };

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

    // Solution will be constrained: x = {2, 2}
    print "Solution: " out.par';

Remarks
-------

:func:`minimize` uses the L-BFGS-B algorithm, a limited-memory quasi-Newton method
that is the gold standard for smooth bound-constrained optimization. It is
particularly suitable for:

- Smooth differentiable objective functions
- Large-scale problems (hundreds to thousands of variables)
- Simple bound constraints (each parameter has a lower and/or upper bound)

L-BFGS-B approximates the Hessian using a limited number of past gradients
(controlled by ``ctl.m``), making it memory-efficient for large problems.

For problems with more complex constraints (linear equality/inequality,
nonlinear constraints), use :func:`sqpSolveMT` instead.

**Gradient computation:**

:func:`minimize` automatically computes gradients numerically using finite differences.
Future versions may support user-provided analytical gradients.

**Convergence criteria:**

The algorithm terminates when either:

1. The function value change is small: ``|f_k - f_{k+1}| < factr * eps``
2. The projected gradient is small: ``max|g_i| < pgtol``
3. Maximum iterations is reached

**Starting point:**

If the starting point *x0* violates any bounds, it is automatically projected
into the feasible region before optimization begins.

.. seealso:: Functions :func:`minimizeControlCreate`, :func:`sqpSolveMT`

