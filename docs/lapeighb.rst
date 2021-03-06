
lapeighb
==============================================

Purpose
----------------

Computes eigenvalues only of a real symmetric or complex Hermitian matrix selected by bounds.

Format
----------------
.. function:: ve = lapeighb(x, vl, vu, abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param vl: lower bound of the interval to be searched for eigenvalues.
    :type vl: scalar

    :param vu: upper bound of the interval to be searched for eigenvalues; *vu* must be greater than *vl*.
    :type vu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval :math:`[a, b]` of
        width less than or equal to :math:`abstol + EPS*max(|a|, |b|)`, where *EPS* is machine precision. If *abstol* is less than or equal to
        zero, then :math:`EPS*||T||` will be used in its place,
        where *T* is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :return ve: eigenvalues, where *M* is the number of eigenvalues on
        the half open interval [vl, vu]. If no eigenvalues are found
        then *ve* is a scalar missing value.

    :rtype ve: Mx1 vector

Examples
----------------

::

    // Define x matrix
    x = { 5 2 1,
          2 6 2,
          1 2 9 };

    // Lower bound of interval to be searched
    vl = 5;

    // Upper bound of interval to be searched
    vu = 10;

    // Find eigenvalues in the range vl to vu
    ve = lapeighb(x, vl, vu, 1e-15);

    // Print eigenvalues
    print ve;

The code above returns:

::

    6.0000

Remarks
-------

:func:`lapeighb` computes eigenvalues only which are found on the half open
interval :math:`[vl, vu]`. To find eigenvalues within a specified range of
indices see :func:`lapeighi`. For eigenvectors see :func:`lapeighvi`, or :func:`lapeighvb`.
:func:`lapeighb` is based on the LAPACK drivers *DSYEVX* and *ZHEEVX*. Further
documentation of these functions may be found in the LAPACK User's Guide.


.. seealso:: Functions :func:`lapeighvi`, :func:`lapeighvb`
