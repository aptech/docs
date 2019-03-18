
corrm,corrvc,corrx
==============================================

Purpose
----------------

Computes an unbiased estimate of a correlation matrix.

Format
----------------
.. function:: corrx(x)

    :param m: KxK moment (x'x) matrix. A constant term MUST have been
        the first variable when the moment matrix was computed.
    :type m: TODO

    :param vc: KxK variance-covariance matrix (of data or parameters).
    :type vc: TODO

    :param x: NxK matrix of data.
    :type x: TODO

    :returns: cx (*TODO*), PxP correlation matrix. For corrm, P = K-1. For corrvc and
        corrx, P = K.

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

    print "corrx(x1) :" corrx(x1);
    print "corrm(x2'x2) :" corrm(x2'x2);
    print "corrvc(varCovMS(x2'x2)):" corrvc(varCovMS(x2'x2));

After the above code,

::

    corrx(x1) :
    	 1.0000000       0.52196856       0.75039768 
    	0.52196856        1.0000000       0.95548228 
    	0.75039768       0.95548228        1.0000000 
    corrm(x2'x2) :
    	 1.0000000       0.52196856       0.75039768 
    	0.52196856        1.0000000       0.95548228 
    	0.75039768       0.95548228        1.0000000 
    corrvc(varCovMS(x2'x2)):
    	 1.0000000       0.52196856       0.75039768 
    	0.52196856        1.0000000       0.95548228 
    	0.75039768       0.95548228        1.0000000

Remarks
+++++++

The correlation matrix is the standardized version of the unbiased
estimator of the population variance-covariance matrix. It is computed
using the moment matrix of deviations about the mean divided by the
number of observations minus one N - 1. For the observed
correlation/covariance matrix which uses N rather than N - 1, see corrms
and corrxs.

Source
++++++

corr.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`, :func:`corrxs`, :func:`varCovX`, :func:`varCovM`

correlation matrix moment variance covariance
