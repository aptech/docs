maxlikmtBoot
==============================================

Purpose
-------
Computes bootstrapped constrained maximum likelihood estimates.

Format
------
.. function:: out1 = maxlikmtBoot(&modelProc, par, ...)

    :param &modelProc: Pointer to a procedure that computes the function to be minimized.
    :type &modelProc: pointer

    :param par: An instance of a PV structure, constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional arguments that will be passed to the user-provided log-likelihood function. Can include any GAUSS data type or a DS structure for dataset handling.
    :type ...: Various

    :param c1: Optional input. Instance of an :class:`maxlikmtControl` structure containing the following members:
    :type c1: struct

        .. list-table::
            :widths: auto

            * - c1.bayesAlpha
              - Exponent of the Dirichlet random variates used in the weighted bootstrap. Default = 1.4.

            * - c1.priorProc
              - Pointer to a procedure for computing the prior. Assumes a uniform prior if not provided.

            * - c1.numSamples
              - Number of re-samples in the weighted likelihood bootstrap.

            * - c1.BayesFname
              - Filename for the simulated posterior parameters dataset. Defaults to a unique "BAYESxxxx" pattern.

            * - c1.maxBootTime
              - Maximum time allowed for resampling.

            * - c1.Bounds
              - Bounds on parameters, either 1x2 for all parameters or Kx2 for individual parameter bounds. Default = {-1e256, 1e256}.

            * - c1.algorithm
              - Descent algorithm for optimization, includes BFGS, DFP, Newton, and BHHH.

            * - c1.switch
              - Controls algorithm switching based on various performance metrics.

            * - c1.lineSearch
              - Method for line search in optimization, includes augmented trust region method and others. Default varies based on constraints.

            * - c1.active
              - Kx1 vector to control which parameters are active or fixed at start value.

            * - c1.numObs
              - Number of observations, required if the log-likelihood function returns a scalar.

            * - c1.maxIters
              - Maximum number of iterations for the optimization process. Default = 10000.

            * - c1.tol
              - Convergence tolerance, optimization stops when all elements of the direction vector are below this value. Default = 1e-5.

            * - c1.weights
              - Vector of weights for the objective function returning a vector. Default = 1.

            * - c1.covParType
              - Determines the type of covariance matrix computed, QML or ML. Default = 1.

            * - c1.alpha
              - Probability level for statistical tests. Default = .05.

            * - c1.feasibleTest
              - If nonzero, parameters are tested for feasibility before computing the function in line search. Default = 1.

            * - c1.maxTries
              - Maximum number of attempts in random search. Default = 100.

            * - c1.randRadius
              - Radius of the random search, if attempted. Default = .001.

            * - c1.gradMethod
              - Method for computing numerical gradient, includes central, forward, and backward difference.

            * - c1.hessMethod
              - Method for computing numerical Hessian, similar options as gradient computation.

            * - c1.gradStep
              - Increment size for computing numerical gradient, can be scalar or Kx1 vector.

            * - c1.hessStep
              - Increment size for computing numerical Hessian, options similar to gradStep.

            * - c1.gradCheck
              - If nonzero and analytical gradients/Hessian provided, numerical versions are computed for comparison.

            * - c1.state
              - Seed for random number generator, ensuring reproducibility.

            * - c1.title
              - Title of the run, for identification in output.

            * - c1.printIters
              - If nonzero, iteration information is printed. Default = 0.

            * - c1.disableKey
              - If nonzero, keyboard input is disabled during execution.

    :return: An instance of a :class:`maxlikmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures.

        .. list-table::
            :widths: auto

            * - out1.bayesLimits
              - Weighted likelihood Bayesian confidence limits, Kx2 matrix.

            * - out1.par
              - Instance of a PV structure containing the parameter estimates, placed in the member matrix *out1.par*.

            * - out1.fct
              - Scalar, function evaluated at parameters in *par*.

            * - out1.returnDescription
              - String, description of return values.

            * - out1.covPar
              - KxK matrix, covariance matrix of parameters.

            * - out1.covParDescription
              - String, description of *covPar*.

            * - out1.numObs
              - Scalar, number of observations.

            * - out1.hessian
              - KxK matrix, Hessian evaluated at parameters in *par*.

            * - out1.xproduct
              - KxK matrix, cross-product of NxK matrix of first derivatives evaluated at parameters in *par*. Not available if log-likelihood function returns a scalar.

            * - out1.waldLimits
              - Kx2 matrix, Wald confidence limits.

            * - out1.inverseWaldLimits
              - Kx2 matrix, confidence limits by inversion of Wald statistics. Available only if :func:`maxlikmtInverseWaldLimits` has been called.

            * - out1.profileLimits
              - Kx2 matrix, profile likelihood confidence limits, by inversion of likelihood ratio statistics. Only available if :func:`maxlikmtProfileLimits` has been called.

            * - out1.bootLimits
              - Kx2 Matrix, bootstrap confidence limits. Available only if :func:`maxlikmtBoot` has been called.

            * - out1.gradient
              - Kx1 vector, gradient evaluated at the parameters in *par*.

            * - out1.numIterations
              - Scalar, number of iterations.

            * - out1.elapsedTime
              - Scalar, elapsed time of iterations.

            * - out1.alpha
              - Scalar, probability level of confidence limits. Default = .05.

            * - out1.title
              - String, title of run.

            * - out1.Lagrangeans
              - Kx2 matrix, Lagrangean coefficients of bounds constraints if any.

            * - out1.retcode
              - Return code indicating the outcome of the computation.

    :rtype: struct
