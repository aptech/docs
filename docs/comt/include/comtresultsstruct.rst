.. list-table::
   :widths: auto

   * - out1.par
     - Instance of a PV structure containing the parameter estimates will be placed in the member matrix out1.par.

   * - out1.fct
     - Scalar, function evaluated at parameters in par.

   * - out1.returnDescription
     - String, description of return values.

   * - out1.hessian
     - KxK matrix, Hessian evaluated at parameters in par.

   * - out1.xproduct
     - KxK matrix, cross-product of NxK matrix of first derivatives evaluated at parameters in par. Not available if log-likelihood function returns a scalar.

   * - out1.gradient
     - Kx1 vector, gradient evaluated at the parameters in par.

   * - out1.numIterations
     - Scalar, number of iterations.

   * - out1.elapsedTime
     - Scalar, elapsed time of iterations.

   * - out1.title
     - String, title of run.

   * - out1.lagr
     - An instance of a comtLagrange structure containing the Lagrangeans for the constraints. For an instance named lagr, the members are:
       
       - out1.lagr.lineq
         - Mx1 vector, Lagrangeans of linear equality constraints.
       - out1.lagr.nlineq
         - Nx1 vector, Lagrangeans of nonlinear equality constraints.
       - out1.lagr.linIneq
         - Px1 vector, Lagrangeans of linear inequality constraints.
       - out1.lagr.nlinineq
         - Qx1 vector, Lagrangeans of nonlinear inequality constraints.
       - out1.lagr.bounds
         - Kx2 matrix, Lagrangeans of bounds.
       - out1.Lagr.EqCov
         - (M+N)x(M+N) matrix, covariance matrix of equality constraints.
       - out1.Lagr.IneqCov
         - (P+Q)x(P+Q) matrix, covariance matrix of inequality constraints.

       Whenever a constraint is active, its associated Lagrangean will be nonzero. For any constraint that is inactive throughout the iterations as well as at convergence, the corresponding Lagrangean matrix will be set to a scalar missing value.

   * - out1.retcode
     - Return code:
       
       - 0
         - Normal convergence.
       - 1
         - Forced exit.
       - 2
         - Maximum number of iterations exceeded.
       - 3
         - Function calculation failed.
       - 4
         - Gradient calculation failed.
       - 5
         - Hessian calculation failed.
       - 6
         - Line search failed.
       - 7
         - Functional evaluation failed.
       - 8
         - Error with initial gradient.
       - 9
         - Error with constraints.
       - 10
         - Second update failed.
       - 11
         - Maximum time exceeded.
       - 12
         - Error with weights.
       - 13
         - Quadratic program failed.
       - 14
         - Equality constraint Jacobian failed.
       - 15
         - Inequality constraint Jacobian failed.
       - 16
         - Function evaluated as complex.
       - 20
         - Hessian failed to invert.
