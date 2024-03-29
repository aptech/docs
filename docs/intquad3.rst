
intquad3
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: y = intquad3(&f, xlims, ylims, zlims, ...)

    :param &f: pointer to the procedure containing the function to be integrated. *f* is a function of :math:`(x, y, z)`.
    :type &f: scalar

    :param xlims: the limits of *x*.
    :type xlims: 2x1 or 2xN matrix

    :param ylims: the limits of *y*.
    :type ylims: 2x1 or 2xN matrix

    :param zlims: the limits of *z*.
    :type zlims: 2x1 or 2xN matrix

    :param ...: Optional. A variable number of extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: any

    :return y: of the estimated integral(s) of :math:`f(x,y,z)` evaluated between the limits given by *xl*, *yl*, and *zl*.

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

    // Define function to integrate
    proc f(x, y, z);
       retp(sqrt(x.^2 +  y.^2  +  z.^2));
    endp;

    // Define limits of integration
    xlims = { 1, 0 };
    ylims = { 1, 0 };
    zlims = { 3, 0 };

    // Calculate integral
    ans = intquad3(&f, xlims, ylims, zlims);

After the code above, *ans* should equal:

::

    5.2994691

Passing extra arguments
+++++++++++++++++++++++

::

    // Define function to integrate which takes an additional argument
    proc f(x, y, z, a);
       retp(sqrt(a .* x.^2 +  y.^2  +  z.^2));
    endp;

    // Define limits of integration
    xlims = { 1, 0 };
    ylims = { 1, 0 };
    zlims = { 3, 0 };

    // Define extra scalar argument
    a = 3.14;

    // Calculate integral, passing in extra scalar argument
    ans = intquad3(&f, xlims, ylims, zlims, a);

After the code above, *ans* should equal:

::

    5.8969356

Multiple limits of integration
++++++++++++++++++++++++++++++

::

    // Define function to integrate
    proc f(x, y, z);
       retp(sqrt(x.^2 +  y.^2  +  z.^2));
    endp;

    // Define 3 sets of limits of integration
    xlims = { 1, 0 };
    ylims = { 1, 0 };
    zlims = { 1 2 3,
             0 0 0 };

    // Calculate integrals
    ans = intquad3(&f, xlims, ylims, zlims);

This will integrate the function :math:`f(x) = x*y*z` over 3 sets of limits, since
*zlim* is defined to be a 2x3 matrix. The value of *ans* should be:

::

    0.96059195
     2.6692443
     5.2994691

Remarks
-------

The user-defined function *f* must return a vector of function values.
:func:`intquad3` will pass to the user-defined function a vector or matrix for
*x*, *y* and *z* and expect a vector or matrix to be returned. Use ``.*`` and ``./``
instead of ``*`` and ``/``.

:func:`intquad3` will expand scalars to the appropriate size. This means that
functions can be defined to return a scalar constant. If users write
their functions incorrectly (using ``*`` instead of ``.*,`` for example),
:func:`intquad3` may not compute the expected integral, but the integral of a
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

.. seealso:: Functions :func:`intquad1`, :func:`intquad2`, :func:`intsimp`, :func:`intgrat2`, :func:`intgrat3`
