
hessp, hesscplx
==============================================

Purpose
----------------

Computes the matrix of second partial derivatives (Hessian matrix) of a function defined as a procedure. hesscplx allows for
complex arguments.

Format
----------------
.. function:: hessp(&f, x0)

    :param &f: pointer to a single-valued function f(x),
        defined as a procedure, taking a single Kx1 vector argument (f: Kx1 → 1x1);  f(x) may be defined
        in terms of global arguments in addition to x.
    :type &f: TODO

    :param x0: 
    :type x0: Kx1 vector specifying the point at which the Hessian of f(x) is to be computed

    :returns: h (*TODO*), KxK matrix of second derivatives of  f with respect to x at x0; this matrix will be symmetric.

Examples
----------------

::

    x = { 1, 2, 3 };
     
    proc g(b);
    retp( exp(x'b));
    endp;
     
    b0 = { 3, 2, 1 };
    h = hessp(&g,b0);

The resulting matrix of second partial derivatives of g(b) evaluated at b=b0 is:

::

    22026.865  44053.686  66080.596
    h =  44053.686  88107.753 132161.059
         66080.596 132161.059 198240.695

Source
++++++

hessp.src

.. seealso:: Functions :func:`gradp`, :func:`gradcplx`

gradient Hessian derivative complex argument
