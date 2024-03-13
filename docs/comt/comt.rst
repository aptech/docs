comt
==============================================

Purpose
----------------

Solve the nonlinear programming problem.

Format
----------------
.. function:: out = Comt(&logl, par)
                  out = Comt(&logl, par, ...)
                  out = Comt(&logl, par, ..., c1)
                  out = Comt(&logl, par, c1)
                  out = Comt(&logl, par, data)
                  out = Comt(&logl, par, data, c1)

    :param &logl: Pointer to a procedure that computes the function to be minimized.
    :type &logl: pointer

    :param par: An instance of a PV structure. The par instance is passed to the user-provided procedure pointed to by &fct. par is constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional input arguments. They can be any set of structures, matrices, arrays, strings, required to compute the objective function. It can also include a comtControl structure.
    :type ...: Various

    :param c1: Optional input. Instance of a :class:`comtControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - c1.A
              - MxK matrix, linear equality constraint coefficients. ``c1.A * p = c1.B`` where ``p`` is a vector of the parameters.

            * - c1.B
              - Mx1 vector, linear equality constraint constants. ``c1.A * p = c1.B``.

            * - c1.C
              - MxK matrix, linear inequality constraint coefficients. ``c1.C * p >= c1.D`` where ``p`` is a vector of the parameters.

            * - c1.D
              - Mx1 vector, linear inequality constraint constants. ``c1.C * p >= c1.D``.

            * - c1.eqProc
              - Scalar, pointer to a procedure that computes the nonlinear equality constraints. Default = {.}, i.e., no equality procedure.

            * - c1.ineqProc
              - Scalar, pointer to a procedure that computes the nonlinear inequality constraints. Default = {.}, i.e., no inequality procedure.

            * - c1.eqJacobian
              - Scalar, pointer to a procedure that computes the Jacobian of the equality constraints. Default = {.}, i.e., no equality Jacobian procedure.

            * - c1.ineqJacobian
              - Scalar, pointer to a procedure that computes the Jacobian of the inequality constraints. Default = {.}, i.e., no inequality Jacobian procedure.

            * - c1.bounds
              - 1x2 or Kx2 matrix, bounds on parameters. Default = {-1e256, 1e256}.

            * - c1.algorithm
              - Scalar, descent algorithm. Default = 0 (Modified BFGS).

            * - c1.useThreads
              - Scalar, if nonzero threading is turned on, else off. Default = off.

            * - c1.switch
              - 4x1 or 4x2 vector, controls algorithm switching. Default = {1 3, .0001 .0001, 10 10, .0001 .0001}.

            * - c1.lineSearch
              - Scalar, sets line search method. Default = 1 (STEPBT).

            * - c1.trustRadius
              - Scalar, radius of the trust region. Default = 0.1.

            Additional control parameters as described in the original text.

    :type c1: struct

    :return out1: An instance of a :class:`comtResults` structure. Contains the results of the nonlinear programming problem solution, including parameter estimates, function evaluations, and detailed information about constraints handling and optimization process. The :class:`comtResults` structure includes:

        .. list-table::
            :widths: auto

            * - out1.par
              - Instance of a PV structure containing the parameter estimates.

            * - out1.fct
              - Scalar, function evaluated at parameters in par.

            * - out1.returnDescription
              - String, description of return values.

            * - out1.hessian
              - KxK matrix, Hessian evaluated at parameters in par.

            * - out1.xproduct
              - KxK matrix, cross-product of NxK matrix of first derivatives evaluated at parameters in par.

            * - out1.gradient
              - Kx1 vector, gradient evaluated at the parameters in par.

            * - out1.numIterations
              - Scalar, number of iterations.

            * - out1.elapsedTime
              - Scalar, elapsed time of iterations.

            * - out1.title
              - String, title of run.

            * - out1.lagr
              - Instance of a comtLagrange structure containing the Lagrangeans for the constraints.

            * - out1.retcode
              - Return code indicating the outcome of the computation.

    :rtype out1: comtResults structure instance


Remarks
-------

- There is one required user-provided procedure, the one computing the objective function and optionally the first and/or second derivatives, and four other optional procedures, one each for computing the equality constraints, the inequality constraints, the Jacobian of the equality constraints, and the Jacobian of the inequality constraints.

- The main procedure, computing the objective function and optionally the first and/or second derivatives, has three arguments: an instance of type struct PV containing the parameters, a second argument that is an instance of type struct DS containing the data, and a third argument that is a vector of zeros and ones indicating which of the results, the function, first derivatives, or second derivatives, are to be computed.

- The remaining optional procedures take just two arguments: the instance of the PV structure containing the parameters and any optional arguments that were passed to COMT.

- The instance of the PV structure is set up using the PV pack procedures, pvPack, pvPackm, pvPacks, and pvPacksm. These procedures allow for setting up a parameter vector in a variety of ways.

- The optional arguments passed to the user-provided objective function procedure are untouched. This allows you to pass into your function any information it needs.

- The procedures for nonlinear equality and inequality constraints take two input arguments, an instance of a PV parameters structure. For example, to constrain the sum of squares of the regression coefficients to be greater than one, provide the following procedure:

  ::
  
      proc ineqConst(struct PV par1);
           local b;
           b = pvUnpack(p,"b");
           retp( sumc(b^2) - 1 );
      endp;

- If COMT has been called with optional arguments, then they must be included in the call to ineqConst() as well.
