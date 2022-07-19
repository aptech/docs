
ssSkewness
==============================================

Purpose
----------------

Compute the sample skewness.

Format
----------------
.. function:: g = ssSkewness(x [, bias] )

    :param x: Nx1, sample data.
    :type x: Vector

    :param bias: Optional argument. Indicator for bias correction. If anything other than 0, bias correction is used. Default = 0.
    :type bias: Scalar

    :return g: Sample skewness.
    :rtype g: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Compute sample skewness
  g = ssSkewness(resid);

The code above results in the following:

::

  g = 0.3049


Source
------

ssmain.src

.. seealso:: Functions :func:`ssKurtosis`, :func:`ssJarqueBera`
