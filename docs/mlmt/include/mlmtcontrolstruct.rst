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

