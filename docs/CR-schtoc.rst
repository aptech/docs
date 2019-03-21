
schtoc
==============================================

Purpose
----------------

Reduces any 2x2 blocks on the diagional of the real Schur matrix returned from schur. The transformation matrix is also updated.

Format
----------------
.. function:: schtoc(sch, trans)

    :param sch: i.e., upper
        triangular except for possibly 2x2 blocks on the
        diagonal.
    :type sch: real NxN matrix in Real Schur form

    :param trans: the associated transformation matrix.
    :type trans: real NxN matrix

    :returns: schc (*NxN matrix*), possibly complex, strictly upper triangular.
        The diagonal entries are the eigenvalues.

    :returns: transc (*NxN matrix*), possibly complex, the associated
        transformation matrix.

Remarks
-------

Other than checking that the inputs are strictly real matrices, no other
checks are made. If the input matrix sch is already upper triangular, it
is not changed. Small off-diagonal elements are considered to be zero.
See the source code for the test used.


Examples
----------------

::

    { schc, transc } = schtoc(schur(a));

This example calculates the complex Schur form for a real
matrix a.

Source
------

schtoc.src

.. seealso:: Functions :func:`schur`

reduce 2x2 block diagonal real Schur form matrix return transformation
