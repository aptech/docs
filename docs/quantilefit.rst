
quantileFit
==============================================

Purpose
----------------
Perform linear quantile regression.

Format
----------------
.. function:: qOut = quantileFit(y, x [, tau, w, qCtl])
              qOut = quantileFit(dataset, formula [, tau, w, qCtl])
              qOut = quantileFit(dataframe, formula [, tau, w, qCtl])

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

            * - qCtl.vce_method
              - scalar, method to use for calculating the asymptotic covariance matrix. Default = 1.

                :1: IID errors.
                :2: heteroskedasticity robust standard errors.

            * - qCtl.bw_method
              - scalar, method to use for calculating the bandwidth for the asymptotic covariance matrix computation. Default = 1.

                :1: Hall-Sheather bandwidth.
                :2: Bofinger bandwidth.
                :3: Chamberlain bandwidth.

            * - qCtl.vce_kernel
              - scalar,kernel to use for calculating the asymptotic covariance matrix computation. Default = 1.

                :1: Normal(Gaussian).
                :2: Epanechnikov.
                :3: Biweight.
                :4: Parzen.
                :5: Cosine.

           * - qCtl.bootstrap
             - scalar, number of iterations for bootstrap standard errors and confidence intervals. Default = 0, for no bootstrap.
           * - qCtl.alpha
              - scalar, alpha values for bootstrap confidence intervals.

    :type qCtl: struct

    :return qOut: instance of :class:`qfitOut` struct structure:

        .. csv-table::
            :widths: auto

            "qOut.beta", "KxM matrix, quantile parameter estimates, with estimates for each tau stored in a separate column."
            "qOut.u_plus", "NxM matrix, positive part of residuals."
            "qOut.u_minus", "NxM matrix, negative part of residuals."
            "qOut.vce", "array, with a KxK matrix estimated asymptotic covariance matrix stored on separate plane for each tau specified."
            "qOut.vce_ci", "array, with a 2xK matrix containing lower and upper confidence intervals based on asymptotic covariance estimates stored on separate planes for each tau specified."
            "qOut.vce_se", "matrix, with estimated asymptotic standard errors, stored in separate columns for each tau specified."
            "qOut.ci", "array, with a 2xK matrix containing bootstrapped lower and upper confidence intervals stored on separate planes for each tau specified."
            "qOut.se", "matrix, with bootstrapped standard errors, stored in separate columns for each tau specified."
            "qOut.t", "KxM matrix, with estimate t-values based on asymptotic standard errors. Estimates for each tau are stored in separate columns."
            "qOut.pvt", "KxM matrix, with p-values for estimated t-values. Estimates for each tau are stored in separate columns."
            "qOut.number_obs", "Scalar, number of observations used in estimation."
            "qOut.number_missing", "Scalar, number of missing values eliminated from original data."
            "qOut.df_residuals", "Scalar, residual degrees of freedom."
            "qOut.df_model", "Scalar, model degrees of freedom."
            "qOut.h", "Vector, bandwidth used in asymptotic variance estimation. Values for each tau are stored in separate columns."
            "qOut.sparsity", "Vector, sparsity used in asymptotic variance estimation. Values for each tau are stored in separate columns."

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
    tau = 0.05;

    // Call quantileFit
    struct qfitOut qOut;
    qOut = quantileFit(Y, X, tau);

This produces the following output

::

  =====================================================================================
  Valid cases:                   1000                Dependent variable:              Y
  Missing cases:                    0                   Deletion method:           None
  Number variables:                 1                           DF model              1
  DF residuals                    998
  =====================================================================================

                     Name    Coeff.  Standard   t-value    P >|t|        lb        ub
                                        Error
 -------------------------------------------------------------------------------------
 Tau = 0.05

                 CONSTANT  -11.6768    0.5542  -21.0713    0.0000  -12.7629  -10.5907
                       X1    1.6790    0.1885    8.9059    0.0000    1.3095    2.0485


Source
------

quantilefit.src

.. seealso:: Functions :func:`glm`, :func:`olsmt`, :func:`quantileFitLoc`
