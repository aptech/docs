gyjinv
==============================================
Purpose
----------------
Computes the gradient of the inverse Yeo-Johnson transformation.

Format
----------------
.. function:: { glam, gmu, gw, gx, gy } = gyjinv(mu, wdiag, lamnew, x)

    :param mu: Location parameter vector.
    :type mu: vector

    :param wdiag: Diagonal weights.
    :type wdiag: vector

    :param lamnew: Lambda parameter (logit transformed).
    :type lamnew: scalar or vector

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