
corrms, corrxs
==============================================

Purpose
----------------

Computes the observed correlation matrix.

Format
----------------
.. function:: cx = corrms(m)
              cx = corrxs(x)

    :param m: A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param x: data
    :type x: NxK matrix

    :return cx: For :func:`corrms`, :math:`P = K-1`. For :func:`corrxs`, :math:`P = K`.

    :rtype cx: PxP correlation matrix

Examples
----------------

::

  // Set rnd seed for reproducible results
  rndseed   8989;

  // Assign x1 and x2
  x1 = rndn(3, 3);
  x2 = ones(3, 1)~x1;

  print "x1 :" x1;
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
    print "corrxs(x1) :" corrxs(x1) ;

    // Correlation of moment = x2'x2
    m = x2'x2;
    print "corrms(x2'x2) :" corrms(m);

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
------------

The :func:`corrms` and :func:`corrxs` computes the sample correlation matrix. For the population
correlation matrix, use :func:`corrm` or :func:`corrx`.

Source
------------

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrm`, :func:`corrx`, :func:`varCovX`, :func:`varCovM`
