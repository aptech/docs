
lapsvdcusv
==============================================

Purpose
----------------

Computes the singular value decomposition of a real or complex rectangular matrix, returns compact U and  v.

Format
----------------
.. function:: lapsvdcusv(x)

    :param x: real or complex rectangular matrix.
    :type x: MxN matrix

    :returns: u (*TODO*), Mxmin(M,N) matrix, left singular vectors.

    :returns: s (*TODO*), min(M,N)xN matrix, singular values.

    :returns: v (*NxN matrix*), right singular values.

Examples
----------------

::

    x = { 2.143 4.345 6.124,
          1.244 5.124 3.412, 
          0.235 5.657 8.214 };
     
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

.. seealso:: Functions :func:`lapsvds`, :func:`lapsvdusv`

singular value decomposition real complex rectangular matrix return
compact
