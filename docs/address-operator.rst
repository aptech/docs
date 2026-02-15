
address-operator
==============================================

Purpose
----------------

Returns the address of a procedure or function for use with function pointers.

Format
----------------

::

    fptr = &procname

Parameters
----------------

    :param procname: Name of a procedure or function.
    :type procname: procedure name

Returns
----------------

    :return fptr: Pointer to the procedure that can be passed to other functions.

    :rtype fptr: function pointer

Examples
----------------

Basic Function Pointer
++++++++++++++++++++++

::

    // Define a procedure
    proc (1) = mySquare(x);
        retp(x .* x);
    endp;

    // Get pointer to procedure
    fptr = &mySquare;

    // Use with local declaration
    local fptr:proc;

    // Call through pointer
    y = fptr(5);

::

    y =    25.000000

Passing to Optimization Functions
+++++++++++++++++++++++++++++++++

::

    // Define objective function
    proc (1) = objective(x);
        retp(x[1]^2 + x[2]^2);
    endp;

    // Pass to optimizer
    x0 = { 1, 1 };
    { x, fval, retcode } = sqpSolveMT(&objective, x0);

Selecting Functions Dynamically
+++++++++++++++++++++++++++++++

::

    proc (1) = add(a, b);
        retp(a + b);
    endp;

    proc (1) = mult(a, b);
        retp(a * b);
    endp;

    // Choose function at runtime
    op = 1;
    if op == 1;
        fn = &add;
    else;
        fn = &mult;
    endif;

    local fn:proc;
    result = fn(3, 4);

::

    result =    7.0000000

Remarks
-------

- Function pointers allow procedures to be passed as arguments to other procedures.
- The pointer variable must be declared with ``local varname:proc`` before being called.
- Commonly used with optimization routines, numerical integration, and callback functions.
- The ``&`` must immediately precede the procedure name with no spaces.

.. seealso:: Keywords ``proc``, ``local``
