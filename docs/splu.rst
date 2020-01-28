
spLU
==============================================

Purpose
----------------
Computes the :math:`LU` decomposition of a sparse matrix *A* with partial pivoting.

Format
----------------
.. function:: { l, u } = spLU(a)

    :param a: N x N non-singular sparse matrix.
    :type a: sparse matrix

    :return l: . This is a "scrambled" lower-triangular, sparse
        matrix that has been reordered based upon the row pivoting.

    :rtype l: NxN sparse matrix

    :return u: . This is an "scrambled" upper-triangular, sparse
        matrix that has been reordered based upon column pivoting to preserve sparsity.

    :rtype u: NxN sparse matrix

Examples
----------------

::

    declare sparse matrix a, l, u;

    nz = {-5.974       0  -13.37   6.136       0,
               0   5.932   7.712       0  -6.549,
               0  -5.728       0  14.227       0,
               0 -12.164   9.916  13.902   6.182,
          13.425       0 -12.654 -16.534       0 };

    a = densetosp(nz, 0);
    { l, u } = spLU(a);

Remarks
-------

If the input matrix or either of the factors :math:`L` and :math:`U` are singular, the
function will either terminate the program with an error message or
return an error code which can be tested for with the :func:`scalerr` function.

This depends on the `trap` state as follows:

============ =====================
``trap 1``   return error code: 50
``trap 0``   terminate with error message: Matrix singular
============ =====================

Technical Notes
----------------

:func:`spLU` implements functions from the SuperLU 4.0 library written by James
W. Demmel, John R. Gilbert and Xiaoye S. Li.

Copyright ©2003, The Regents of the University of California, through
Lawrence Berkeley National Laboratory (subject to receipt of any
required approvals from U.S. Dept. of Energy). All rights reserved.

.. seealso:: Functions :func:`spLDL`
