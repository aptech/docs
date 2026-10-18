
ssKurtosis
==============================================

Purpose
----------------

Computes the sample kurtosis.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: k = ssKurtosis(x [, excess] )

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

  // Compute sample kurtosis
  k = ssKurtosis(resid);

The code above results in the following:

::

  k = 2.7234


Source
------

ssdiagnostics.src

.. seealso:: Functions :func:`ssSkewness`, :func:`ssJarqueBera`
