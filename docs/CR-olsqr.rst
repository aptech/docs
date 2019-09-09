
olsqr
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: b = olsqr(depvar, indepvars)

    :param depvar: dependent variable
    :type depvar: Nx1 vector

    :param indepvars: independent variables
    :type indepvars: NxP matrix

    :return b: least squares estimates of
        regression of *depvar* on *indepvars*. If *depvar* does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :rtype b: Px1 vector

Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices it may produce better results.

The :func:`olsqr` procedure handles matrices that do not have full rank by returning zeros for
the coefficients that cannot be estimated.


Examples
----------------

::

    A = rndn(4, 4);
    b = rndn(4, 1);

    // Solve OLS coefficient using QR decomposition
    x = olsqr(b, A);

.. seealso:: Functions :func:`ols`, :func:`olsqr2`, :func:`orth`, :func:`qqr`
