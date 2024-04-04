arfac
=============

Purpose
-------
This procedure finds the coefficients (phi) for the factors of a dynamic factor model.

Format
------
.. function:: { phi, accept } = arfac(y, p, r0_, R0__, phi0, xvar, sig2)

    :param y: Current draw for factor.
    :type y: Matrix

    :param p: Number of autoregressive terms on factor.
    :type p: Scalar

    :param r0_: Prior mean of phi.
    :type r0_: Matrix

    :param R0__: Prior precision of phi.
    :type R0__: Matrix

    :param phi0: Previous draw of phi.
    :type phi0: Matrix

    :param xvar: Number of independent variables (including constant).
    :type xvar: Scalar

    :param sig2: Initial :math:`\sigma^2` value for factor.
    :type sig2: Matrix

    :return phi1: Current draw of phi.
    :rtype phi1: Matrix

    :return accept: Indicator variable used intrinsically.
    :rtype accept: Scalar
