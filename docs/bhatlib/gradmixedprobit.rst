gradmixedprobit
==============================================
Purpose
----------------
Computes the gradient for a mixed probit model likelihood.

Format
----------------
.. function:: { gb, gd, gLsubtau, gLsubtaufinal } = gradmixedprobit(xsubq, zsubq, Msubq, b, c, Lsubtau, theta, lambda)

    :param xsubq: Submatrix of independent variables for fixed effects.
    :type xsubq: matrix

    :param zsubq: Submatrix of independent variables for random effects.
    :type zsubq: matrix

    :param Msubq: Selection or differencing matrix.
    :type Msubq: matrix

    :param b: Coefficient vector for fixed effects.
    :type b: vector

    :param c: Constant vector.
    :type c: vector

    :param Lsubtau: Lower triangular Cholesky factor matrix.
    :type Lsubtau: matrix

    :param theta: Random coefficients.
    :type theta: vector

    :param lambda: Vector for thresholding.
    :type lambda: vector

    :return gb: Gradient with respect to b.
    :rtype gb: vector

    :return gd: Gradient with respect to d.
    :rtype gd: vector

    :return gLsubtau: Gradient with respect to Lsubtau.
    :rtype gLsubtau: matrix

    :return gLsubtaufinal: Final gradient with respect to Lsubtau.
    :rtype gLsubtaufinal: matrix

Library
-------
bhatlib

Source
------
matgradient.src