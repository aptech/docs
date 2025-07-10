gradunivariatenormaltrunc
==============================================
Purpose
----------------
Computes the gradients of the mean and variance of a truncated univariate normal distribution with respect to its parameters.

Format
----------------
.. function:: { dmu, dsigma } = gradunivariatenormaltrunc(mu_untrunc, sigma_untrunc, trpoint)

    :param mu_untrunc: Untruncated mean.
    :type mu_untrunc: scalar

    :param sigma_untrunc: Untruncated variance.
    :type sigma_untrunc: scalar

    :param trpoint: Truncation point.
    :type trpoint: scalar

    :return dmu: Gradient of the truncated mean.
    :rtype dmu: scalar

    :return dsigma: Gradient of the truncated variance.
    :rtype dsigma: scalar

Library
-------
bhatlib

Source
------
vecup.src