
lapeighi
==============================================

Purpose
----------------

Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by index.

Format
----------------
.. function:: ve = lapeighi(x, il, iu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param il: index of the smallest desired eigenvalue ranking them from smallest to largest.
    :type il: scalar

    :param iu: index of the largest desired eigenvalue, *iu* must be greater than *il*.
    :type iu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval :math:`[a, b]` of width less
        than or equal to :math:`abstol + EPS*max(|a|, |b|)`, where *EPS* is machine precision.
        If *abstol* is less than or equal to zero, then :math:`EPS*||T||` will be used in its place,
        where *T* is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :return ve: eigenvalues.

    :rtype ve: (iu-il+1)x1 vector

Examples
----------------

::

    // Define x matrix
    x = { 5 2 1,
          2 6 2,
          1 2 9 };

    // Index of smallest desired eigenvalue
    il = 2;

    // Index of largest desired eigenvalue
    iu = 3;

    // Compute eigenvalues with indices between
    // il and iu
    ve = lapeighi(x, il, iu, 0);

    // Print eigenvalues
    print ve;

The code above calculates the second and third eigenvalues and returns:

::

    6.0000
    10.6056

To calculate the first, second and third eigenvalues, reusing the same *x* from above:

::

  // Index of smallest desired eigenvalue
  il = 1;

  // Index of largest desired eigenvalue
  iu = 3;

  // Compute eigenvalues with indices between
  // il and iu
  ve = lapeighi(x, il, iu, 0);

  // Print eigenvalues
  print ve;

The output from this code is:

::

     3.3944
     6.0000
    10.6056

Remarks
-------

:func:`lapeighi` computes :math:`iu-il+1` eigenvalues only given a range of indices,
i.e., the ith to jth eigenvalues, ranking them from smallest to largest.
To find eigenvalues within a specified range see :func:`lapeighxb`. For
eigenvectors see :func:`lapeighvi`, or :func:`lapeighvb`. :func:`lapeighi` is based on the
LAPACK drivers *DSYEVX* and *ZHEEVX*. Further documentation of these
functions may be found in the LAPACK User's Guide.


.. seealso:: Functions :func:`lapeighb`, :func:`lapeighvi`, :func:`lapeighvb`
