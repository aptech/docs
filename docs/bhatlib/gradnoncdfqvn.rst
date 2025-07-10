gradnoncdfqvn
==============================================
Purpose
----------------
Computes the gradient of the non-CDF quadrivariate normal function.

Format
----------------
.. function:: grad = gradnoncdfqvn(w, cor)

    :param w: Evaluation points.
    :type w: 4xN matrix

    :param cor: Correlation matrix.
    :type cor: 4x4 matrix

    :return grad: Computed gradient.
    :rtype grad: matrix

Library
-------
bhatlib

Source
------
gradients-mvn.src