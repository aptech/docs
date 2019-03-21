
olsqr
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: olsqr(y, x)

    :param y: 
    :type y: Nx1 vector containing dependent variable

    :param x: 
    :type x: NxP matrix containing independent variables

    :returns: b (*TODO*), Px1 vector of least squares estimates of
        regression of y on x. If x does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

Remarks
-------

This provides an alternative to y/x for computing least squares
coefficients.

This procedure is slower than the / operator. However, for near singular
matrices it may produce better results.

olsqr handles matrices that do not have full rank by returning zeros for
the coefficients that cannot be estimated.


Examples
----------------

::

    A = rndn(4,4);
    b = rndn(4,1);
    x = olsqr(b,A);

.. seealso:: Functions :func:`ols`, :func:`olsqr2`, :func:`orth`, :func:`qqr`

ols least square regression linear coefficients QR decomposition
