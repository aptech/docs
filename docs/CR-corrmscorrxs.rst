
corrms,corrxs
==============================================

Purpose
----------------

Computes the observed correlation matrix.

Format
----------------
.. function:: corrxs(x)

    :param m: KxK moment (x'x) matrix. A constant term MUST have been
        the first variable when the moment matrix was computed.
    :type m: TODO

    :param x: NxK matrix of data.
    :type x: TODO

    :returns: cx (*TODO*), PxP correlation matrix. For corrms, P = K-1. For corrxs, P = K.

Examples
----------------

::

    rndseed   8989;
    x1 = rndn(3,3);
    x2 = ones(3,1)~x1;
    print "x1 :" x1 ;
    print "x2 :" x2;

After the above code, x1 and x2 look like:

::

    x1 :
          0.010555555     -0.045969063       0.12701699 
    	1.6454828        1.2380373       0.53988699 
    	1.1556776      -0.53575797       0.14056238 
    x2 :
    	1.0000000      0.010555555     -0.045969063       0.12701699 
    	1.0000000        1.6454828        1.2380373       0.53988699 
    	1.0000000        1.1556776      -0.53575797       0.14056238

Continuing from above code,

::

    print "corrxs(x1) :" corrxs(x1) ;				
    print "corrms(x2'x2) :" corrms(x2'x2);

After the above code,

::

    corrxs(x1) :
    	 1.0000000       0.52196856       0.75039768 
    	0.52196856        1.0000000       0.95548228 
    	0.75039768       0.95548228        1.0000000 
    corrms(x2'x2) :
    	 1.0000000       0.52196856       0.75039768 
    	0.52196856        1.0000000       0.95548228 
    	0.75039768       0.95548228        1.0000000

Remarks
+++++++

The correlation matrix is the standardized version of the
correlation/covariance matrix computed from the input data, that is, it
divides the sample size, N, rather than N - 1. For an unbiased estimate
correlation/covariance matrix which uses N - 1, use corrm or corrx.

Source
++++++

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrm`, :func:`corrx`, :func:`varCovX`, :func:`varCovM`

sample correlation matrix moment
