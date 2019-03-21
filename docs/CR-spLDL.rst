
spLDL
==============================================

Purpose
----------------
Computes the LDL decomposition of a symmetric sparse matrix A.

Format
----------------
.. function:: spLDL(a)

    :param a: symmetric sparse matrix.
    :type a: N x N

    :returns: l (*TODO*), NxN lower-triangular sparse matrix.

    :returns: d (*TODO*), NxN diagonal sparse matrix.

Examples
----------------

::

    declare sparse matrix a, l, d;
    nz = { 142 13 56 57 0,
            13  0  0  0 0,
            56  0 94 47 0,
            57  0 47 35 0,
             0  0  0  0 0 };
             
     a = densetosp(nz,0);
     { l, d } = spLDL(a);

Remarks
-------

spLDL will not check to see if the input matrix is symmetric. The
function looks only at the lower triangular portion of the input matrix.

.. seealso:: Functions :func:`spLU`

Technical Notes
+++++++++++++++

spLDL implements functions from the TAUCS library:

TAUCS Version 2.2 Copyright ©2003, by Sivan Toledo, Tel-Aviv University,
stoledo@tau.ac.il. All Rights Reserved.
