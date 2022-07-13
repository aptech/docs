
ssJarqueBera
==============================================

Purpose
----------------

Performs the Jarque-Bera goodness-of-fit test on model residuals.

Format
----------------
.. function:: { jb_stat, jb_pval } = ssJarqueBera(resid [, skew, kurtosis])

    :param resid: Model residuals.
    :type resid: Vector

    :param skew: Optional argument, skewness of residuals. If not provided, the skewness is computed.
    :type skew: Scalar

    :param kurtosis: Optional argument, kurtosis of residuals. If not provided, the kurtosis is computed.
    :type kurtosis: Scalar

    :return jb_stat: The Jarque-Bera test statistic for goodness-of-fit.
    :rtype jb_stat: Scalar

    :return jb_pval: The p-value for the returned Jarque-Bera test statistic for goodness-of-fit.
    :rtype jb_pval: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Compute Jarque-Bera test
  { jb_stat, jb_pval } = ssJarqueBera(resid);

The code above results in the following:

::

  jb_stat = 2.8019
  jb_pval = 0.2464

Source
------

ssmain.src

.. seealso:: Functions :func:`ssHeteroskedasticityTest`, :func:`ssSkewness`, :func:`ssKurtosis`, :func:`ssLjungBox`
