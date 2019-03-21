
intquad2
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: intquad2(&f, xl, yl,  ...)

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: scalar

    :param xl: the limits of x.
    :type xl: 2x1 or 2xN matrix

    :param yl: the limits of y.
    :type yl: 2x1 or 2xN matrix

    :param ...: a variable number of extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: Optional

    :returns: y (*TODO*), Nx1 vector of the estimated integral(s) of f(x,y)
        evaluated between the limits given by xl and yl.

Examples
----------------

Basic example
+++++++++++++

::

    //Define function to be integrated
    proc f(x,y);
       retp(x .* sin(x + y));
    endp;
     
    //Limits of integration
    xlim = { 1, 0 };
    ylim = { 1, 0 };
     
    //Calculate integral
    ans = intquad2(&f, xlim, ylim);

After the code above, ans should equal:

::

    0.42892501

Multiple integration limits
+++++++++++++++++++++++++++

::

    //Define function to be integrated
    proc (1) = myProc(x,y);
       retp(x .* sin(x + y));
    endp;
    
    //Define multiple integration limits
    xlim = {  1  0.5,
            0.5    0 };
    
    ylim = {  1  0.5,
            0.5  0.3 };
    
    //Calculate integrals
    ans = intquad2(&myProc, xlim, ylim);

This will integrate the function:

::

    myProc(x) = x.*sin(x+y)

x
y
x
y
The returned variable, ans should be equal to:

::

    0.18352849 
    0.016593029

Extra arguments to function
+++++++++++++++++++++++++++

::

    //Define function to be integrated that takes an additional argument
    proc f(x,y,a);
       retp(x .* sin(a .* x + y));
    endp;
     
    //Limits of integration
    xlim = { 1, 0 };
    ylim = { 1, 0 };
    
    
    //Assign extra scalar argument
    a = pi/2;
     
    //Calculate integral
    ans = intquad2(&f, xlim, ylim, a);

After the code above, ans should equal:

::

    0.44737953

Remarks
+++++++

The user-defined function f must return a vector of function values.
intquad2 will pass to user-defined functions a vector or matrix for x
and y and expect a vector or matrix to be returned. Use .\* and ./
instead of \* and /.

intquad2 will expand scalars to the appropriate size. This means that
functions can be defined to return a scalar constant. If users write
their functions incorrectly (using \* instead of .\*, for example),
intquad2 may not compute the expected integral, but the integral of a
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

.. seealso:: Functions :func:`intquad1`, :func:`intquad3`, :func:`intsimp`, :func:`intgrat2`, :func:`intgrat3`

intergrate 2-dimensional function user defined rectangular region


Global Input
------------

+-----------------+-----------------------------------------------------+
| \_intord        | scalar, the order of the integration. The larger    |
|                 | \_intord, the more precise the final result will    |
|                 | be. \_intord may be set to 2, 3, 4, 6, 8, 12, 16,   |
|                 | 20, 24, 32, 40. Default = 12.                       |
+-----------------+-----------------------------------------------------+

