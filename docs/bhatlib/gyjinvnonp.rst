gyjinvnonp
==============================================
Purpose
----------------
Computes the gradient of the nonparametric inverse Yeo-Johnson transformation.

Format
----------------
.. function:: { glam, gmu, gw, gx, gy } = gyjinvnonp(mu, wdiag, lamnonp, x)

    :param mu: Location parameter vector.
    :type mu: vector

    :param wdiag: Diagonal weights.
    :type wdiag: vector

    :param lamnonp: Lambda parameter (nonparametric).
    :type lamnonp: scalar or vector

    :param x: Input data vector.
    :type x: vector

    :return glam: Gradient with respect to lambda.
    :rtype glam: vector

    :return gmu: Gradient with respect to mu.
    :rtype gmu: matrix

    :return gw: Gradient with respect to weights.
    :rtype gw: vector

    :return gx: Gradient with respect to x.
    :rtype gx: matrix

    :return gy: Gradient output vector.
    :rtype gy: vector

Library
-------
bhatlib

Source
------
vecup.src