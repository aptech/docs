
olsqr2
==============================================

Purpose
----------------

Computes OLS coefficients, residuals, and predicted values using the QR decomposition.

Format
----------------
.. function:: olsqr2(y, x)

    :param y: Nx1 vector containing dependent variable.
    :type y: TODO

    :param x: NxP matrix containing independent variables.
    :type x: TODO

    :returns: b (*TODO*), Px1 vector of least squares estimates of
        regression of y on x. If x does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :returns: r (*TODO*), Px1 vector of residuals. (r = y - x*b)

    :returns: p (*TODO*), Px1 vector of predicted values. (p = x*b)

