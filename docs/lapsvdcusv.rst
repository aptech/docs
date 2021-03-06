
lapsvdcusv
==============================================

Purpose
----------------

Computes the singular value decomposition of a real or complex rectangular matrix, returns compact *U* and *v*.

Format
----------------
.. function:: { u, s, v } = lapsvdcusv(x)

    :param x: real or complex rectangular matrix.
    :type x: MxN matrix

    :return u: left singular vectors.

    :rtype u: Mxmin(M,N) matrix

    :return s: singular values.

    :rtype s: min(M,N)xN matrix

    :return v: right singular values.

    :rtype v: NxN matrix

Examples
----------------

::

    // Assign x matrix
    x = { 2.143 4.345 6.124,
          1.244 5.124 3.412,
          0.235 5.657 8.214 };

    // Compute singular value decomposition 
    { u,s,v } = lapsvdusv(x);

::

    print u;

::

     -0.55531277  0.049048431 0.83019394
     -0.43090168  0.83684123 -0.33766923
     -0.71130266 -0.54524400 -0.44357356

::

    print s;

::

     13.895868 0.0000000 0.0000000
     0.0000000 2.1893939 0.0000000
     0.0000000 0.0000000 1.4344261

::

    print v;

::

     -0.13624432  -0.62209955 -0.77099263
      0.46497296   0.64704876 -0.60425826
      0.87477862  -0.44081748  0.20110275

Remarks
-------

:func:`lapsvdcusv` computes the singular value decomposition of a real or
complex rectangular matrix. The SVD is

::

   x = usv'

where *v* is the matrix of right singular vectors. :func:`lapsvdcusv` is based on
the LAPACK drivers *DGESVD* and *ZGESVD*. Further documentation of these
functions may be found in the LAPACK User's Guide.


.. seealso:: Functions :func:`lapsvds`, :func:`lapsvdusv`
