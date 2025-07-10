gradcovcor
==============================================

Purpose
----------------

Computes gradients for transforming a covariance matrix to a correlation matrix.

Format
----------------
.. function:: { gBcorcov, gomegacorcov } = gradcovcor(capomega)

    :param capomega: Covariance matrix.
    :type capomega: KxK matrix

    :return gBcorcov: Gradients of scaled variables with respect to covariance elements.
    :rtype gBcorcov: matrix

    :return gomegacorcov: Gradients of correlation elements with respect to covariance elements.
    :rtype gomegacorcov: matrix

Library
-------
bhatlib

Source
------
matgradient.src