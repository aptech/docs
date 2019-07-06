
corrm, corrvc, corrx
==============================================

Purpose
----------------

Computes an unbiased estimate of a correlation matrix.

Format
----------------
.. function:: corrm(m)
              corrvc(vc)
              corrx(x)

    :param m: A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param vc: data or parameters
    :type vc: KxK variance-covariance matrix

    :param x: data
    :type x: NxK matrix

    :returns: **cx** (*PxP correlation matrix*) - For :func:`corrm`, :math:`P = K-1`. For :func:`corrvc` and
        :func:`corrx`, :math:`P = K`.

Remarks
------------

The correlation matrix is the standardized version of the unbiased
estimator of the population variance-covariance matrix. It is computed
using the moment matrix of deviations about the mean divided by the
number of observations minus one :math:`N - 1`. For the observed
correlation/covariance matrix which uses :math:`N` rather than :math:`N - 1`, see :func:`corrms`
and :func:`corrxs`.

Examples
----------------

::

    // Set rnd seed for reproducible results
    rndseed   8989;

    // Assign x1 and x2
    x1 = rndn(3, 3);
    x2 = ones(3, 1)~x1;

    print "x1 :" x1 ;
    print "x2 :" x2;

After the above code, *x1* and *x2* look like:

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

    // Correlation of x1 with x1
    print "corrx(x1) :" corrx(x1);

    // Correlation of moment = x2'x2
    m = x2'x2;
    print "corrm(x2'x2) :" corrm(m);

    // Correlation of vc of x2
    vc = varCovMS(x2'x2);
    print "corrvc(varCovMS(x2'x2)):" corrvc(vc);

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

    corrvc(vc):
    	 1.0000000       0.52196856       0.75039768
    	0.52196856        1.0000000       0.95548228
    	0.75039768       0.95548228        1.0000000

Source
------------

corr.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`, :func:`corrxs`, :func:`varCovX`, :func:`varCovM`
