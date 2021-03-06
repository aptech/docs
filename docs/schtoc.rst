
schtoc
==============================================

Purpose
----------------

Reduces any 2x2 blocks on the diagonal of the real Schur matrix returned from :func:`schur`. The transformation matrix is also updated.

Format
----------------
.. function:: { schc, transc } = schtoc(sch, trans)

    :param sch: real NxN matrix in Real Schur form. i.e., upper triangular except for possibly 2x2 blocks on the diagonal.
    :type sch: matrix

    :param trans: real NxN matrix. the associated transformation matrix.
    :type trans: matrix

    :return schc: possibly complex, strictly upper triangular. The diagonal entries are the eigenvalues.

    :rtype schc: NxN matrix

    :return transc: possibly complex, the associated transformation matrix.

    :rtype transc: NxN matrix

Examples
----------------

::

    // Create a 2 x 2 matrix
    a = { 7 -2,
       12 -5 };

   { schc, transc } = schtoc(schur(a));

This example calculates the complex Schur form for a real matrix *a*.

Remarks
-------

Other than checking that the inputs are strictly real matrices, no other
checks are made. If the input matrix *sch* is already upper triangular, it
is not changed. Small off-diagonal elements are considered to be zero.
See the source code for the test used.


Source
------

schtoc.src

.. seealso:: Functions :func:`schur`
