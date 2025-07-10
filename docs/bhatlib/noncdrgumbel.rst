noncdrgumbel
==============================================
Purpose
----------------
Computes the survival function (1-CDF) of the reversed Gumbel distribution.

Format
----------------
.. function:: sf = noncdrgumbel(x, mu, beta)

    :param x: Evaluation points.
    :type x: scalar or vector

    :param mu: Location parameter.
    :type mu: scalar

    :param beta: Scale parameter.
    :type beta: scalar

    :return sf: Computed survival function values.
    :rtype sf: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src