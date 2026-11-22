
minimize
==============================================

Purpose
----------------

Minimizes a function using L-BFGS-B for bound-constrained optimization or
Nelder-Mead for unconstrained optimization without derivatives.

Format
----------------
.. function:: out = minimize(&fct, x0)
              out = minimize(&fct, x0, ctl)
              out = minimize(&fct, x0, ...)
              out = minimize(&fct, x0, ..., ctl)
              out = minimize(&fct, x0, method="nelder-mead")
              out = minimize(&fct, x0, ..., ctl, method="nelder-mead")
              out = minimize(&fct, x0, ..., gradCheck=1)

    :param &fct: pointer to a procedure that computes the objective function to be minimized.
        The procedure receives the parameter vector *x* as its first argument, plus any additional
        data arguments passed to :func:`minimize`.
    :type &fct: function pointer

    :param x0: Kx1 vector, starting values for the parameters.
    :type x0: vector

    :param method: Optional named algorithm, ``"nelder-mead"`` or ``"lbfgsb"``
        (also accepts ``"l-bfgs-b"``). Overrides ``ctl.method`` when supplied.
        Otherwise uses ``ctl.method``, whose default is L-BFGS-B. Place any
        positional data arguments and control structure before the named option.
    :type method: string

    :param gradCheck: Optional 0 or 1 (default 0). Set to 1 to print and check
        the supplied gradient at the starting point. Either this keyword or
        ``ctl.gradCheck`` set to 1 enables the check. Requires a ``proc (2)``
        objective. See Gradient computation below.
    :type gradCheck: scalar

    :param ...: Optional extra arguments. These arguments are passed untouched to the user-provided objective function.
    :type ...: any

    :param ctl: Optional input. Instance of a :class:`minimizeControl` structure. Normally an instance
        is initialized by calling :func:`minimizeControlCreate` and members of this instance can be
        set to other values by the user. For an instance named *ctl*, the members are:

        .. csv-table::
            :widths: auto

            "ctl.method", "string, algorithm: ``lbfgsb`` (default, also accepts ``l-bfgs-b``) or ``nelder-mead``. Nelder-Mead is unconstrained and requires a scalar objective."
            "ctl.fTol", "Nelder-Mead only: absolute objective spread tolerance. Default = 1e-10."
            "ctl.xTol", "Nelder-Mead only: maximum coordinate spread tolerance. Default = 1e-5."
            "ctl.maxEvals", "Nelder-Mead only: -1 (default) selects 200 times the number of parameters. 0 means unlimited; positive values set an explicit limit. Limits above 2,147,483,647, including infinity, are treated as 2,147,483,647, which no practical run reaches. Checked between simplex steps; initialization, shrink or restart may exceed the limit."
            "ctl.maxRestarts", "Nelder-Mead only: maximum stall restarts. Default = 3."
            "ctl.stallLimit", "Nelder-Mead only: iterations without an improved best value before restarting. 0 (default) selects 50 times the parameter count."
            "ctl.initialStep", "Nelder-Mead only: initial displacement as a fraction of the absolute starting coordinate. Default = 0.05."
            "ctl.zeroStep", "Nelder-Mead only: initial displacement for coordinates with absolute value at most 1e-8. Default = 0.00025."
            "ctl.m", "scalar, number of L-BFGS corrections to store. Default = 10."
            "ctl.maxIters", "scalar, maximum iterations. -1 (default) selects 200 times the number of parameters for Nelder-Mead or 1000 for L-BFGS-B. Positive whole numbers set an explicit limit. Limits above 2,147,483,647, including infinity, are treated as 2,147,483,647, which no practical run reaches. Other values return a setup error before evaluation."
            "ctl.factr", "scalar, function convergence tolerance factor. Convergence occurs when ``|f_k - f_{k+1}| < factr * machine_epsilon``. Use 1e12 for low accuracy, 1e7 for moderate accuracy (default), 1e1 for high accuracy."
            "ctl.pgtol", "scalar, projected gradient tolerance. Default = 1e-5."
            "ctl.bounds", "Kx2 matrix or 1x2 vector specifying parameter bounds. Column 1 contains lower bounds, column 2 contains upper bounds. If 1x2, applies to all parameters. Default = ``{ -1e300 1e300 }`` (effectively unbounded)."
            "ctl.printSummary", "scalar, print final summary. 0 = no (default), 1 = yes."
            "ctl.printEvery", "scalar, print progress every N iterations. 0 = never (default), N = every N iterations. Nelder-Mead requires 0; use printSummary for final output."
            "ctl.gradCheck", "0 (default) or 1; check the supplied gradient at x0 before optimization. Either the member or keyword set to 1 enables it."
            "ctl.gradCheckTol", "Positive finite relative tolerance for gradCheck. Default = 1e-4. Member only."

    :type ctl: struct

    :return out: an instance of a :class:`minimizeOut` structure. For an instance named *out*, the members are:

        .. list-table::
            :widths: auto

            * - out.x
              - Kx1 vector, solution values.
            * - out.fval
              - scalar, objective function value at solution.
            * - out.gradient
              - Kx1 vector, gradient at solution for L-BFGS-B. All entries are missing for Nelder-Mead; the optional starting-point gradient check does not populate this output.
            * - out.retcode
              - scalar, L-BFGS-B return code:

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

            * - out.restarts
              - scalar, number of Nelder-Mead restarts; 0 for L-BFGS-B.
            * - out.fSpread
              - scalar, last checked Nelder-Mead simplex objective spread; missing for L-BFGS-B.
            * - out.xSpread
              - scalar, last checked Nelder-Mead maximum coordinate spread; missing for L-BFGS-B.

        For Nelder-Mead, ``retcode`` is 0 when both simplex spreads are below their
        tolerances, 1 at the iteration limit, 2 at the evaluation limit, and 3
        when all simplex objective values are nonfinite. A setup error reported
        by the wrapper returns -1. Always inspect ``retcode`` and ``retmsg``.
        Spreads are checked before each simplex step. At an iteration-limit
        exit, the returned spreads can describe the simplex before the last
        step, and the returned point need not be the best objective evaluation
        from that last step. ``out.fval`` is the value at ``out.x``.
        A small simplex does not prove that the point is a local or global minimum.

    :rtype out: struct

The ``maxIters`` field returned by ``minimizeControlCreate`` now contains ``-1``
(the automatic marker), rather than ``1000``. Set an explicit numeric limit
before doing arithmetic on it: doubling the marker produces an error, not
2000 iterations, while adding 500 produces the valid explicit limit 499.
Comparisons against the unresolved marker also differ from comparisons against
1000. The input control is not updated with the resolved limit.

Nelder-Mead without derivatives
--------------------------------

Use Nelder-Mead for an unconstrained objective returning one real scalar.
It also accepts either two-return form described below, ignoring the gradient.
An f-only procedure is faster for Nelder-Mead than one that always computes both
f and g. With ``ind``, the objective can skip g. Data arguments are passed in
the same order as for L-BFGS-B.

::

    #include minimize.sdf
    struct minimizeControl ctl;
    struct minimizeOut out;
    ctl = minimizeControlCreate();
    out = minimize(&distance, 0|0, 3|-2, method="nelder-mead");
    print out.x out.fval;
    print out.retmsg;

    proc (1) = distance(x, target);
        retp(sumc((x - target)^2));
    endp;

The exact minimizer is ``3|-2`` with objective zero. The returned point is an
approximation controlled by both ``fTol`` and ``xTol``. Try different starting
points when the objective may have multiple minima. Parameter scaling matters:
``xTol`` is measured in the supplied coordinate units.

Nelder-Mead rejects finite bounds before evaluating the objective, with a
message directing you to L-BFGS-B. Keep the default unbounded ``ctl.bounds = {-1e300 1e300}``
or use the documented signed infinities ``{-__INFP __INFP}``. Each lower
endpoint must be exactly ``-1e300`` or ``-__INFP``; each upper endpoint must be
exactly ``1e300`` or ``__INFP``. You may repeat or mix these representations
for each parameter. Other finite intervals are rejected.
An objective returning NaN or infinity supplies a penalty value; an interpreter
error or user Stop ends the call immediately. These are different outcomes.
Evaluation counts include every objective call, including simplex initialization
and restarts. Iteration counts follow the simplex loop, including a loop that
terminates before taking a new step.

A complete example is installed as ``minimize_nelder_mead.e``.

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

    print "Solution:  " out.x';
    print "Objective: " out.fval;
    print "Iterations:" out.iterations;

::

    Solution:        0.99999999       0.99999998
    Objective:    1.3717997e-16
    Iterations:       37.000000

The optimizer finds the known minimum at (1, 1) with an objective value near zero in 37 iterations.

Example 2: With data arguments
++++++++++++++++++++++++++++++++++++++++++++

::

    rndseed 42;

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

    print "True coefficients:      " beta_true';
    print "Estimated coefficients: " out.x';

::

    True coefficients:             1.0000000        2.0000000       -1.0000000
    Estimated coefficients:       0.94044863        2.0263110       -1.0269490

Data arguments (*Y* and *X*) are passed directly through to the objective function without modification.

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
    ctl.bounds = { 0 10 };

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

    print "Solution: " out.x';

::

    Solution:        0.0000000        0.0000000        0.0000000

When ``ctl.bounds`` is a 1x2 vector, the same bounds apply to all parameters.

Example 4: Variable-specific bounds
++++++++++++++++++++++++++++++++++++++++++++

::

    proc (1) = myfunc(x);
        retp((x[1] - 2)^2 + (x[2] - 3)^2);
    endp;

    x0 = { 0, 0 };

    // x[1] in [0, inf), x[2] in [0, 2]
    struct minimizeControl ctl;
    ctl = minimizeControlCreate();
    ctl.bounds = { 0 1e300,    // x[1] >= 0
                   0     2 };  // x[2] in [0, 2]

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

    print "Solution: " out.x';

::

    Solution:        2.0000000        2.0000000

The unconstrained minimum is at (2, 3), but the bound ``x[2] <= 2`` forces the solution to (2, 2). When ``ctl.bounds`` is Kx2, each row specifies bounds for the corresponding parameter.

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

By default, L-BFGS-B computes the gradient by central differences. Each
gradient costs two objective evaluations per parameter. Parameter *i* is moved
by ``h = 6.0554544523933395e-6 * max(|x_i|, 1)`` (the cube root of machine
epsilon times the parameter's size) in each direction. Near a bound, the move
stops at the bound; if the objective is not finite on one side, a one-sided
difference is used. This step suits smooth objectives whose parameters vary on
a scale of about 1 or more. If a parameter near 0 matters on a much smaller
scale, rescale it or supply g.

You can supply your own gradient without a flag. The procedure's declared
argument and return counts select its form (``data`` denotes all supplied data
arguments):

.. list-table::
    :header-rows: 1
    :widths: auto

    * - Objective declaration
      - Behavior
    * - ``proc (1) = obj(x, data)``
      - Returns f only; L-BFGS-B computes numerical differences.
    * - ``proc (2) = obj(x, data, ind)``
      - Returns f and g as requested by the 2x1 vector ``ind``.
    * - ``proc (2) = obj(x, data)``
      - Always returns f and g; methods needing only f discard g.

``ind[1]`` asks for f and ``ind[2]`` asks for g, using OPTMT's indexes.
L-BFGS-B requests ``{1,1}``; Nelder-Mead requests ``{1,0}``. Unrequested
returns are ignored and may be empty. A requested gradient must be a finite,
real Kx1 vector (a scalar is accepted for one parameter). Wrong size, complex,
string, nonfinite or partly missing gradients return code 3 with missing
``out.fval`` and ``out.gradient``. Missing elements are not filled numerically.

::

    proc (2) = squared_error(b, y, X, ind);
        local e, f, g;
        e = y - X*b;
        f = {}; g = {};
        if ind[1]; f = e'e; endif;
        if ind[2]; g = -2*X'e; endif;
        retp(f, g);
    endp;

    out = minimize(&squared_error, b0, y, X, gradCheck=1);

A ``proc (2)`` declared with ``...`` always receives ``ind`` as its last dynamic
argument. Read it with ``dynargsGet(dynargsCount(), 0)``. For example, for
``obj(b, ...)`` with two data arguments, obtain the data with
``{ y, X } = dynargsGet(1|2, 0, 0);`` and call a fixed-argument helper as
``helper(b, y, X)``. Forwarding all of ``...`` would also forward ``ind``.
A ``proc (1)`` never receives ``ind``.

Other argument or return counts produce a setup error before the first call.
Pass every data argument: forgetting the last data argument of a two-return
objective can cause ``ind`` to be interpreted as that argument. ``printSummary``
names the detected form. Objectives cannot rely on keyword defaults; pass the
value as a data argument or use a keyword-free wrapper. Detection will not put
``ind`` into a parameter declared with a keyword default.

**Checking a supplied gradient:**

Set ``gradCheck=1`` or ``ctl.gradCheck=1`` to check g at x0 before either solver
runs. The check makes one g-only request, one f-only request at x0, and two
f-only requests per free parameter,
then prints the supplied g, central-difference g and relative difference.
The always-both form computes both outputs on each of these calls. A one-return
objective cannot be checked.

The check fails with code 3 if any absolute difference exceeds
``ctl.gradCheckTol * max(1, |numerical g|)``. The default tolerance is ``1e-4``;
it is a control member, not a keyword. On failure, ``out.retmsg`` names the worst element and
returns missing f and g without starting optimization. A nonfinite numerical
difference also fails the check. L-BFGS-B checks the starting point after
projecting it into the supplied bounds. Differences stop at bounds, as in the
solver; if one side is nonfinite, a finite one-sided difference uses f(x0).
A fixed parameter has numerical derivative zero. If neither direction is usable,
the error names the element. Calls made by the check are included in ``out.fnEvals``.

If an L-BFGS-B line search fails, ``out.retcode`` is 2 (abnormal termination).
For a supplied gradient, the message suggests trying ``gradCheck``.

**Convergence criteria:**

The algorithm terminates when either:

1. The function value change is small: ``|f_k - f_{k+1}| < factr * eps``
2. The projected gradient is small: ``max|g_i| < pgtol``
3. Maximum iterations is reached

**Starting point:**

If the starting point *x0* violates any bounds, it is automatically projected
into the feasible region before optimization begins.

.. seealso:: Functions :func:`minimizeControlCreate`, :func:`sqpSolveMT`, :func:`QNewton`, :func:`optmt`

