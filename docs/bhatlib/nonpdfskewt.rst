nonpdfskewt
==============================================
Purpose
----------------
Computes the non-probability density function for the skew-t distribution.

Format
----------------
.. function:: npdf = nonpdfskewt(x, alpha, nu)

    :param x: Evaluation points.
    :type x: scalar or vector

    :param alpha: Skewness parameter.
    :type alpha: scalar

    :param nu: Degrees of freedom.
    :type nu: scalar

    :return npdf: Computed non-PDF values.
    :rtype npdf: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src