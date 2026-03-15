
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

Examples
----------------

::

    // Random matrices
    x = rndn(4, 4);
    y = rndn(4, 1);

    // Solve OLS coefficient using QR decomposition
    b = olsqr(y, x);

.. note:: This example uses a square system (4 equations, 4 unknowns), which has an exact solution rather than a least squares fit. In practice, :func:`olsqr` is most useful when the system is overdetermined (more observations than parameters), where it computes the least squares solution.

Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices it may produce better results.

The :func:`olsqr` procedure handles matrices that do not have full rank by returning zeros for
the coefficients that cannot be estimated.


.. seealso:: Functions :func:`ols`, :func:`olsqr2`, :func:`orth`, :func:`qqr`
