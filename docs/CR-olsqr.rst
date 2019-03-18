
olsqr
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: olsqr(y, x)

    :param y: Nx1 vector containing dependent variable.
    :type y: TODO

    :param x: NxP matrix containing independent variables.
    :type x: TODO

    :returns: b (*TODO*), Px1 vector of least squares estimates of
        regression of y on x. If x does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

Examples
----------------

::

    A = rndn(4,4);
    b = rndn(4,1);
    x = olsqr(b,A);

.. seealso:: Functions :func:`ols`, :func:`olsqr2`, :func:`orth`, :func:`qqr`

ols least square regression linear coefficients QR decomposition
