gradcdfqvn
==============================================

Purpose
----------------

Develops gradients with respect to the standard approximated quadrivariate normal cumulative function

Format
----------------
.. function:: { gw,grho } = gradcdfqvn(w,cor)

    :param w: Abscissae, where K corresponds to the number of variates and Q corresponds to the number of observations.
    :type w: (KxQ) matrix

    :param cor: Correlation matrix.
    :type cor: (KxK) matrix

    :return gw: Gradient with respect to `w`.
    :rtype gw: (KxQ) matrix

    :return grho: Gradient with respect to `cor`.
    :rtype grho: (KxK) matrix

Source
------------

gradients-mvn.src
