
gmmFitIV
==============================================

Purpose
----------------
Estimate instrumental variables model using the generalized method of moments.


Format
----------------
.. function:: gOut = gmmFitIV(y, x[, gCtl])
              gOut = gmmFitIV(y, x[, z[, gCtl]])
              gOut = gmmFitIV(dataset, formula[, gCtl])
              gOut = gmmFitIV(dataset, formula[, inst_list[, gCtl]])

    :param y: dependent data vector
    :type y: Nx1 matrix

    :param x: independent data matrix.
    :type x: NxK matrix

    :param z: Optional input, instrumental variables data matrix. If *z* is excluded, the linear model of *y* and *x* is estimated.
    :type z: NxK matrix

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: formula string of the model.

        e.g :code:`"y ~ X1 + X2"`, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;

        e.g. :code:`"y ~ ."`, ``.`` means including all variables except dependent variable ``y``.

    :type formula: string

    :param inst_list: Optional input. Formula string representing the instrumental variables to be included in the model.

        e.g. :code:`"pcturban + price + age + zip"` specifies that the variables *pcturban*, *price*, *age*, and *zip*
        should be used as instrumental variables.
    :type inst_list: string

    :param gCtl: Optional argument. An instance of an :class:`gmmControl` structure

        .. list-table::
            :widths: auto

            * - gCtl.method
              - string, GMM method to be used.

                  :"onestep": One-step GMM
                  :"twostep": Two-step GMM
                  :"iterative": Iterative GMM
                  :"CU": Continuous updating GMM.

                Default = :code:`"twostep"`
            * - gCtl.vceType
              - string, variance-covariance matrix type.

                  :"unadj": Unadjusted, non-robust SE.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.

                Default = :code:`"robust"`
            * - gCtl.wType
              - string, type of weight matrix used. Ignored for one-step case.

                  :"unadj": Unadjusted, non-robust SE.
                  :"robust": Heteroscedastic robust SE.
                  :"hac": Heteroscedastic-autocorrelation robust SE.

                Default = :code:`"robust"`
            * - gCtl.hacKernel
              - string, type of kernel used for estimation of HAC robust weight matrix and/or variance-covariance matrix. Ignored if not using :code:`"hac"` weight matrix and/or variance-covariance matrix.

                  .. NOTE:: Bandwidth is determined using the Newey-West optimal lag length selection method.

                  :"bartlett": Bartlett kernel.
                  :"parzen": Parzen kernel.
                  :"quad": Quadraticspectral kernel.

                Default = :code:`"bartlett"`
            * - gCtl.gmmlags
              - Scalar, Scalar, user specified lag truncation for HAC weight matrix and variance computations.
            * - gCtl.wInitMat
              - data matrix, initial weight matrix to be used. If specified the matrix is used as initial weighting matrix and overrides specification of gCtl.wInit*.
            * - gCtl.wInit
              - string, type of initial weight matrix used. If data matrix, the specified matrix is used as initial weighting matrix. Else:

                  :"identity": Identity matrix.
                  :"unadj": Weight matrix :math:`1/n*inv(Z'Z)`. Assumes moments are i.i.d. Default = :code:`"unadj"`
            * - gCtl.gIter
              - instance of :class:`gmmIterative` structure. This structure houses the tolerances for convergence for iterative GMM. Ignored if iterative GMM is not specified. The members include:

                  :gCtl.gIter.maxIter: scalar, maximum number of iterations. Default = 500.
                  :gCtl.gIter.paramTol: scalar, tolerance level for convergence based on parameter estimates. Default = 1e-6.
                  :gCtl.gIter.wTol: scalar, tolerance level for convergence based on weight matrix estimates. Default = 1e-6.
            * - gCtl.noconstant
              - scalar, specified to indicate if constant is included in model. Only valid if data vector input method is used. Set to 1 to exclude constant from model. Constant is always first parameter in parameter vector. Default = 0 [constant included].For dataset and string formula method to remove constant from model specify :code:`"-1"` as first dependent variable: e.g.: :code:`"y ~ -1 + X1 + X2"`
            * - gCtl.varNames
              - string array, dependent variable names. Only used for data vector input case. Default = ``X1, X2, ...``
            * - gCtl.instNames
              - string array, instrumental variable names. Only used for data vector input case. Default = ``Z1, Z2, ...``

    :type gCtl: struct

    :return gOut: instance of :class:`gmmOut` struct containing the following members:

        .. csv-table::
            :widths: auto

            "gOut.paramEst", "column vector of final estimates. Constant, if included in model, is the first element."
            "gOut.wFinal", "matrix, final weighting matrix."
            "gOut.covPar", "matrix, estimated variance-covariance matrix."
            "gOut.numParams", "scalar, number of parameters estimated in model."
            "gOut.numMoments", "scalar, number of moments."
            "gOut.numObs", "scalar, number of observations."
            "gOut.numInstruments", "scalar, number of instruments."
            "gOut.numMoments", "scalar, number of moments."
            "gOut.JStat", "scalar, Hansen statistic of overidentification."
            "gOut.df", "scalar, degrees of freedom."

    :rtype gOut: struct

Examples
----------------

Formula String
+++++++++++++++++++

::

    new;
    cls;

    /*
    ** Declare gmm_result to be a gmmOut struct
    ** to hold the results of the estimation
    */
    struct gmmOut gmm_result;

    // Create fully pathed dataset file name string
    auto_dset = getGAUSSHome("examples/auto");

    // Perform estimation, using a formula string specification
    gmm_result = gmmFitIV(auto_dset, "mpg ~ weight + length");

The above code will print out the following report:

::

    Generalized Method of Moments
    ====================================================================================
    Valid cases:                       74          Dependent variable:               mpg
    Number of moments:                  0          Degrees of freedom:                71
    Number of vars:                     3                                               
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------
    Constant          47.885       7.506       6.380       0.000      33.173      62.597 
    weight            -0.004       0.002      -1.978       0.052      -0.008      -0.000 
    length            -0.080       0.068      -1.175       0.244      -0.212       0.053 
    ====================================================================================
    Instruments: Constant, weight, length

Data Matrix
+++++++++++++++++++

::

    new;
    cls;

    data = loadd(getGAUSSHome("examples/hsng.dat"));

    y = data[., 12];
    x = data[., 11 7];
    z = data[., 7 8 14:16];

    /*
    ** Declare gctl to be a gmmControl struct
    ** and fill with default settings
    */
    struct gmmControl gctl;
    gctl = gmmControlCreate();

    // Set desired estimation options
    gctl.wInit = "unadj";

    // Set method
    gctl.method = "twostep";

    // Set variance type
    gctl.vceType = "robust";

    // Weight matrix type
    gctl.wType = "robust";

    struct gmmOut gOut;
    gOut = gmmFitIV(y, x, z, gctl);

The above code will print out the following report:

::

    Generalized Method of Moments
    ====================================================================================
    Valid cases:                       50          Dependent variable:              rent
    Number of moments:                  0          Degrees of freedom:                47
    J-stat                          6.975          Probability of J:               0.073
    Number of vars:                     3                                               
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------
    Constant         112.123      10.546      10.632       0.000      91.453     132.792 
    hsngval            0.001       0.000       3.627       0.001       0.001       0.002 
    pcturban           0.762       0.264       2.880       0.006       0.243       1.280 
    ====================================================================================
    Instruments: Constant, pcturban, faminc, reg2, reg3, reg4

Remarks
-------

The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

.. seealso:: Functions :func:`gmmControlCreate`, :func:`gmmFit`
