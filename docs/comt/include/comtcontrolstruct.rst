.. list-table::
   :widths: auto


   * - c1.A
     - MxK matrix, linear equality constraint coefficients: c1.A * p = c1.B where p is a vector of the parameters.

   * - c1.B
     - Mx1 vector, linear equality constraint constants: c1.A * p = c1.B where p is a vector of the parameters.

   * - c1.C
     - MxK matrix, linear inequality constraint coefficients: c1.C * p >= c1.D where p is a vector of the parameters.

   * - c1.D
     - Mx1 vector, linear inequality constraint constants: c1.C * p >= c1.D where p is a vector of the parameters.

   * - c1.eqProc
     - Scalar, pointer to a procedure that computes the nonlinear equality constraints. It has two input arguments, an instance of a PV parameter structure, and an instance of a DS data structure, and one output argument, a vector of computed equality constraints. Default = {}, i.e., no equality procedure.

   * - c1.ineqProc
     - Scalar, pointer to a procedure that computes the nonlinear inequality constraints. It has two input arguments, an instance of a PV parameter structure, and an instance of a DS data structure, and one output argument, a vector of computed inequality constraints. Default = {}, i.e., no inequality procedure.

   * - c1.eqJacobian
     - Scalar, pointer to a procedure that computes the Jacobian of the equality constraints. It has two input arguments, an instance of a PV parameter structure, and an instance of a DS data structure, and one output argument, a matrix of derivatives of the equality constraints with respect to the parameters. Default = {}, i.e., no equality Jacobian procedure.

   * - c1.ineqJacobian
     - Scalar, pointer to a procedure that computes the Jacobian of the inequality constraints. It has two input arguments, an instance of a PV parameter structure, and an instance of a DS data structure, and one output argument, a matrix of derivatives of the inequality constraints with respect to the parameters. Default = {}, i.e., no inequality Jacobian procedure.

   * - c1.bounds
     - 1x2 or Kx2 matrix, bounds on parameters. If 1x2 all parameters have same bounds. Default = {-1e256, 1e256}.

   * - c1.algorithm
     - Scalar, descent algorithm, 0 - Modified BFGS (Default), 1 = BFGS, 2 = DFP, 3 = Newton.

   * - c1.useThreads
     - Scalar, if nonzero threading is turned on, else off. Default = off.

   * - c1.switch
     - 4x1 or 4x2 vector, controls algorithm switching. If 4x1, specifics include algorithm number to switch to, COMT switches if function changes less than a certain amount, COMT switches if a certain number of iterations is exceeded, COMT switches if line search step changes less than a certain amount. Default = {1 3, .0001 .0001, 10 10, .0001 .0001}.

   * - c1.lineSearch
     - Scalar, sets line search method, 0 augmented Lagrangian penalty method (requires constraints), 1 STEPBT (quadratic and cubic curve fit) (default), 2 Brent's method, 3 half, 4 Strong Wolfe's condition.

   * - c1.trustRadius
     - Scalar, radius of the trust region. If scalar missing, trust region not applied. Sets a maximum amount of the direction at each iteration. Default = 0.1.

   * - c1.penalty
     - Scalar, augmentation constant for augmented Lagrangian penalty line search method.

   * - c1.active
     - Kx1 vector, set K-th element to zero to fix it to start value. Use the GAUSS function pvGetIndex to determine where parameters in the PV structure are in the vector of parameters. Default = {}, all parameters are active.

   * - c1.maxIters
     - Scalar, maximum number of iterations. Default = 10000.

   * - c1.dirTol
     - Scalar, convergence tolerance. Iterations cease when all elements of the direction vector are less than this value. Default = 1e-5.

   * - c1.feasibleTest
     - Scalar, if nonzero, parameters are tested for feasibility before computing function in line search. If function is defined outside inequality boundaries, then this test can be turned off. Default = 1.

   * - c1.maxTries
     - Scalar, maximum number of attempts in random search. Default = 100.

   * - c1.randRadius
     - Scalar, if zero, no random search is attempted. If nonzero, it is the radius of the random search. Default = .001.

   * - c1.gradMethod
     - Scalar, method for computing numerical gradient. 0 = central difference, 1 = forward difference (default), 2 = backward difference.

   * - c1.hessMethod
     - Scalar, method for computing numerical Hessian. 0 = central difference, 1 = forward difference (default), 2 = backward difference.

   * - c1.gradStep
     - Scalar or Kx1, increment size for computing numerical derivatives (gradient and/or Hessian). If scalar, stepsize will be gradStep value times parameter estimates for the numerical derivative. If Kx1, the step size for the numerical derivatives will be the literal values of the elements of the gradStep vector.

   * - c1.gradCheck
     - Scalar, if nonzero and if analytical gradients and/or Hessian have been provided, numerical gradients and/or Hessian are computed and compared against the analytical versions.

   * - c1.state
     - Scalar, seed for random number generator.

   * - c1.title
     - String, title of run.

   * - c1.printIters
     - Scalar, if nonzero, prints iteration information. Default = 0.

   * - c1.disableKey
     - Scalar, if nonzero, keyboard input disabled.
