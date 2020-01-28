
olsqrmt
==============================================

Purpose
----------------

Computes OLS coefficients using QR decomposition.

Format
----------------
.. function:: b = olsqrmt(depvars indepvars, tol)

    :param depvar: dependent variable
    :type depvar: Nx1 vector

    :param indepvars: independent variables
    :type indepvars: NxP matrix

    :param tol: the tolerance for testing if diagonal elements are approaching zero.
        The default value is 10-14.
    :type tol: scalar

    :return b: least squares estimates of
        regression of *depvar* on *indepvars*. If *indepvars* does not have full
        rank, then the coefficients that cannot be
        estimated will be zero.

    :rtype b: Px1 vector

Examples
----------------

::

            rndseed 129727134;

            // Assign random matrices
            x = rndn(150, 4);
            y = rndn(150, 1);

            // Set tolerance
            tol = 1E-10;

            // Solve OLS coefficient using QR decomposition
            { b, r, p } = olsqrmt(y, x, tol);

Remarks
-------

This provides an alternative to :math:`y/x` for computing least squares
coefficients.

This procedure is slower than the ``/`` operator. However, for near singular
matrices it may produce better results.

The :func:`olsqrmt` procedure handles matrices that do not have full rank by returning zeros
for the coefficients that cannot be estimated.

Source
------

olsmt.src

.. seealso:: Functions :func:`olsmt`, :func:`olsqr2`
