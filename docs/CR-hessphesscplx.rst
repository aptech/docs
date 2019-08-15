
hessp, hesscplx
==============================================

Purpose
----------------

Computes the matrix of second partial derivatives (Hessian matrix) of a function defined as a procedure. :func:`hesscplx` allows for
complex arguments.

Format
----------------
.. function:: h = hessp(&f, x0)

    :param &f: pointer to a single-valued function :math:`f(x)`,
        defined as a procedure, taking a single Kx1 vector argument (f: :math:`Kx1 → 1x1`); :math:`f(x)` may be defined
        in terms of global arguments in addition to *x*.
    :type &f: function pointer

    :param x0: the point at which the Hessian of :math:`f(x)` is to be computed
    :type x0: Kx1 vector

    :return h: Second derivatives of *f* with respect to *x* at *x0*; this matrix will be symmetric.

    :rtype h: KxK matrix

Remarks
-------

This procedure requires :math:`K*(K+1)/2` function evaluations. Thus if *K* is
large, it may take a long time to compute the Hessian matrix.

No more than 3-4 digit accuracy should be expected from this function,
though it is possible for greater accuracy to be achieved with some
functions.

It is important that the function be properly scaled, in order to obtain
greatest possible accuracy. Specifically, scale it so that the first
derivatives are approximately the same size. If these derivatives differ
by more than a factor of 100 or so, the results can be meaningless.


Examples
----------------

::

    // X matrix
    x = { 1, 2, 3 };

    proc g(b);
      retp( exp(x'b));
    endp;

    // Parameter startvalues
    b0 = { 3, 2, 1 };

    // Compute Hessian
    h = hessp(&g, b0);

The resulting matrix of second partial derivatives of :math:`g(b)` evaluated at :math:`b = b0` is:

::

         22026.865  44053.686  66080.596
    h =  44053.686  88107.753 132161.059
         66080.596 132161.059 198240.695

Source
------

hessp.src

.. seealso:: Functions :func:`gradp`, :func:`gradcplx`
