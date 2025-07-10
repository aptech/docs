gradcorcov
==============================================

Purpose
----------------

Computes gradients for transforming a correlation matrix back to covariance parameters.

Format
----------------
.. function:: { gBcorcov, gomegacorcov } = gradcorcov(C, litomega, omegastar)

    :param C: Scaled variable vector.
    :type C: Kx1 vector

    :param litomega: Standard deviations.
    :type litomega: Kx1 vector

    :param omegastar: Correlation matrix.
    :type omegastar: KxK matrix

    :return gBcorcov: Gradient matrix of scaled variables w.r.t covariance elements.
    :rtype gBcorcov: matrix

    :return gomegacorcov: Gradient matrix of correlation elements w.r.t covariance elements.
    :rtype gomegacorcov: matrix

Library
-------
bhatlib

Source
------
matgradient.src