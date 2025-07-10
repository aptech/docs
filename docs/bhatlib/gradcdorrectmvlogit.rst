gradcdorrectmvlogit
==============================================

Purpose
----------------

Simulates error term realizations for the MDCEV model, where a represents v-tilde values for inside goods, and m specifies the number of consumed inside goods. 

Format
----------------
.. function:: { F, gmu, gsig, gxg, gx1, gx2 } = gradcdorrectmvlogit(mu, sig, xg, x1, x2, indxone, indxcomp)


    :param mu: (K x 1) vector of location parameters.
    :type mu: (Specify type)
    :param sig: (K x 1) vector of scale parameters.
    :type sig: (Specify type)
    :param xg: (K x 1) vector of truncation points for one-sided orthant integrals.
    :type xg: (Specify type)
    :param x1: (K x 1) vector of lower truncation points for rectangular integrals.
    :type x1: (Specify type)
    :param x2: (K x 1) vector of upper truncation points for rectangular integrals.
    :type x2: (Specify type)
    :param indxone: (K x 1) binary vector where:
    :type indxone: (Specify type)
    :param indxcomp: (K x 1) binary vector where:
    :type indxcomp: (Specify type)

    :return F: (1 x 1) scalar, representing the computed probability.
    :rtype F: (Specify type)
    :return gmu: (K x 1) vector of gradients of F with respect to the location parameters (mu).
    :rtype gmu: (Specify type)
    :return gsig: (K x 1) vector of gradients of F with respect to the scale parameters (sig).
    :rtype gsig: (Specify type)
    :return gxg: (K x 1) vector of gradients of F with respect to one-sided truncation points.
    :rtype gxg: (Specify type)
    :return gx1: (K x 1) vector of gradients of F with respect to lower truncation points.
    :rtype gx1: (Specify type)
    :return gx2: (K x 1) vector of gradients of F with respect to upper truncation points.
    :rtype gx2: (Specify type)


Source
------------

gradients-mvn.src
