
ssgetHQIC
==============================================

Purpose
----------------

Computes the Hannan–Quinn information criterion from loglikelihood.

Format
----------------
.. function:: hqic = ssgetHQIC(loglikelihood, df, numObs)

    :param loglikelihood: Loglikelihood value.
    :type loglikelihood: Scalar

    :param df: Degrees of freedom.
    :type df: Scalar

    :param numObs: Number of observations.
    :type numObs: Scalar

    :return hqic: Computed Hannan–Quinn information criterion.
    :rtype hqic: Scalar

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
  hqic = ssgetHQIC(ll, df_model, numObs);

The code above results in the following:

::

  hqic = 79.82

Source
------

ssmain.src

.. seealso:: Functions :func:`ssgetAICC`, :func:`ssgetBIC`, :func:`ssgetAIC`
