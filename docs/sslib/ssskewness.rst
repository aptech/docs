
ssSkewness
==============================================

Purpose
----------------

Computes the sample skewness.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

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

ssdiagnostics.src

.. seealso:: Functions :func:`ssKurtosis`, :func:`ssJarqueBera`
