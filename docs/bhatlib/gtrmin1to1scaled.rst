gtrmin1to1scaled
==============================================
Purpose
----------------
Computes the scaled trmin1to1 transformation and its gradient.

Format
----------------
.. function:: { s, gs, gss } = gtrmin1to1scaled(sstar, scal)

    :param sstar: Input data vector.
    :type sstar: vector

    :param scal: Scaling parameter.
    :type scal: scalar

    :return s: Transformed vector.
    :rtype s: vector

    :return gs: Gradient with respect to sstar.
    :rtype gs: vector

    :return gss: Second-order gradient component.
    :rtype gss: vector

Library
-------
bhatlib

Source
------
vecup.src