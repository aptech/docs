
ssgetAIC
==============================================

Purpose
----------------

Computes Akaike's information criterion from loglikelihood.

Format
----------------
.. function:: aic = ssgetAIC(loglikelihood, df)

    :param loglikelihood: Loglikelihood value.
    :type loglikelihood: Scalar

    :param df: Degrees of freedom.
    :type df: Scalar

    :return aic: Computed Akaike's information criterion
    :rtype aic: Scalar

Examples
----------------

::

  // Loglikelihood value
  ll = -38.3;

  // Degrees of freedom
  df_model = 2;

  // Compute AIC
  aic = ssgetAIC(ll, df_model);

The code above results in the following:

::

  aic = 80.6

Source
------

ssmain.src

.. seealso:: Functions :func:`ssgetAICC`, :func:`ssgetBIC`, :func:`ssgetHQIC`
