
ssgetAICC
==============================================

Purpose
----------------

Computes the corrected Akaike's information criterion from loglikelihood.

Format
----------------
.. function:: aicc = ssgetAICC(loglikelihood, df, numObs)

    :param loglikelihood: Loglikelihood value.
    :type loglikelihood: Scalar

    :param df: Degrees of freedom.
    :type df: Scalar

    :param numObs: Number of observations.
    :type numObs: Scalar

    :return aicc: Computed corrected Akaike's information criterion.
    :rtype aicc: Scalar

Examples
----------------

::

  // Loglikelihood value
  ll = -38.3;

  // Degrees of freedom
  df_model = 2;

  // Number of observations
  numObs = 150;

  // Compute AIC
  aicc = ssgetAICC(ll, df_model, numObs);

The code above results in the following:

::

  aic = 80.682

Source
------

ssmain.src

.. seealso:: Functions :func:`ssgetAIC`, :func:`ssgetBIC`, :func:`ssgetHQIC`
