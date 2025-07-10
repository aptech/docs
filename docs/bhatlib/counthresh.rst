counthresh
==============================================
Purpose
----------------
Computes the cumulative distribution function for count thresholds under negative binomial or Poisson assumptions.

Format
----------------
.. function:: psi = counthresh(lambda, theta, countvector, alphavector, _poisson)

    :param lambda: Mean parameter.
    :type lambda: scalar

    :param theta: Overdispersion parameter.
    :type theta: scalar

    :param countvector: Vector of count values.
    :type countvector: vector

    :param alphavector: Alpha vector for model.
    :type alphavector: vector

    :param _poisson: Poisson indicator flag (0 = negative binomial, 1 = Poisson).
    :type _poisson: scalar

    :return psi: Computed cumulative distribution function value.
    :rtype psi: scalar

Library
-------
bhatlib

Source
------
vecup.src