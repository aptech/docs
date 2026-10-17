
minimizeControlCreate
==============================================

Purpose
----------------

Creates a :class:`minimizeControl` structure with default values for use with :func:`minimize`.

Format
----------------
.. function:: ctl = minimizeControlCreate()

    :return ctl: an instance of a :class:`minimizeControl` structure with the following default values:

        .. csv-table::
            :widths: auto

            "ctl.method", "``lbfgsb``; use ``nelder-mead`` for an unconstrained scalar objective without gradients."
            "ctl.fTol", "1e-10, Nelder-Mead objective spread tolerance."
            "ctl.xTol", "1e-5, Nelder-Mead coordinate spread tolerance."
            "ctl.maxEvals", "-1, automatic Nelder-Mead evaluation budget: 200 times the parameter count. 0 disables this limit; positive values set an explicit limit checked between simplex steps. Limits above 2,147,483,647, including infinity, are treated as 2,147,483,647, which no practical run reaches."
            "ctl.maxRestarts", "3, maximum Nelder-Mead stall restarts."
            "ctl.stallLimit", "0, use 50 times the parameter count for the Nelder-Mead stall interval."
            "ctl.initialStep", "0.05, Nelder-Mead relative initial displacement."
            "ctl.zeroStep", "0.00025, initial displacement for near-zero starting coordinates."
            "ctl.m", "10, number of L-BFGS corrections to store."
            "ctl.maxIters", "-1, automatic maximum iterations: 200 times the parameter count for Nelder-Mead, 1000 for L-BFGS-B. Positive whole numbers set an explicit limit. Limits above 2,147,483,647, including infinity, are treated as 2,147,483,647, which no practical run reaches. Other values return a setup error before evaluation. The returned ``maxIters`` reads -1 until you set it; see the note on ``maxIters`` arithmetic and comparisons in :func:`minimize`."
            "ctl.factr", "1e7, function convergence tolerance factor (moderate accuracy)."
            "ctl.pgtol", "1e-5, projected gradient tolerance."
            "ctl.bounds", "``{ -1e300 1e300 }``, 1x2 bounds matrix (effectively unbounded)."
            "ctl.printSummary", "0, no final summary."
            "ctl.printEvery", "0, no iteration output. Required for Nelder-Mead."

    :rtype ctl: struct

Examples
----------------

Example 1: Use defaults
++++++++++++++++++++++++++++++++++++++++++++

::

    struct minimizeControl ctl;
    ctl = minimizeControlCreate();

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

Example 2: Modify settings
++++++++++++++++++++++++++++++++++++++++++++

::

    struct minimizeControl ctl;
    ctl = minimizeControlCreate();

    // Set bounds: all parameters in [0, 100]
    ctl.bounds = { 0 100 };

    // High accuracy
    ctl.factr = 1e1;

    // Print final summary
    ctl.printSummary = 1;

    // Print progress every 10 iterations
    ctl.printEvery = 10;

    struct minimizeOut out;
    out = minimize(&myfunc, x0, ctl);

Remarks
-------

For L-BFGS-B, the ``factr`` parameter controls the convergence tolerance for function values.
The algorithm terminates when the reduction in the objective function is
within ``factr * machine_epsilon`` of the previous value.

Common settings for ``factr``:

- **1e12**: Low accuracy, fast convergence
- **1e7**: Moderate accuracy (default), good balance
- **1e1**: High accuracy, more iterations

The ``pgtol`` parameter controls the tolerance on the projected gradient.
Smaller values require the gradient to be closer to zero at convergence.

For Nelder-Mead, both ``fTol`` and ``xTol`` must be satisfied. Bounds are not
supported. See :func:`minimize` for stopping codes and the evaluation-limit
semantics. L-BFGS-B settings ``m``, ``factr`` and ``pgtol`` do not apply to
Nelder-Mead.

The automatic budgets are resolved by :func:`minimize` after the method and
number of parameters are known. For example, a 20-parameter Nelder-Mead call
defaults to 4,000 iterations and 4,000 objective evaluations. Each limit is
independent: setting ``maxIters`` leaves the automatic evaluation limit active.
To use only an explicit iteration limit, also set ``maxEvals = 0``. Reaching
either limit is reported separately from convergence.

.. seealso:: Functions :func:`minimize`

