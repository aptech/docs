
spLU
==============================================

Purpose
----------------
Computes the LU decomposition of a sparse matrix A with partial pivoting.

Format
----------------
.. function:: spLU(a)

    :param a: non-singular sparse matrix.
    :type a: N x N

    :returns: l (*TODO*), NxN ''scrambled'' lower-triangular sparse matrix. This is a lower triangular
        matrix that has been reordered based upon the row pivoting.

    :returns: u (*TODO*), NxN ''scrambled'' upper-triangular sparse matrix. This is an upper triangular
        matrix that has been reordered based upon column pivoting to preserve sparsity.

Examples
----------------

::

    declare sparse matrix a, l, u;
    
    nz = {-5.974 0 -13.37 6.136                0,
               0   5.932   7.712       0  -6.549,
               0  -5.728       0  14.227       0,
               0 -12.164   9.916  13.902   6.182,
          13.425       0 -12.654 -16.534       0 };
    
    a = densetosp(nz,0);
    { l, u } = spLU(a);

Remarks
-------

If the input matrix or either of the factors L and U are singular, the
function will either terminate the program with an error message or
return an error code which can be tested for with the scalerr function.
This depends on the trap state as follows:

+------------+-----------------------------------------------+
| **trap 1** | return error code: 50                         |
+------------+-----------------------------------------------+
| **trap 0** | terminate with error message: Matrix singular |
+------------+-----------------------------------------------+

.. seealso:: Functions :func:`spLDL`

Technical Notes
+++++++++++++++

spLU implements functions from the SuperLU 4.0 library written by James
W. Demmel, John R. Gilbert and Xiaoye S. Li.

Copyright ©2003, The Regents of the University of California, through
Lawrence Berkeley National Laboratory (subject to receipt of any
required approvals from U.S. Dept. of Energy). All rights reserved.
