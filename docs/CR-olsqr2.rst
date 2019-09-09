
olsqr2
==============================================

Purpose
----------------

Computes OLS coefficients, residuals, and predicted values using the QR decomposition.

Format
----------------
.. function:: { b, r, p } = olsqr2(depvar, indepvars)

    :param depvar: dependent variable
    :type depvar: Nx1 vector

    :param indepvars: independent variables
    :type indepvars: NxP matrix

    :return b: least squares estimates of
        regression of *y* on *x*. If *x* does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :rtype b: Px1 vector

    :return r: OLS residuals. (:math:`r = y - x*b`)

    :rtype r: Px1 vector

    :return p: predicted values. (:math:`p = x*b`)

    :rtype p: Px1 vector

Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices, it may produce better results.

The :func:`olsqr2` procedure handles matrices that do not have full rank by returning zeros
for the coefficients that cannot be estimated.

.. seealso:: Functions :func:`olsqr`, :func:`orth`, :func:`qqr`
