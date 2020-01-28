
lapeighvb
==============================================

Purpose
----------------

Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix selected by bounds.

Format
----------------
.. function:: { ve, va } = lapeighvb(x, vl, vu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param vl: lower bound of the interval to be searched for eigenvalues.
    :type vl: scalar

    :param vu: upper bound of the interval to be searched for eigenvalues; *vu* must be greater than *vl*.
    :type vu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval :math:`[a, b]`
        of width less than or equal to :math:`abstol + EPS*max(|a|, |b|)`, where *EPS* is machine precision.
        If *abstol* is less than or equal to zero, then :math:`EPS*||T||` will be used in its place, where
        *T* is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :return ve: eigenvalues, where *M* is the number of eigenvalues on the half open interval :math:`[vl, vu]`. If no eigenvalues are found then *s* is a scalar missing value.

    :rtype ve: Mx1 vector

    :return va: eigenvectors.

    :rtype va: NxM matrix

Examples
----------------

::

    // Assign x
    x = { 5 2 1,
          2 6 2,
          1 2 9 };

    // Set lower bound to be searched
    vl = 5;

    // Set upper bound to be searched
    vu = 10;

    // Find eigenvalues within the bounds of
    // vl and vu and the corresponding
    // eigenvectors
    { ve, va } = lapeighvb(x, vl, vu, 0);

    print "Eigenvalues = " ve;
    print "Eigenvectors = " va;

::

    Eigenvalues =   6.0000
    Eigenvectors =
     -0.5774
     -0.5774
      0.5774

If you increase the value of *vu* to 12.

::

  // Set lower bound to be searched
  vl = 5;

  // Set upper bound to be searched
  vu = 12;

  // Find eigenvalues within the bounds of
  // vl and vu and the corresponding
  // eigenvectors
  { ve, va } = lapeighvb(x, vl, vu, 0);

  print "Eigenvalues = " ve;
  print "Eigenvectors = " va;

::

    Eigenvalues
      6.0000
     10.6056
    Eigenvectors =
     -0.5774   0.3197
     -0.5774   0.4908
      0.5774   0.8105

Remarks
-------

:func:`lapeighvb` computes eigenvalues and eigenvectors which are found on the
half open interval :math:`[vl, vu]`. :func:`lapeighvb` is based on the LAPACK drivers
*DSYEVX* and *ZHEEVX*. Further documentation of these functions may be found
in the LAPACK User's Guide.


