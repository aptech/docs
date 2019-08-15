
gradp, gradcplx
==============================================

Purpose
----------------

Computes the gradient vector or matrix (Jacobian) of a vector-valued function that has been defined in a
procedure. Single-sided (forward difference) gradients are computed. :func:`gradcplx` allows for
complex arguments.

Format
----------------
.. function:: g = gradp(&fct, x0)
              g = gradcplx(&fct, x0)

    :param &fct: a pointer to a vector-valued function (fct: :math:`Kx1 → Nx1`)
        defined as a procedure. It is acceptable for :math:`fct(x)`
        to have been defined in terms of global arguments in addition to *x*, and thus *fct* can
        return an Nx1 vector:

    ::

        proc fct(x);
            retp( exp(x.*b));
        endp;

    :type &fct: Function pointer

    :param x0: points at which to compute gradient
    :type x0: Kx1 vector

    :return g: containing the gradients of *fct* with
        respect to the variable *x* at *x0*.

    :rtype g: NxK matrix

Remarks
-------

:func:`gradp` will return a row for every row that is returned by *fct*. For
instance, if *fct* returns a scalar result, then :func:`gradp` will return a 1xK row
vector. This allows the same function to be used regardless of *N*, where
*N* is the number of rows in the result returned by *fct*. Thus, for instance,
:func:`gradp` can be used to compute the Jacobian matrix of a set of equations.


Examples
----------------

::

    proc myfunc(x);
       retp(x .* 2 .* exp( x .* x ./ 3 ));
    endp;

    x0 = 2.5|3.0|3.5;
    y = gradp(&myfunc, x0);

After the code above, *y* is equal to:

::

    82.989017       0.00000000       0.00000000
    0.00000000        281.19753       0.00000000
    0.00000000       0.00000000        1087.9541

It is a 3x3 matrix because we are passing it 3 arguments and ``myfunc`` returns 3 results when we do
 that; the off-diagonals are zeros because the cross-derivatives of 3 arguments are 0.

Source
------

gradp.src

.. seealso:: Functions :func:`hessp`, :func:`hesscplx`
