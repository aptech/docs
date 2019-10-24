
pinv
==============================================

Purpose
----------------
Computes the Moore-Penrose pseudo-inverse of a matrix, using the singular value decomposition. This pseudo-inverse is one particular type of generalized inverse.

Format
----------------
.. function:: y = pinv(x)

    :param x: data
    :type x: NxM matrix

    :return y: satisfies the 4 Moore-Penrose conditions:

        .. csv-table::
            :widths: auto

            ":math:`xyx = x`"
            ":math:`yxy = y`"
            ":math:`xy` is symmetric"
            ":math:`yx` is symmetric"

    :rtype y: MxN matrix

Global Input
------------

:_svdtol: (*scalar*), any singular values less than *_svdtol* are treated as zero
    in determining the rank of the input matrix. The default value for *_svdtol* is 1.0e-13.

Global Output
-------------

:_svderr: (*scalar*), if not all of the singular values can be computed *_svderr* will be nonzero.

Examples
----------------
:func:`pinv` can be used to solve an undertermined least squares problem.

::

    // Create an underdetermined system of equations 'A'
    A = rndn(4, 5);

    // Create a right hand side
    b = rndn(4, 1);

    if rank(A) < cols(A);
       print "A does not have full rank, using pinv to solve";
       Api = pinv(A);
       x = Api*b;
    else;
       print "A has full rank, solve with '/' operator";
       x = b/A;
    endif;

Least squares problems with full rank can also be solved with the GAUSS
functions: :func:`ols`, :func:`olsqr` and :func:`olsqr2`.

Source
------

svd.src
