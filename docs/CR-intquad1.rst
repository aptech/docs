
intquad1
==============================================

Purpose
----------------

Integrates a specified function using Gauss-Legendre quadrature. A suite of upper and lower bounds may be calculated in one procedure call.

Format
----------------
.. function:: intquad1(&f, xl,  ...)

    :param &f: pointer to the procedure containing the function to be integrated. This must be a function of x.
    :type &f: scalar

    :param xl: the limits of x.
        The first row is the upper limit and the second
        row is the lower limit. N integrations are
        computed.
    :type xl: 2xN matrix

    :param ...: a variable number of extra scalar arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: Optional

    :returns: y (*TODO*), Nx1 vector of the estimated integral(s) of f(x)
        evaluated between the limits given by  xl.

Remarks
-------

The user-defined function f must return a vector of function values.
intquad1 will pass to the user-defined function a vector or matrix for x
and expect a vector or matrix to be returned. Use the .\* and ./ instead
of \* and /.


Examples
----------------

Basic example
+++++++++++++

This will integrate the function f(x) = x*sin(x) between 0 and 1.
Note the use of the .* instead of *.

::

    //Define function to be integrated
    proc f(x);
       retp(x.*sin(x));
    endp;
     
    //Limits of integration
    xlim = { 1, 0 };
    
    //Calculate integral
    y = intquad1(&f,xlim);

After the code above, y should equal:

::

    0.30116868

Passing in additional arguments
+++++++++++++++++++++++++++++++

::

    //Define function to be integrated
    //with a second input
    proc f(x, a);
       retp(x.*sin(x .* a));
    endp;
    
    //Create additional scalar argument 'a'
    a = 3.14; 
    
    //Limits of integration
    xlim = { 1, 0 };
    
    //Calculate integral, passing in extra input
    //'a' as the final input to 'intquad1'
    y = intquad1(&f, xlim, a);

After the code above, y should equal:

::

    0.31863247

Source
------

integral.src

Globals
+++++++

\_intord, \_intq12, \_intq16, \_intq2, \_intq20, \_intq24, \_intq3,
\_intq32, \_intq4, \_intq40, \_intq6, \_intq8

.. seealso:: Functions :func:`intsimp`, :func:`intquad2`, :func:`intquad3`, :func:`intgrat2`, :func:`intgrat3`

intergrate 1-dimensional function
