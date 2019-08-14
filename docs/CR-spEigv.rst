
spEigv
==============================================

Purpose
----------------

Computes a specified number of eigenvalues and eigenvectors of a square, sparse matrix *a*.

Format
----------------
.. function:: { va, ve } = spEigv(a, nev, which, tol, maxit, ncv)

    :param a: NxN square, sparse matrix.
    :type a: sparse matrix

    :param nev: number of eigenvalues to compute.
    :type nev: scalar

    :param which: may be one of the following: "LM" largest magnitude, "LR" largest real, "LI" largest imaginary, "SR" smallest real, or "SI" smallest imaginary. Default input 0, sets *which* to "LM."
    :type which: string

    :param tol: tolerance for eigenvalues. Default input 0, sets  tol to 1e-15.
    :type tol: scalar

    :param maxit: maximum number of iterations. Default input 0, sets  maxit to  nevx(columns of  a)x100.
    :type maxit: scalar

    :param ncv: size of Arnoldi factorization. The minimum setting is the greater of :math:`nev+2` and 20. See Remarks on how to set *ncv*. Default input 0, sets *ncv* to 2x :math:`nev+1`.
    :type ncv: scalar

    :return va: containing the computed eigenvalues of input matrix *a*.

    :type va: nevx1 dense vector

    :return ve: containing the corresponding eigenvectors of input matrix *a*.

    :type ve: Nx nev dense matrix

Remarks
-------

The ideal setting for input *ncv* is problem dependent and cannot be
easily predicted ahead of time. Increasing *ncv* will increase the amount
of memory used during computation. For a large, sparse matrix, *ncv*
should be small compared to the order of input matrix *a*. :func:`spEigv` is not
thread-safe.

Examples
----------------

::

    rndseed 3456;
    sparse matrix a;
     x = 10*rndn(5,5);
     a = densetosp(x,4);

::

        21.276135  5.4078872 -19.817044  9.6771132 -19.211952
        0.0000000 -4.4011007  10.445221 -5.1742289 -16.336474
    a = 0.0000000 -20.853017  7.6285434  0.0000000 -15.626397
       -12.637055  8.1227002  0.0000000 -8.7817892  0.0000000
        0.0000000 -7.8181517  15.326816  0.0000000  0.0000000

::

    { va, ve } = spEigv(a,2,0,0,0,0); 
    /* equivalent to call { va, ve } = spEigv(a,2,"LM",1e-15,2*5*100,5); */

::

    va = 21.089832
        -3.4769986 + 20.141970i
    
    ve = -0.92097057   0.29490584 - 0.38519280i
         -0.10091920  -0.18070330 - 0.38405816i
         0.061241324   0.24121182 - 0.56419722i
          0.36217049  0.017643612 + 0.26254313i
         0.081917964  -0.31466284 - 0.19936942i

Below we show that the first eigenvalue times the corresponding eigenvector (1) equals the input 
matrix times the first eigenvector (2).

::

    (1) va[1]*ve[.,1]     =      (2) a*ve[.,1] =
     -19.423115                  -19.423115
     -2.1283690                  -2.1283690
      1.2915693                   1.2915693
      7.6381149                   7.6381149
      1.7276361                   1.7276361

Technical Notes
----------------

spEigv implements functions from the ARPACK library.

