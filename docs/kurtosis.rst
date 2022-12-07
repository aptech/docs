
kurtosis
==============================================

Purpose
----------------

Compute the sample kurtosis.

Format
----------------
.. function:: k = kurtosis(x [, excess] )

    :param x: Nxk, sample data.
    :type x: Matrix

    :param excess: Optional argument. Indicator for computing excess kurtosis. If anything other than 0, excess kurtosis is computed. Default = 0.
    :type excess: Scalar

    :return k: Sample kurtosis.
    :rtype k: Scalar

Examples
----------------

Example One: Vector input
+++++++++++++++++++++++++++++++

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Compute sample skewness
  k = kurtosis(resid);

The code above results in the following:

::

  k = 2.7234

Example Two: Matrix input
+++++++++++++++++++++++++++++++

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 2);

  // Compute sample skewness
  k = kurtosis(resid);

The code above results in the following:

::

  k = 2.6612276        3.0123801

.. seealso:: Functions :func:`skewness`, :func:`JarqueBera`
