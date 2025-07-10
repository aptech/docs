gcmlpanel
==============================================
Purpose
----------------
Computes the gradient for panel data composite marginal likelihood estimation.

Format
----------------
.. function:: { g1, g2, g3, g4 } = gcmlpanel(nchoc, nc, Msubq, vsubq, xisubq, seed)

    :param nchoc: Number of choices.
    :type nchoc: scalar

    :param nc: Number of clusters.
    :type nc: scalar

    :param Msubq: Submatrix M.
    :type Msubq: matrix

    :param vsubq: Subvector v.
    :type vsubq: vector

    :param xisubq: Submatrix xi.
    :type xisubq: matrix

    :param seed: Random seed.
    :type seed: scalar

    :return g1: Gradient output 1.
    :rtype g1: matrix

    :return g2: Gradient output 2.
    :rtype g2: matrix

    :return g3: Gradient output 3.
    :rtype g3: matrix

    :return g4: Gradient output 4.
    :rtype g4: matrix

Library
-------
bhatlib

Source
------
matgradient.src