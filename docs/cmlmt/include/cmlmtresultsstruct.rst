.. list-table::
   :widths: auto

   * - out.par
     - Instance of a PV structure containing the parameter estimates will be placed in the member matrix out.par.

   * - out.fct
     - Scalar, function evaluated at parameters in *par*.

   * - out.returnDescription
     - String, description of return values.

   * - out.covPar
     - KxK matrix, covariance matrix of parameters.

   * - out.covParDescription
     - String, description of covPar.

   * - out.numObs
     - Scalar, number of observations.

   * - out.hessian
     - KxK matrix, Hessian evaluated at parameters in *par*.

   * - out.xproduct
     - KxK matrix, cross-product of NxK matrix of first derivatives evaluated at parameters in *par*. Not available if log-likelihood function returns a scalar.
   
   * - out.waldLimits
     - Kx2 matrix, Wald confidence limits.
   
   * - out.inverseWaldLimits
     - Kx2 matrix, confidence limits by inversion of Wald statistics. Available only if :func:`cmlmtInverseWaldLimits` has been called.
   
   * - out.profileLimits
     - Kx2 matrix, profile likelihood confidence limits, i.e., by inversion of likelihood ratio statistics. Only available if :func:`cmlmtProfileLimits` has been called.
   
   * - out.bayesLimits
     - Kx2 matrix, weighted likelihood Bayesian confidence limits. Only available if :func:`cmlmtBayes` has been called.
   
   * - out.bootLimits
     - Kx2 Matrix, bootstrap confidence limits. Available only if :func:`cmlmtBoot` has been called.
   
   * - out.gradient
     - Kx1 vector, gradient evaluated at the parameters in *par*.
   
   * - out.numIterations
     - Scalar, number of iterations.
   
   * - out.elapsedTime
     - Scalar, elapsed time of iterations.
   
   * - out.alpha
     - Scalar, probability level of confidence limits. Default = .05.
   
   * - out.title
     - String, title of run.
   
   * - out.lagr
     - An instance of a :class:`cmlmtLagrange` structure containing the Lagrangeans for the constraints. For an instance named *lagr*, the members are:
       
       - out.lagr.lineq
         - Mx1 vector, Lagrangeans of linear equality constraints,
       - out.lagr.nlineq
         - Nx1 vector, Lagrangeans of nonlinear equality constraints
       - out.lagr.linineq
         - Px1 vector, Lagrangeans of linear inequality constraints
       - out.lagr.nlinineq
         - Qx1 vector, Lagrangeans of nonlinear inequality constraints
       - out.lagr.bounds
         - Kx2 matrix, Lagrangeans of bounds
       - out.Lagr.EqCov
         - (M+N)x(M+N) matrix, covariance matrix of equality constraints
       - out.Lagr.IneqCov
         - (P+Q)x(P+Q) matrix, covariance matrix of inequality constraints

       Whenever a constraint is active, its associated Lagrangean will be nonzero. For any constraint that is inactive throughout the iterations as well as at convergence, the corresponding Lagrangean matrix will be set to a scalar missing value.

   * - out.retcode
     - Return code:
       
       - 0
         - Normal convergence
       - 1
         - Forced exit
       - 2
         - Maximum number of iterations exceeded
       - 3
         - Function calculation failed
       - 4
         - Gradient calculation failed
       - 5
         - Hessian calculation failed
       - 6
         - Line search failed
       - 7
         - Functional evaluation failed
       - 8
         - Error with initial gradient
       - 9
         - Error with constraints
       - 10
         - Second update failed
       - 11
         - Maximum time exceeded
       - 12
         - Error with weights
       - 13
         - Quadratic program failed
       - 14
         - Equality constraint Jacobian failed
       - 15
         - Inequality constraint Jacobian failed
       - 16
         - Function evaluated as complex
       - 20
         - Hessian failed to invert
       - 34
         - Data set could not be opened
