
olsqrmt
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: olsqrmt(y, x, tol)

    :param y: dependent variable
    :type y: Nx1 vector

    :param x: independent variables
    :type x: NxP matrix

    :param tol: the tolerance for testing if diagonal elements are approaching zero. 
        The default value is 10-14.
    :type tol: scalar

    :returns: b (*Px1 vector*) of least squares estimates of
        regression of *y* on *x*. If *x* does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices it may produce better results.

:func:`olsqrmt` handles matrices that do not have full rank by returning zeros
for the coefficients that cannot be estimated.

Source
------

olsmt.src

.. seealso:: Functions :func:`olsmt`, :func:`olsqr2`

