
rref
==============================================

Purpose
----------------
Computes the reduced row echelon form of a matrix.

Format
----------------
.. function:: y = rref(x)

    :param x: data
    :type x: MxN matrix

    :return y: containing reduced row echelon form of *x*.

    :type y: MxN matrix

Remarks
-------

The tolerance used for zeroing elements is computed inside the procedure using:

::

   tol = maxc(m|n) * eps * maxc(abs(sumc(x')));

where :math:`eps = 2.24e-16`.

This procedure can be used to find the rank of a matrix. It is not as
stable numerically as the singular value decomposition (which is used in
the rank function), but it is faster for large matrices.

There is some speed advantage in having the number of rows be greater
than the number of columns, so you may want to transpose if all you care
about is the rank.

The following code can be used to compute the rank of a matrix:

::

   r = sumc(sumc(abs(y')) .> tol);

where *y* is the output from :func:`rref`, and *tol* is the tolerance used. This
finds the number of rows with any nonzero elements, which gives the rank
of the matrix, disregarding numeric problems.

Examples
----------------

::

    // Since (row 2) = 2*(row 1), we do not expect this
    // matrix to have full rank
    x[3,3] = 1 2 3
             2 4 6
             3 5 2;
    y = rref(x);
    
    // compute rank of x
    r = sumc(sumc(abs(rref(x)')) .> 1e-15);
    print "The rank of x = " r;

::

    The rank of x = 2.000

Source
------

rref.src

