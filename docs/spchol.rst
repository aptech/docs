
spChol
==============================================

Purpose
----------------
Computes the :math:`LL^{T}` decomposition of a sparse matrix *A*.

Format
----------------
.. function:: L = spChol(a)

    :param a: symmetric, positive definite sparse matrix.
    :type a: NxN sparse matrix

    :return L: lower-triangular sparse matrix

    :rtype L: NxN sparse matrix

Examples
----------------

::

    sparse matrix A;
    sparse matrix L;

    // Create a small, simple positive-definite matrix
    x = { 9.53984224e+001 -5.84272701e+000 1.99970335e+001,
         -5.84272701e+000  1.09765831e+002 2.52038945e+000,
          1.99970335e+001  2.52038945e+000 4.71834812e+000 };

    // Create the sparse matrix A from x, keeping all elements
    A = denseToSp(x, 0);

    // Create matrix factorization
    L = spChol(A);

Technical Notes
----------------

:func:`spChol` implements functions from the TAUCS library: TAUCS Version 2.2.
Copyright ©2001, 2002, 2003 by Sivan Toledo, Tel-Aviv University,
stoledo@tau.ac.il. All Rights Reserved.

.. seealso:: Functions :func:`spLDL`, :func:`spLU`
