
besselj
==============================================

Purpose
----------------

Computes a Bessel function of the first kind, :math:`J_n(x)`.

Format
----------------
.. function:: y = besselj(n, x)

    :param n: The order of the Bessel function. Non-integers will be truncated to an integer.
    :type n: NxK matrix or P-dimensional array where the last two dimensions are NxK

    :param x:
    :type x: LxM matrix or P-dimensional array where the last two dimensions are LxM, ExE conformable with n

    :returns: y, max(N,L) by max(K,M) matrix or P-dimensional array where the last two dimensions are max(N, L) by max(K, M)

Examples
----------------

::

    // Create the sequence 0.1, 0.2, 0.3,...,19.9
    x = seqa(0, 0.1, 200);

    // Calculate a first order Bessel function
    n = 1;
    y0 = besselj(n, x);

    // Calculate the first and second order Bessel function
    n = { 1 2 };
    y = besselj(n, x);

    /*
    ** Plot the output of the first and second order Bessel
    ** functions
    */
    plotXY(x, y);

In the code above, the calculation of both the first and second order Bessel functions assigns the
return from the first order calculation to be the first column of *y* and the return from the calculation
of the second order function to be the second column of *y*.

The :func:`plotXY` function treats each incoming column as a separate line.

.. seealso:: Functions :func:`bessely`, :func:`mbesseli`, :func:`besselk`
