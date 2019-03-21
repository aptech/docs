
gradp, gradcplx
==============================================

Purpose
----------------

Computes the gradient vector or matrix (Jacobian) of a vector-valued function that has been defined in a
procedure. Single-sided (forward difference) gradients are computed. gradcplx allows for
complex arguments. 

Format
----------------
.. function:: gradp(&f, x0) 
			  gradcplx(&f, x0)

    :param &f: a pointer to a vector-valued function (f: Kx1 → Nx1)
        defined as a procedure. It is acceptable for f(x)
        to have been defined in terms of global
        arguments in addition to x, and thus f can
        return an Nx1 vector:
        proc f(x);
        retp( exp(x.*b));
        endp;
    :type &f: TODO

    :param x0: 
    :type x0: Kx1 vector of points at which to compute gradient

    :returns: g (*NxK matrix*), containing the gradients of f with
        respect to the variable x at x0.

Remarks
-------

gradp will return a row for every row that is returned by f. For
instance, iff returns a scalar result, then gradp will return a 1xK row
vector. This allows the same function to be used regardless of N, where
N is the number of rows in the result returned byf. Thus, for instance,
gradp can be used to compute the Jacobian matrix of a set of equations.


Examples
----------------

::

    proc myfunc(x);
       retp(x .* 2 .* exp( x .* x ./ 3 ));
    endp;
    
    x0 = 2.5|3.0|3.5;
    y = gradp(&myfunc,x0);

After the code above, y is equal to:

::

    82.989017       0.00000000       0.00000000
    0.00000000        281.19753       0.00000000
    0.00000000       0.00000000        1087.9541

It is a 3x3 matrix because we are passing it 3 arguments and myfunc returns 3 results when we do
 that; the off-diagonals are zeros because the cross-derivatives of 3 arguments are 0.

Source
++++++

gradp.src

.. seealso:: Functions :func:`hessp`, :func:`hesscplx`

gradient first derivative complex argument
