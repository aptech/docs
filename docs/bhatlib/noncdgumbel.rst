noncdgumbel
==============================================
Purpose
----------------
Computes the non-cumulative (survival function) of the Gumbel distribution.

Format
----------------
.. function:: sf = noncdgumbel(x, mu, beta)

    :param x: Evaluation point(s).
    :type x: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar

    :param beta: Scale parameter.
    :type beta: scalar

    :return sf: Survival function evaluated at x.
    :rtype sf: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src