
skewness
==============================================

Purpose
----------------

Compute the sample skewness.

Format
----------------
.. function:: g = skewness(x [, bias] )

    :param x: Nxk, sample data.
    :type x: Vector

    :param bias: Optional argument. Indicator for bias correction. If anything other than 0, bias correction is used. Default = 0.
    :type bias: Scalar

    :return g: Sample skewness.
    :rtype g: Scalar

Examples
----------------

Example One: Vector input
+++++++++++++++++++++++++++++++

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Compute sample skewness
  g = skewness(resid);

The code above results in the following:

::

  g = 0.3049

Example Two: Matrix input
+++++++++++++++++++++++++++++++

  ::

    // Generate random vector of residuals
    rndseed 929212;
    resid = rndn(150, 2);

    // Compute sample skewness
    g = skewness(resid);

  The code above results in the following:

  ::

    g = 0.26494746   -0.14941577
.. seealso:: Functions :func:`kurtosis`, :func:`JarqueBera`
