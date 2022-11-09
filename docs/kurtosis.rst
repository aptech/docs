
kurtosis
==============================================

Purpose
----------------

Compute the sample kurtosis.

Format
----------------
.. function:: k = kurtosis(x [, excess] )

    :param x: Nx1, sample data.
    :type x: Vector

    :param excess: Optional argument. Indicator for computing excess kurtosis. If anything other than 0, excess kurtosis is computed. Default = 0.
    :type excess: Scalar

    :return k: Sample kurtosis.
    :rtype k: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Compute sample skewness
  k = kurtosis(resid);

The code above results in the following:

::

  k = 2.7234


.. seealso:: Functions :func:`skewness`, :func:`JarqueBera`
