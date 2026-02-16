
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

            "ctl.m", "10, number of L-BFGS corrections to store."
            "ctl.maxIters", "1000, maximum number of iterations."
            "ctl.factr", "1e7, function convergence tolerance factor (moderate accuracy)."
            "ctl.pgtol", "1e-5, projected gradient tolerance."
            "ctl.bounds", "``{ -1e300 1e300 }``, 1x2 bounds matrix (effectively unbounded)."
            "ctl.printSummary", "0, no final summary."
            "ctl.printEvery", "0, no iteration output."

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

The ``factr`` parameter controls the convergence tolerance for function values.
The algorithm terminates when the reduction in the objective function is
within ``factr * machine_epsilon`` of the previous value.

Common settings for ``factr``:

- **1e12**: Low accuracy, fast convergence
- **1e7**: Moderate accuracy (default), good balance
- **1e1**: High accuracy, more iterations

The ``pgtol`` parameter controls the tolerance on the projected gradient.
Smaller values require the gradient to be closer to zero at convergence.

.. seealso:: Functions :func:`minimize`

