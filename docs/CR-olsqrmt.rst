
olsqrmt
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: olsqrmt(y, x,  tol)

    :param y: Nx1 vector containing dependent variable.
    :type y: TODO

    :param x: NxP matrix containing independent variables.
    :type x: TODO

    :param tol: the tolerance for testing if
        diagonal elements are approaching zero. The
        default value is 10-14.
    :type tol: scalar

    :returns: b (*TODO*), Px1 vector of least squares estimates of
        regression of y on x. If x does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

