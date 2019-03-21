
olsqr2
==============================================

Purpose
----------------

Computes OLS coefficients, residuals, and predicted values using the QR decomposition.

Format
----------------
.. function:: olsqr2(y, x)

    :param y: 
    :type y: Nx1 vector containing dependent variable

    :param x: 
    :type x: NxP matrix containing independent variables

    :returns: b (*TODO*), Px1 vector of least squares estimates of
        regression of y on x. If x does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :returns: r (*TODO*), Px1 vector of residuals. (r = y - x*b)

    :returns: p (*TODO*), Px1 vector of predicted values. (p = x*b)



Remarks
-------

This provides an alternative to y/x for computing least squares
coefficients.

This procedure is slower than the / operator. However, for near singular
matrices, it may produce better results.

olsqr2 handles matrices that do not have full rank by returning zeros
for the coefficients that cannot be estimated.

