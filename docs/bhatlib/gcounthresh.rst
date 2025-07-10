gcounthresh
==============================================
Purpose
----------------
Computes the gradient of the cumulative distribution function for count thresholds.

Format
----------------
.. function:: { dpsi_dlambda, dpsi_dtheta, dpsi_dalpha } = gcounthresh(lambda, theta, countvector, alphavector, _poisson)

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

    :return dpsi_dlambda: Gradient with respect to lambda.
    :rtype dpsi_dlambda: scalar

    :return dpsi_dtheta: Gradient with respect to theta.
    :rtype dpsi_dtheta: scalar

    :return dpsi_dalpha: Gradient with respect to alpha vector.
    :rtype dpsi_dalpha: vector

Library
-------
bhatlib

Source
------
vecup.src