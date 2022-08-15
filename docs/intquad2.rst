
intquad2
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: y = intquad2(&f, xlims, ylims[, ...])

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: scalar

    :param xlims: the limits of *x*.
    :type xlims: 2x1 or 2xN matrix

    :param ylims: the limits of *y*.
    :type ylims: 2x1 or 2xN matrix

    :param ...: Optional. A variable number of extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: any

    :return y: the estimated integral(s) of :math:`f(x,y)` evaluated between the limits given by *xl* and *yl*.

    :rtype y: Nx1 vector

Global Input
------------

.. data:: _intord

    scalar, the order of the integration. The larger \_intord, the more precise the final result will be. \_intord may be set to 2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40.

    Default = 12.

Examples
----------------

Basic example
+++++++++++++

::

    // Define function to be integrated
    proc f(x, y);
       retp(x .* sin(x + y));
    endp;

    // Limits of integration
    xlims = { 1, 0 };
    ylims = { 1, 0 };

    // Calculate integral
    ans = intquad2(&f, xlims, ylims);

After the code above, *ans* should equal:

::

    0.42892501

Multiple integration limits
+++++++++++++++++++++++++++

::

    // Define function to be integrated
    proc (1) = myProc(x, y);
       retp(x .* sin(x + y));
    endp;

    // Define multiple integration limits
    xlims = {  1  0.5,
            0.5    0 };

    ylims = {  1  0.5,
            0.5  0.3 };

    // Calculate integrals
    ans = intquad2(&myProc, xlims, ylims);

This will integrate the function:

::

    myProc(x) = x.*sin(x+y)

between *x* = 0 and 0.5, and between *y* = 0.3 and 0.5 as well as between *x* = 0.5 and 1, and between *y* = 0.5 and 1.

The returned variable, *ans* should be equal to:

::

    0.18352849
    0.016593029

Extra arguments to function
+++++++++++++++++++++++++++

::

    // Define function to be integrated that takes an additional argument
    proc f(x, y, a);
       retp(x .* sin(a .* x + y));
    endp;

    // Limits of integration
    xlims = { 1, 0 };
    ylims = { 1, 0 };

    // Assign extra scalar argument
    a = pi/2;

    // Calculate integral
    ans = intquad2(&f, xlims, ylims, a);

After the code above, *ans* should equal:

::

    0.44737953

Remarks
-------

The user-defined function *f* must return a vector of function values.
:func:`intquad2` will pass to user-defined functions a vector or matrix for *x*
and *y* and expect a vector or matrix to be returned. Use ``.*`` and ``./``
instead of ``*`` and ``/``.

:func:`intquad2` will expand scalars to the appropriate size. This means that
functions can be defined to return a scalar constant. If users write
their functions incorrectly (using ``*`` instead of ``.*,`` for example),
:func:`intquad2` may not compute the expected integral, but the integral of a
constant function.

To integrate over a region which is bounded by functions, rather than
just scalars, use :func:`intgrat2` or :func:`intgrat3`.

Source
------

integral.src

Globals
------------

*_intord*, *_intq12*, *_intq16*, *_intq2*, *_intq20*, *_intq24*, *_intq3*,
*_intq32*, *_intq4*, *_intq40*, *_intq6*, *_intq8*

.. seealso:: Functions :func:`intquad1`, :func:`intquad3`, :func:`intsimp`, :func:`intgrat2`, :func:`intgrat3`
