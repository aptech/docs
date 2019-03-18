
lapeighvb
==============================================

Purpose
----------------

Computes eigenvalues and eigenvectors of a real symmetric or complex Hermitian matrix selected by bounds.

Format
----------------
.. function:: lapeighvb(x,  vl,  vu,  abstol)

    :param x: real symmetric or complex Hermitian.
    :type x: NxN matrix

    :param vl: lower bound of the interval to be searched for eigenvalues.
    :type vl: scalar

    :param vu: upper bound of the interval to be searched for eigenvalues;  vu must be greater than  vl.
    :type vu: scalar

    :param abstol: the absolute error tolerance for the
        eigenvalues. An approximate eigenvalue is accepted as converged
        when it is determined to lie in an interval [a, b]
        of width less than or equal to  abstol + EPS*max(|a|, |b|), where EPS is machine precision.
        If abstol is less than or equal to zero, then EPS*||T|| will be used in its place, where
        T is the tridiagonal matrix obtained by reducing the input matrix to tridiagonal form.
    :type abstol: scalar

    :returns: ve (*Mx1 vector*), eigenvalues, where M is the number of eigenvalues on the half open interval [vl, vu]. If no eigenvalues are found
        then s is a scalar missing value.

    :returns: va (*NxM matrix*), eigenvectors.

Examples
----------------

::

    x = { 5 2 1,
          2 6 2,
          1 2 9 };
     
    vl = 5;
    vu = 10;
    { ve, va } = lapeighvb(x,vl,vu,0);
    
    print "Eigenvalues" ve;
    print "Eigenvectors = " va;

::

    Eigenvalues =   6.0000
    Eigenvectors =
     -0.5774
     -0.5774
      0.5774

If you increase the value of vu to 12.

::

    { ve, va } = lapeighvb(x,5,12,0);
    
    print "Eigenvalues" ve;
    print "Eigenvectors = " va;

::

    Eigenvalues
      6.0000
     10.6056
    Eigenvectors =
     -0.5774   0.3197
     -0.5774   0.4908
      0.5774   0.8105

eigenvalue and eigenvectors real symmetric complex Hermitian matrix
selected by bounds
