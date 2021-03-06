
lapsvdusv
==============================================

Purpose
----------------

Computes the singular value decomposition a real or complex rectangular matrix.

Format
----------------
.. function:: { u, s, v } = lapsvdusv(x)

    :param x: real or complex rectangular matrix.
    :type x: MxN matrix

    :return u: left singular vectors.

    :rtype u: MxM matrix

    :return s: singular values.

    :rtype s: MxN matrix

    :return v: right singular vectors.

    :rtype v: NxN matrix

Examples
----------------

::

    // Assign x
    x = { 2.143 4.345 6.124,
          1.244 5.124 3.412,
          0.235 5.657 8.214 };

    { u, s, v } = lapsvdusv(x);

    print u;

::

     -0.5553  0.0490  0.8302
     -0.4309  0.8368 -0.3377
     -0.7113 -0.5452 -0.4436

::

    print s;

::

    13.8959 0.0000 0.0000
     0.0000 2.1894 0.0000
     0.0000 0.0000 1.4344

::

    print v;

::

     -0.1362  0.4650  0.8748
      0.6221  0.6470 -0.4408
     -0.7710 -0.6043  0.2011

Remarks
-------

:func:`lapsvdusv` computes the singular value decomposition of a real or complex
rectangular matrix. The SVD is

::

   x = usv'

where *v* is the matrix of right singular vectors. :func:`lapsvdusv` is based on
the LAPACK drivers *DGESVD* and *ZGESVD*. Further documentation of these
functions may be found in the LAPACK User's Guide.


.. seealso:: Functions :func:`lapsvds`, :func:`lapsvdcusv`
