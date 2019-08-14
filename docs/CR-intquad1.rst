
intquad1
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: y = intquad1(&f, lims[,  ...])

    :param &f: pointer to the procedure containing the function to be integrated. This must be a function of *x*.
    :type &f: scalar

    :param lims: the limits of *x*. The first row is the upper limit and the second
        row is the lower limit. *N* integrations are computed.
    :type lims: 2xN matrix

    :param ...: Optional. Extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: any

    :returns: **y** (*Nx1 vector*) - the estimated integral(s) of :math:`f(x)` evaluated between the limits given by *lims*.

Global Input
------------

.. data:: \_intord

    scalar, the order of the integration. The larger \_intord, the more precise the final result will be. \_intord may be set to 2, 3, 4, 6, 8, 12, 16, 20, 24, 32, 40.

    Default = 12.


Remarks
-------

The user-defined function *f* must return a vector of function values.
:func:`intquad1` will pass to the user-defined function a vector or matrix for *x*
and expect a vector or matrix to be returned. Use the ``.*`` and ``./`` instead
of ``*`` and ``/``.

Examples
----------------

Basic example
+++++++++++++

This will integrate the function :math:`f(x) = x*sin(x)` between 0 and 1.
Note the use of the ``.*`` instead of ``*``.

::

    // Define function to be integrated
    proc f(x);
       retp(x.*sin(x));
    endp;

    // Limits of integration
    lims = { 1, 0 };

    // Calculate integral
    y = intquad1(&f, lims);

After the code above, *y* should equal:

::

    0.30116868

Passing in additional arguments
+++++++++++++++++++++++++++++++

::

    /*
    ** Define function to be integrated
    ** with a second input
    */
    proc f(x, a);
       retp(x.*sin(x .* a));
    endp;

    // Create additional scalar argument 'a'
    a = 3.14;

    // Limits of integration
    lims = { 1, 0 };

    /*
    ** Calculate integral, passing in extra input
    ** 'a' as the final input to 'intquad1'
    */
    y = intquad1(&f, lims, a);

After the code above, *y* should equal:

::

    0.31863247

Source
------

integral.src

Globals
------------

*_intord*, *_intq12*, *_intq16*, *_intq2*, *_intq20*, *_intq24*, *_intq3*,
*_intq32*, *_intq4*, *_intq40*, *_intq6*, *_intq8*

.. seealso:: Functions :func:`intsimp`, :func:`intquad2`, :func:`intquad3`, :func:`intgrat2`, :func:`intgrat3`
