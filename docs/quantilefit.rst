
quantileFit
==============================================

Purpose
----------------
Perform linear quantile regression.

Format
----------------
.. function:: qOut = quantileFit(y, x[, tau[, w]], [qCtl])
              qOut = quantileFit(dataset, formula[, tau[, w]], [qCtl])

    :param y: dependent variable.
    :type y: Nx1 vector

    :param x: independent variables.
    :type x: NxK matrix or sparse matrix or N-dimensional array

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: formula string of the model.

        E.g ``"y ~ X1 + X2"``, 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables;

        E.g ``"y ~ ."``, '.' means including all variables except dependent variable 'y';

        E.g ``"y ~ -1 + X1 + X2"``, '-1' means no intercept model.

    :type formula: string

    :param tau: Optional argument, quantile levels. Default = { 0.05, 0.5, 0.95 };
    :type tau: Mx1 vector

    :param w: Optional argument, containing weights. Default = uniform weights.
    :type w: Nx1 vector

    :param qCtl: Optional argument, instance of the :class:`qfitControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - qCtl.bandwidth
              - scalar, the multiplicative factor of the bandwidth. Default = 1.
            * - qCtl.varnames
              - Kx1 string array, variable names. Default = ``{"X1", "X2", ..., "XK"}``.
                The name for the constant will be added automatically if it is included in the model.
            * - qCtl.verbose
              - scalar, print results Default = 1.

                :1: Printing on.
                :0: No printing.

            * - qCtl.const
              - scalar, include constant in regression. Default = 1.

                :1: a constant term will be added.
                :0: no constant term will be added.

            * - qCtl.bootstrap
              - scalar, number of iterations for bootstrap standard errors and confidence intervals. Default = 0, for no bootstrap.
            * - qCtl.alpha
              - scalar, alpha values for bootstrap confidence intervals. Ignored if *qctl.bootstrap* is set to 0.

    :type qCtl: struct

    :return qOut: instance of :class:`qfitOut` struct structure:

        .. csv-table::
            :widths: auto

            "qOut.beta", "Kx1 matrix, quantile parameter estimates."
            "qOut.u_plus", "NxM matrix, positive part of residuals."
            "qOut.u_minus", "NxM matrix, negative part of residuals."
            "qOut.ci", "array, with a 2xK matrix containing bootstrapped lower and upper confidence intervals stored on separate planes for each tau specified."
            "qOut.se", "matrix, with bootstrapped standard errors, stored in separate columns for each tau specified."

    :rtype qOut: struct

Examples
----------------

::

    new;
    cls;

    // Set random number generator seed for
    // repeatable random numbers
    rndseed 4893;

    N = 1000;
    x = 10*rndu(N, 1) - 5;
    y = 5 + 2*X + rndn(rows(x), 1)*10;

    // Set up tau for regression
    tau = 0.05|0.50|0.75|0.95;

    // Call quantileFit
    struct qfitOut qOut;
    qOut = quantileFit(Y, X, tau);

Source
------

quantilefit.src

.. seealso:: Functions :func:`glm`, :func:`olsmt`, :func:`quantileFitLoc`
