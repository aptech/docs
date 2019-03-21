
intsimp
==============================================

Purpose
----------------

Integrates a specified function using Simpson's method with end correction. A single integral is computed in one function call.

Format
----------------
.. function:: intsimp(&f, xl, tol)

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: TODO

    :param xl: the limits of x.
        The first element is the upper limit and the second element is the lower limit.
    :type xl: 2x1 vector

    :param tol: 
    :type tol: The tolerance to be used in testing for convergence

    :returns: y (*TODO*), The estimated integral of f(x) between xl[1] and xl[2].

Examples
----------------

::

    proc f(x);
      retp(sin(x));
    endp;
     
    let xl = { 1, 0 };
     
    y = intsimp(&f,xl,1e-8);
    print y;

The code above, returns the following:

::

    0.45969769

This will integrate the function between 0 and 1.

Source
------

intsimp.src

.. seealso:: Functions :func:`intquad1`, :func:`intquad2`, :func:`intquad3`, :func:`intgrat2`, :func:`intgrat3`

intergrate Simpson
