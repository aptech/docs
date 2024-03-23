.. list-table::
   :widths: auto

   * - out1.par
     - Instance of a PV structure containing the parameter estimates will be placed in the member matrix out1.par.

   * - out1.fct
     - Scalar, function evaluated at parameters in par.

   * - out1.gradient
     - Kx1 vector, gradient evaluated at the parameters in par.

   * - out1.numIterations
     - Scalar, number of iterations.

   * - out1.elapsedTime
     - Scalar, elapsed time of iterations.

   * - out1.title
     - String, title of run.

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
       - 10
         - Second update failed.
       - 11
         - Maximum time exceeded.
       - 16
         - Function evaluated as complex.
       - 17
         - Nnull activeset.
       - 20
         - Hessian failed to invert.
       - 20
         - Data set could not open.
