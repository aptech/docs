
olsqr2
==============================================

Purpose
----------------

Computes OLS coefficients, residuals, and predicted values using the QR decomposition.

Format
----------------
.. function:: { b, r, p } = olsqr2(y, x)

    :param y: dependent variable
    :type y: Nx1 vector

    :param x: independent variables
    :type x: NxP matrix

    :returns: b (*Px1 vector*) of least squares estimates of
        regression of *y* on *x*. If *x* does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :returns: r (*Px1 vector*) of residuals. (:math:`r = y - x*b`)

    :returns: p (*Px1 vector*) of predicted values. (:math:`p = x*b`)



Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices, it may produce better results.

:func:`olsqr2` handles matrices that do not have full rank by returning zeros
for the coefficients that cannot be estimated.

.. seealso:: Functions :func:`olsqr`, :func:`orth`, :func:`qqr`

