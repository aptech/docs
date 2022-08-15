
ssgetBIC
==============================================

Purpose
----------------

Computes the Schwarz’s Bayesian information criterion from loglikelihood.

Format
----------------
.. function:: bic = ssgetBIC(loglikelihood, df, numObs)

    :param loglikelihood: Loglikelihood value.
    :type loglikelihood: Scalar

    :param df: Degrees of freedom.
    :type df: Scalar

    :param numObs: Number of observations.
    :type numObs: Scalar

    :return bic: Computed Schwarz’ Bayesian information criterion.
    :rtype bic: Scalar

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
  bic = ssgetBIC(ll, df_model, numObs);

The code above results in the following:

::

  bic = 86.62

Source
------

ssmain.src

.. seealso:: Functions :func:`ssgetAICC`, :func:`ssgetAIC`, :func:`ssgetHQIC`
