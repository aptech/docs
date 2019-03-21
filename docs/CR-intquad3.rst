
intquad3
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: intquad3(&f, xl, yl, zl, ...)

    :param &f: pointer to the procedure containing the
        function to be integrated.  f is a function of (x, y, z).
    :type &f: scalar

    :param xl: the limits of x.
    :type xl: 2x1 or 2xN matrix

    :param yl: the limits of y.
    :type yl: 2x1 or 2xN matrix

    :param zl: the limits of  z.
    :type zl: 2x1 or 2xN matrix

    :param ...: a variable number of extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: Optional

    :returns: y (*TODO*), Nx1 vector of the estimated integral(s) of f(x,y,z)
        evaluated between the limits given by  xl, yl, and  zl.

Examples
----------------

Basic example
+++++++++++++

::

    //Define function to integrate
    proc f(x,y,z);
       retp(sqrt(x.^2 +  y.^2  +  z.^2));
    endp;
     
    //Define limits of integration
    xlim = { 1, 0 };
    ylim = { 1, 0 };
    zlim = { 3, 0 };
     
    //Calculate integral
    ans = intquad3(&f,xlim, ylim, zlim);

After the code above, ans should equal:

::

    5.2994691

Passing extra arguments
+++++++++++++++++++++++

::

    //Define function to integrate which takes an additional argument
    proc f(x,y,z,a);
       retp(sqrt(a .* x.^2 +  y.^2  +  z.^2));
    endp;
     
    //Define limits of integration
    xlim = { 1, 0 };
    ylim = { 1, 0 };
    zlim = { 3, 0 };
    
    //Define extra scalar argument
    a = 3.14;
     
    //Calculate integral, passing in extra scalar argument
    ans = intquad3(&f,xlim, ylim, zlim, a);

After the code above, ans should equal:

::

    5.8969356

Multiple limits of integration
++++++++++++++++++++++++++++++

::

    //Define function to integrate
    proc f(x,y,z);
       retp(sqrt(x.^2 +  y.^2  +  z.^2));
    endp;
     
    //Define 3 sets of limits of integration
    xlim = { 1, 0 };
    ylim = { 1, 0 };
    zlim = { 1 2 3, 
             0 0 0 };
     
    //Calculate integrals
    ans = intquad3(&f,xlim, ylim, zlim);

This will integrate the function f(x) = x*y*z over 3 sets of limits, since
zlim is defined to be a 2x3 matrix. The value of  ans should be:

::

    0.96059195 
     2.6692443 
     5.2994691

Remarks
-------

The user-defined function f must return a vector of function values.
intquad3 will pass to the user-defined function a vector or matrix for
x, y and z and expect a vector or matrix to be returned. Use .\* and ./
instead of \* and /.

intquad3 will expand scalars to the appropriate size. This means that
functions can be defined to return a scalar constant. If users write
their functions incorrectly (using \* instead of .\*, for example),
intquad3 may not compute the expected integral, but the integral of a
constant function.

To integrate over a region which is bounded by functions, rather than
just scalars, use intgrat2 or intgrat3.

Source
------

integral.src

Globals
+++++++

\_intord, \_intq12, \_intq16, \_intq2, \_intq20, \_intq24, \_intq3,
\_intq32, \_intq4, \_intq40, \_intq6, \_intq8

.. seealso:: Functions :func:`intquad1`, :func:`intquad2`, :func:`intsimp`, :func:`intgrat2`, :func:`intgrat3`

intergrate 3-dimensional function user defined rectangular region


Global Input
------------

+-----------------+-----------------------------------------------------+
| \_intord        | scalar, the order of the integration. The larger    |
|                 | \_intord, the more precise the final result will    |
|                 | be. \_intord may be set to 2, 3, 4, 6, 8, 12, 16,   |
|                 | 20, 24, 32, 40.                                     |
|                 | Default = 12.                                       |
+-----------------+-----------------------------------------------------+

