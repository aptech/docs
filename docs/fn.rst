fn
==============================================

Purpose
----------------

Defines a one-line function.

.. _fn:
.. index:: fn

Format
----------------

::

    fn name(arg1, arg2, ...) = expression;

Parameters
----------------

:name: the name of the function.

:arg1, arg2, ...: the names of the function's arguments. Inside *expression* they stand for the values the function is called with.

:expression: one expression that gives the function's single return value.

Examples
----------------

Basic use
+++++++++

::

    fn area(r) = pi*r*r;
    a = area(4);
    print a;

The code above prints:

::

    50.265482

An fn can take more than one argument:

::

    fn h(x, y) = x + 2*y;
    print h(1, 2);

::

    5.0000000

An fn inside a procedure
++++++++++++++++++++++++

An fn defined inside a procedure can use that procedure's local variables and arguments. It reads their value when the fn is called, not when it is defined:

::

    proc (2) = scaled(x);
        local s, a1, a2;

        fn f(z) = s * z;

        s = 2;
        a1 = f(x);

        s = 10;
        a2 = f(x);

        retp(a1, a2);
    endp;

    { a1, a2 } = scaled(3);
    print a1;
    print a2;

::

    6.0000000
    30.000000

Passing an fn to another procedure
++++++++++++++++++++++++++++++++++

Pass an fn by pointer to a procedure that takes a function, such as :func:`gradp`. It still uses the local variables of the procedure that defined it:

::

    proc (1) = slope(b0);
        local c;
        c = 3;

        // Derivative of 3*b^2 is 6*b
        fn sq(b) = c * b^2;

        retp(gradp(&sq, b0));
    endp;

    print slope(2);

::

    12.000000

Remarks
-------

Call an fn the same way as a procedure. It returns one value.

An fn defined inside a procedure can use that procedure's local variables and arguments, and it reads their current value each time it is called. You can pass such an fn with ``&`` to procedures that take a function argument, for example :func:`gradp`, :func:`hessp`, :func:`intquad1` and the optimizers, and it still sees the variables of the procedure that defined it.

**fn names are global.** If two procedures, keywords or your main program define an fn with the same name, every call runs the definition compiled last. In the code below, ``p1(1)`` returns 100, not 2, because the definition in ``p2`` replaces the one in ``p1``:

::

    proc (1) = p1(x);
        fn g(z) = z + 1;
        retp(g(x));
    endp;

    proc (1) = p2(x);
        fn g(z) = z * 100;
        retp(g(x));
    endp;

GAUSS prints a warning when it compiles a second fn with a name that is already in use, for example::

    Warning: fn g in proc p2 replaces fn g defined in proc p1; fn names are global.

Give each fn its own name, for example ``g1`` and ``g2``.

Saved programs (``.gcg`` files) made with GAUSS 26 or earlier that pass an fn using a procedure's local variables to another procedure must be recompiled with GAUSS 27.

.. seealso:: `proc`, `keyword`, :func:`gradp`, :func:`hessp`
