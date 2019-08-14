
intsimp
==============================================

Purpose
----------------

Integrates a specified function using Simpson's method with end correction. A single integral is computed in one function call.

Format
----------------
.. function:: intsimp(&f, xlims, tol)

    :param &f: pointer to the procedure containing the function to be integrated.
    :type &f: scalar

    :param xlims: the limits of *x*.
        The first element is the upper limit and the second element is the lower limit.
    :type xlims: 2x1 vector

    :param tol: The tolerance to be used in testing for convergence
    :type tol: scalar

    :returns: **y** (*scalar*) - The estimated integral of :math:`f(x)` between :math:`xlims[1]` and :math:`xlims[2]`.

Examples
----------------

::

    // Function to be integrated
    proc f(x);
        retp(sin(x));
    endp;

    // Define limits
    xlims = { 1, 0 };

    // Integrate using Simpson's method
    y = intsimp(&f, xl, 1e-8);
    print y;

The code above returns the following:

::

    0.45969769

This will integrate the function between 0 and 1.

Source
------

intsimp.src

.. seealso:: Functions :func:`intquad1`, :func:`intquad2`, :func:`intquad3`, :func:`intgrat2`, :func:`intgrat3`
