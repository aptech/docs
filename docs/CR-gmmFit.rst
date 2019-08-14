
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

    :param y: independent data vector.
    :type y: Nx1 matrix

    :param \.\.\.: Optional inputs. These arguments are passed untouched to the user-provided moment function by :func:`gmmFit`.
    :type \.\.\.: Any

    :param gCtl: Optional argument, an instance of an :class:`gmmControl` structure. The following members of *gCtl* are referenced within the :func:`gmmFit` routine:

        .. list-table::
            :widths: auto

            * - *gCtl.bStart*
              - column vector of parameter starting values. For all methods except continuous updating GMM default = 0.1. For continuous updating GMM default equals estimation from onestep GMM. Must be specified if data matrix syntax is used and *gctl.numParms* is not specified. For estimation stability it is highly recommended to speficy starting parameters.
            * - *gCtl.method*
              - string, GMM method to be used. Default = :code:`"twostep"`.

                  :"onestep": One-step GMM
                  :"twostep": Two-step GMM
                  :"iterative": Iterative GMM
                  :"CU": Continuous updating GMM
            * - *gCtl.vceType*
              - string, variance-covariance matrix type. Default = :code:`"robust"`.

                  :"unadj": Unadjusted, non-robust SE. This option is only available if the formula string syntax is used. It assumes a moment function of the form :math:`m = f(Z, u)` or :math:`m = f(X, u)`. The :code:`"unadj"` vce is given by :math:`\sigma_{u}^2 (x'(z(z'z)^{-1}z)x)^{-1}`.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.
            * - *gCtl.wType*
              - string, type of weight matrix used. Ignored for one-step case. Default = :code:`"robust"`.

                  :"unadj": Unadjusted, non-robust SE. This option is only available if the formula string syntax is used.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.
            * - *gCtl.hacKernel*
              - string, type of kernel used for estimation of HAC robust weight matrix and/or variance-covariance matrix. Ignored if not using :code:`"hac"` weight matrix and/or variance-covariance matrix. Bandwidth is determined using the Newey-West optimal lag length selection method. Default = :code:`"bartlett"`.

                  :"bartlett": Bartlett kernel.
                  :"parzen": Parzen kernel.
                  :"quad": Quadraticspectral kernel.
            * - *gCtl.wInitMat*
              - data matrix, initial weight matrix to be used. If specified the matrix is used as initial weighting matrix and overrides specification of *gCtl.wInit*.
            * - *gCtl.wInit*
              - string or data matrix, type of initial weight matrix used. If data matrix, the specified matrix is used as initial weighting matrix. Default = :code:`"identity"`.

                  :"identity": Identity matrix.
                  :"unadj": Weight matrix :math:`\frac{1}{n}*inv(Z'Z)`. Assumes moments are i.i.d. This option is only available if the formula string syntax is used.
            * - *gCtl.gIter*
              - instance of :class:`gmmIterative` structure. This structure houses the tolerances for convergence for iterative GMM. Ignored if iterative GMM is not specified. The members include:

                  :gCtl.gIter.maxIter: scalar, maximum number of iterations.
                  :gCtl.gIter.parmTol: scalar, tolerance level for convergence based on parameter estimates. Default = 1e-5.
                  :gCtl.gIter.wTol: scalar, tolerance level for convergence based on weight matrix estimates. Default = 1e-5.

            * - *gCtl.noconstant*
              - scalar, specified to indicate if constant is included in model. Only valid if data vector input method is used. Set to 1 to exclude constant from model. Constant is always first parameter in parameter vector. Default = 0 [constant included].For dataset and string formula method to remove constant from model specify :code:`"-1"` as first dependent variable: e.g. : :code:`"y ~ -1 + X1 + X2"`
            * - *gCtl.varNames*
              - string array, dependent variable names. Only used for data vector input case. Default = :code:`"X1", "X2", ...`
            * - *gCtl.instNames*
              - string array, instrumental variable names. Only used for data vector input case. Default = :code:`"Z1", "Z2", ...`
            * - *gCtl.numParms*
              - scalar, number of parameters estimated in model. Must be specified if data matrix syntax is used and *gCtl.bStart* is not specified.
            * - *gctl.A*
              - MxK matrix, linear equality constraint coefficients: :code:`gctl.A * p = gctl.B` where *p* is a vector of the parameters.
            * - *gctl.B*
              - Mx1 vector, linear equality constraint constants: :code:`gctl.A * p = gctl.B` where *p* is a vector of the parameters.
            * - *gctl.C*
              - MxK matrix, linear inequality constraint coefficients: :code:`gctl.C * p >= gctl.D` where *p* is a vector of the parameters.
            * - *gctl.D*
              - Mx1 vector, linear inequality constraint constants: :code:`gctl.C * p >= gctl.D` where *p* is a vector of the parameters.
            * - *gctl.bounds*
              - 1x2 or Kx2 matrix, bounds on parameters. If 1x2 all parameters have same bounds. Default = :code:`{ -1e256 1e256 }`.

    :type gCtl: struct

    :return gOut: instance of :class:`gmmOut` struct containing the following members:

        .. csv-table::
            :widths: auto

            "*gOut.parEst*", "column vector of final estimates. Constant, if included in model, is the first element."
            "*gOut.wFinal*", "matrix, final weighting matrix."
            "*gOut.covPar*", "matrix, estimated variance-covariance matrix."
            "*gOut.fct*", "vector, mean value of the moment equations."
            "*gOut.hessian*", "matrix, Hessian of mean of moment equation wrt parameters."
            "*gOut.gradient*", "matrix, Gradient of mean of moment equation wrt parameters."
            "*gOut.numParms*", "scalar, number of parameters estimated in model."
            "*gOut.numMoments*", "scalar, number of moments."
            "*gOut.numObs*", "scalar, number of observations."
            "*gOut.numInstruments*", "scalar, number of instruments."
            "*gOut.JStat*", "scalar, Hansen statistic of overidentification."
            "*gOut.df*", "scalar, degrees of freedom."

    :type gOut: struct

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

    // Number of observations>
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

.. seealso:: Functions :func:`gmmFitControlCreate`, :func:`gmmFitIV`
