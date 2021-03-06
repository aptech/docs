
pinvmt
==============================================

Purpose
----------------

Computes the Moore-Penrose pseudo-inverse of a matrix, using the singular
value decomposition. This pseudo-inverse is one particular type of generalized
inverse.

Format
----------------
.. function:: { y, err } = pinvmt(x, tol)

    :param x: data
    :type x: NxM matrix

    :param tol: any singular values less than *tol* are treated as zero in determining the rank of the input matrix.
    :type tol: scalar

    :return y: that satisfies the 4 Moore-Penrose conditions:

        .. csv-table::
            :widths: auto

            ":math:`xyx = x`"
            ":math:`yxy = y`"
            ":math:`xy` is symmetric"
            ":math:`yx` is symmetric"

    :rtype y: MxN matrix

    :return err: if not all of the singular values can be computed *err* will be nonzero.
    :rtype err: scalar

Examples
----------------
:func:`pinvmt` can be used to solve an undertermined least squares problem.

::

    tol = 1e-13;

    // Create an underdetermined system of equations 'A'
    A = rndn(4, 5);

    // Create a right hand side
    b = rndn(4, 1);

    if rank(A) < cols(A);
       print "A does not have full rank, using pinvmt to solve";
        { Api, err } = pinvmt(A, tol);
       x = Api*b;
    else;
       print "A has full rank, solve with '/' operator";
       x = b/A;
    endif;

Least squares problems with full rank can also be solved with the GAUSS
functions: :func:`ols`, :func:`olsqr` and :func:`olsqr2`.

Source
------

svdmt.src
