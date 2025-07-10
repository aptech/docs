gbothxomegax
==============================================

Purpose
----------------

Computes gradients of A = X * CAPOMEGA * X' with respect to both X and CAPOMEGA elements.

Format
----------------
.. function:: { gx1cov, gx2cov } = gbothxomegax(x1, x2)

    :param x1: Data matrix X.
    :type x1: NxK matrix

    :param x2: CAPOMEGA matrix.
    :type x2: KxK matrix

    :return gx1cov: Gradient matrix w.r.t X.
    :rtype gx1cov: matrix

    :return gx2cov: Gradient matrix w.r.t CAPOMEGA.
    :rtype gx2cov: matrix

Library
-------
bhatlib

Source
------
matgradient.src