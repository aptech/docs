
gmmFit
==============================================

Purpose
----------------

Estimate parameters using generalized method of moments.

Format
----------------
.. function:: gOut = gmmFit(&fct, y[, ...[, gCtl]])

    :param &fct: Pointer to user specified moment equation function *&fct*. The function must have the parameter vector to be estimated as the first input and a data matrix as the second input. The data matrix *y* and all optional arguments are passed, untouched, directly to the moment function. The function *fct* should return the desired moments for the GMM objective function and should take the form:

    ::

        m = fct(b, y, ...);

    :type &fct: function pointer

    :param y: data passed to the moment function as its second argument.
    :type y: Nx1 matrix

    :param \.\.\.: Optional inputs. These arguments are passed untouched to the user-provided moment function by :func:`gmmFit`.
    :type \.\.\.: Any

    :param gCtl: Optional argument, an instance of an :class:`gmmControl` structure. The following members of gCtl* are referenced within the :func:`gmmFit` routine:

        .. list-table::
            :widths: auto

            * - gCtl.bStart
              - column vector of parameter starting values. For all methods except continuous updating GMM default = 0.1. For continuous updating GMM default equals estimation from onestep GMM. Must be specified if data matrix syntax is used and *gCtl.numParams* is not specified. For estimation stability it is highly recommended to specify starting parameters.
            * - gCtl.method
              - string, GMM method to be used. Default = :code:`"twostep"`. The names are not case sensitive; any other name stops with an error.

                  :"onestep": One-step GMM
                  :"twostep": Two-step GMM
                  :"iterative": Iterative GMM (or :code:`"iterated"`)
                  :"CU": Continuous updating GMM. It starts from the one-step estimate. For a just-identified model with no constraints other than bounds, whose one-step estimate has mean moments of zero (no active bound), it returns that estimate, which also minimizes the CU objective; if they are not zero and the one-step fit did not converge, *gOut.converged* is 0. Otherwise, if the moment variance at the CU estimate is nearly singular, *gOut.converged* is 0.
            * - gCtl.vceType
              - string, variance-covariance matrix type. Default = :code:`"robust"`. Any other name stops with an error.

                  :"unadj": Not available in :func:`gmmFit`, which uses :code:`"robust"` instead. Use :func:`gmmFitIV` for the unadjusted covariance of a linear model.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.
            * - gCtl.wType
              - string, type of weight matrix used. Ignored for one-step case. Default = :code:`"robust"`. Any other name stops with an error.

                  :"unadj": Not available in :func:`gmmFit`, which uses :code:`"robust"` instead.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.
            * - gCtl.hacKernel
              - string, type of kernel used for estimation of HAC robust weight matrix and/or variance-covariance matrix. Ignored if not using :code:`"hac"` weight matrix and/or variance-covariance matrix. Unless *gCtl.gmmlags* is set, the bandwidth is chosen by the Newey-West (1994) method from the sum of the moment conditions, without prewhitening. It depends on the units of the moments and does not reproduce Stata's automatic bandwidth. The bandwidth of the weight matrix is chosen once, at the first-step estimate (for continuously updated GMM, at the one-step start), and kept for every weight matrix of the fit, for *gOut.wFinal* and for the J statistic; the HAC variance-covariance matrix chooses its own bandwidth at the final estimate. Default = :code:`"bartlett"`.

                  :"bartlett": Bartlett kernel.
                  :"parzen": Parzen kernel.
                  :"quad": Quadratic spectral kernel. It uses every lag, so its cost grows with the square of the number of observations.
            * - gCtl.gmmlags
              - scalar, user specified bandwidth for the HAC weight matrix and variance. For the Bartlett and Parzen kernels it is the number of lags: lags 1 to the integer part *L* of *gmmlags* are used, with weights :math:`k(j/(L+1))`. For the quadratic spectral kernel it is the bandwidth, and every lag is used, with weights :math:`k(j/gmmlags)`. 0 gives the robust (no lags) result. Must be a finite scalar of 0 or more. Default = empty, the Newey-West automatic bandwidth.
            * - gCtl.wInitMat
              - data matrix, initial weight matrix to be used. If specified the matrix is used as initial weighting matrix and overrides specification of *gCtl.wInit*. It must be symmetric positive definite, with one row and column per moment.
            * - gCtl.wInit
              - string or data matrix, type of initial weight matrix used. If data matrix, the specified matrix is used as initial weighting matrix. Default = :code:`"identity"`. Any other name stops with an error.

                  :"identity": Identity matrix.
                  :"unadj": Not available in :func:`gmmFit`, which uses the identity matrix instead.
            * - gCtl.gIter
              - instance of :class:`gmmIterative` structure. This structure houses the tolerances for convergence for iterative GMM. Ignored if iterative GMM is not specified. The members include:

                  :gCtl.gIter.maxIters: scalar, maximum number of iterations, at least 1. Default = 500.
                  :gCtl.gIter.paramTol: scalar, tolerance for the largest relative change in the parameter estimates. Default = 1e-6.
                  :gCtl.gIter.wTol: scalar, tolerance for the relative change in the weight matrix (Frobenius norm). Default = 1e-6.

            * - gCtl.jStatWeight
              - string, weight matrix used in the J statistic of two-step and iterative GMM. Default = :code:`"final"`.

                  :"final": The weight matrix of type *wType* at the final estimate, as R's momentfit.
                  :"estimation": The weight matrix used to compute the final estimate (*N* times the objective), as Stata. The two agree for iterative GMM once it has converged.
            * - gCtl.noconstant
              - scalar, specified to indicate if constant is included in model. Only valid if data vector input method is used. Set to 1 to exclude constant from model. Constant is always first parameter in parameter vector. Default = 0 [constant included].For dataset and string formula method to remove constant from model specify :code:`"-1"` as first dependent variable: e.g. : :code:`"y ~ -1 + X1 + X2"`
            * - gCtl.varNames
              - string array, dependent variable names. Only used for data vector input case. Default = :code:`"X1", "X2", ...`
            * - gCtl.instNames
              - string array, instrumental variable names. Only used for data vector input case. Default = :code:`"Z1", "Z2", ...`
            * - gCtl.numParams
              - scalar, number of parameters estimated in model. Must be specified if data matrix syntax is used and *gCtl.bStart* is not specified.
            * - gCtl.A
              - MxK matrix, linear equality constraint coefficients: :code:`gctl.A * p = gctl.B` where *p* is a vector of the parameters.
            * - gCtl.B
              - Mx1 vector, linear equality constraint constants: :code:`gctl.A * p = gctl.B` where *p* is a vector of the parameters.
            * - gCtl.C
              - MxK matrix, linear inequality constraint coefficients: :code:`gctl.C * p >= gctl.D` where *p* is a vector of the parameters.
            * - gCtl.D
              - Mx1 vector, linear inequality constraint constants: :code:`gctl.C * p >= gctl.D` where *p* is a vector of the parameters.
            * - gCtl.bounds
              - 1x2 or Kx2 matrix, bounds on parameters. If 1x2 all parameters have same bounds. Default = :code:`{ -1e256 1e256 }`.

    :type gCtl: struct

    :return gOut: instance of :class:`gmmOut` struct containing the following members:

        .. csv-table::
            :widths: auto

            "gOut.parEst", "column vector of final estimates. Constant, if included in model, is the first element."
            "gOut.wFinal", "matrix, final weighting matrix."
            "gOut.covPar", "matrix, estimated variance-covariance matrix."
            "gOut.fct", "vector, mean value of the moment equations."
            "gOut.hessian", "matrix, Hessian of mean of moment equation wrt parameters."
            "gOut.gradient", "matrix, Gradient of mean of moment equation wrt parameters."
            "gOut.numParams", "scalar, number of parameters estimated in model."
            "gOut.numMoments", "scalar, number of moments."
            "gOut.numObs", "scalar, number of observations: the number of rows the moment function returns."
            "gOut.numInstruments", "scalar, number of instruments."
            "gOut.JStat", "scalar, Hansen statistic of overidentification. Missing for one-step GMM and just-identified models. See gCtl.jStatWeight."
            "gOut.df", "scalar, degrees of freedom."

    :rtype gOut: struct

Examples
----------------

Use data matrices
+++++++++++++++++++

::

    new;
    rndseed 12576;

    /*
    ** Simulate t distribution data
    ** degrees of freedom
    */
    df = 10;

    // Covariance matrix [columns are independent]
    sigma = { 1 0,
              0 1 };

    // Number of observations
    num = 500;

    // Generate data
    y = rndMVt(num, sigma, df);

    // Just use one of x's
    yt = y[., 1];

    struct gmmControl gctl;
    gctl = gmmControlCreate();

    /*
    ** Set starting values
    ** This or number of parameters must
    ** be specified if no x mats
    */
    gctl.bStart = 7;

    // Continuous estimation
    struct gmmOut gOut1;
    gOut1 = gmmFit(&meqn, yt, gctl);

    /*
    ** User defined moment equation
    ** Use the y2 and y4 as moments
    */
    proc (1) = meqn(b, yt);
        local g1,g2;

        g1 = yt.^2 - b/(b-2);
        g2 = yt.^4 - (3*b^2)/((b-2)*(b-4));

        retp(g1~g2);
    endp;

::

    Generalized Method of Moments
    ====================================================================================
    Valid cases:                      500          Dependent variable:                 Y
    Number of moments:                  2          Degrees of freedom:               499
    J-stat                         0.0541          Probability of J:               0.816
    Number of vars:                     1
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     z-value        >|z|       Bound       Bound
    ------------------------------------------------------------------------------------
    X1                10.105      2.1803      4.6346  3.5757e-06      5.8316      14.378
    ====================================================================================

Remarks
-------

The user defined moment equation function should be set up to take at
least 2 inputs. The first input should always be the parameter vector
and the second input should always be the dependent data vector.
Additional optional arguments may be included. These arguments must
be passed into :func:`gmmFit` in the order they are passed to the moment
equation.

Including four inputs
+++++++++++++++++++++

::

    m = meqn(b, y, x, z);

    proc meqn(b, yt, xt, zt);

        local ut,dt;

        // OLS residuals
        ut = yt - b[1] - b[2]*xt[., 1] - b[3]*xt[., 2];

        // Moment conditions
        dt = ut.*zt;

        retp( dt );

    endp;

Including two inputs
++++++++++++++++++++

::

    m = meqn(b, y);

    proc meqn(b, yt);

        local g1, g2;

        g1= yt.^2 - b/(b-2);
        g2 = yt.^4 - (3*b^2)/((b-2)*(b-4));

        retp( g1~g2 );

    endp;

The :func:`gmmFit` function does not support dataset and formula string
syntax. Formula string syntax may be used for standard IV or ols
relationships in the :func:`gmmFitIV` procedure.

.. seealso:: Functions :func:`gmmFitControlCreate`, :func:`gmmFitIV`
