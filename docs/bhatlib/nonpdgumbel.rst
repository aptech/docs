nonpdgumbel
==============================================
Purpose
----------------
Computes the non-probability density (complement) for the Gumbel distribution.

Format
----------------
.. function:: npdf = nonpdgumbel(x, mu, beta)

    :param x: Evaluation point(s).
    :type x: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar

    :param beta: Scale parameter.
    :type beta: scalar

    :return npdf: Computed non-PDF value.
    :rtype npdf: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src