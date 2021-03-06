
spLDL
==============================================

Purpose
----------------
Computes the :math:`LDL` decomposition of a symmetric sparse matrix *A*.

Format
----------------
.. function:: { l, d } = spLDL(a)

    :param a: NxN symmetric sparse matrix.
    :type a: sparse matrix

    :return l: The lower-triangular sparse matrix :math:`LDL` decomposition of *A*.

    :rtype l: NxN lower-triangular sparse matrix

    :return d: The diagonal sparse matrix :math:`LDL` decomposition of *A*.

    :rtype d: NxN diagonal sparse matrix

Examples
----------------

::

    declare sparse matrix a, l, d;

    nz = { 142 13 56 57 0,
            13  0  0  0 0,
            56  0 94 47 0,
            57  0 47 35 0,
             0  0  0  0 0 };

     a = densetosp(nz, 0);

     { l, d } = spLDL(a);

Remarks
-------

:func:`spLDL` will not check to see if the input matrix is symmetric. The
function looks only at the lower triangular portion of the input matrix.

Technical Notes
----------------

:func:`spLDL` implements functions from the TAUCS library:

TAUCS Version 2.2 Copyright ©2003, by Sivan Toledo, Tel-Aviv University,
stoledo@tau.ac.il. All Rights Reserved.

.. seealso:: Functions :func:`spLU`
