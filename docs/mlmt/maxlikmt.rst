maxlikmt
==============================================

Purpose
----------------

Solves the optimization problem with or without simple bounds.

Format
----------------
.. function:: out = maxlikmt(&logl, par)
                  out = maxlikmt(&logl, par, ...)
                  out = maxlikmt(&logl, par, ..., c1)
                  out = maxlikmt(&logl, par, c1)
                  out = maxlikmt(&logl, par, data)
                  out = maxlikmt(&logl, par, data, c1)

    :param &logl: A pointer to a procedure that returns either the log-likelihood for one observation or a vector of log-likelihoods for a matrix of observations.
    :type &logl: pointer

    :param par: An instance of a PV structure. Constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional arguments that will be passed to the user provided log-likelihood function. They can be any GAUSS data type.
    :type ...: Various

    :param data: Optional DS structure. This parameter allows the function to interact with GAUSS datasets directly.
    :type data: structure

    :param c1: Optional input. Instance of a :class:`maxlikmtControl` structure containing the following members:

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

    :type c1: struct

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
              - Kx2 matrix, confidence limits by inversion of Wald statistics. Available only if :func:`maxlikmtInverseWaldLimits`` has been called.

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
              - Return code indicating the outcome of the computation:

                - 0: Normal convergence
                - 1: Forced exit
                - 2: Maximum number of iterations exceeded
                - 3: Function calculation failed
                - 4: Gradient calculation failed
                - 5: Hessian calculation failed
                - 6: Line search failed
                - 7: Functional evaluation failed
                - 8: Error with initial gradient
                - 9: Error with constraints
                - 10: Second update failed
                - 11: Maximum time exceeded
                - 12: Error with weights
                - 13: Quadratic program failed
                - 14: Equality constraint Jacobian failed
                - 15: Inequality constraint Jacobian failed
                - 20: Hessian failed to invert
                - 34: Data set could not be opened

    :rtype: struct
Example
-------
Maximum Likelihood with Bounded Parameters and User-defined Gradient
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  new;
  cls;
  library maxlikmt;

  //Log-likelihood procedure
  proc lpr(parms, x, y, ind);
      local s2, b0, b, yh, u, res, g1, g2;
      
      struct modelResults mm;

      b0 = parms[1];
      b = parms[2:4];
      s2 = parms[5];

      yh = b0 + x * b;
      res = y - yh;
      u = y[.,1] ./= 0;
      
      // If the first element of 'ind' is non-zero
      // compute the function value
      if ind[1];
          mm.function = u.*lnpdfmvn(res,s2) + (1-u).*(ln(cdfnc(yh/sqrt(s2))));
      endif;

      // If the second element of 'ind' is non-zero
      // compute the gradient value
      if ind[2];
          yh = yh/sqrt(s2);
          g1 = ((res~x.*res)/s2)~((res.*res/s2)-1)/(2*s2);
          g2 = ( -( ones(rows(x),1)~x )/sqrt(s2) )~(yh/(2*s2));
          g2 = (pdfn(yh)./cdfnc(yh)).*g2;
          //Note the computation of 'm' is computed
          //only once and the results shared with
          //function and gradient computations
          mm.gradient = u.*g1 + (1-u).*g2;
      endif;

      retp(mm);

  endp;

  // Starting values for parameters
  // b_start = b0|b1|b2|b3|s2
  b_start = ones(5,1);

  // Declare control structure
  struct maxlikmtControl c0;
  c0 = maxlikmtcontrolcreate;

  // Print Iterations to screen
  c0.printiters = 1;

  // Change descent algorithm to use BHHH
  c0.algorithm = 4;

  // Set tolerance level
  c0.tol = 1e-6;

  // Place bounds on coefficients
  // -10 < b0 < 10
  //- 10 < b1, b2, b3 < 10
  // 0.1 < s2 < 10
  c0.Bounds = { -10 10,
                -10 10,
                -10 10,
                -10 10,
                .1 10 };
                
  // Load all variables from dataset           
  z = loadd(__FILE_DIR $+ "maxlikmttobit.dat");
  y = z[.,1];
  x = z[.,2:4];

  // Declare 'out1' to be a maxlikmtResults
  // structure to hold the estimation results
  struct maxlikmtResults out1;

  // Perform estimation and print report
  out1 = maxlikmtprt(maxlikmt(&lpr, b_start, x, y, c0));

  // Print langrangeans 
  print;
  print out1.lagrangeans;

Remarks
-------

- :func:`maxlikmt` requires a user-provided procedure for computing the log-likelihood function and optionally the first and/or second derivatives. Additionally, there are options for computing equality/inequality constraints and their Jacobians.

- The main procedure for computing the log-likelihood, and optionally the first and/or second derivatives, involves:

  - An instance of a PV structure containing the parameters.
  - A set of optional arguments determined by the user for the calculation of the log-likelihood.
  - A vector of zeros and ones indicating which of the results (the function, first derivatives, or second derivatives) are to be computed.

- The remaining optional procedures take just two arguments: the instance of the PV structure containing the parameters and a set of optional arguments determined by the user for the calculation of the log-likelihood.

- The PV structure instance is configured using the PV pack procedures (:func:`pvPack`, :func:`pvPackm`, :func:`pvPacks`, and :func:`pvPacksm`), enabling a flexible setup of the parameter vector.

- For instance, the following procedure demonstrates how to compute the log-likelihood and first derivatives for a tobit model:

  ::

      proc lpr(struct PV p, y, x, ind);
         local s2, b0, b, yh, u, res, g1, g2;
    
         struct modelResults mm;
    
         b0 = pvUnpack(p, "b0");
         b = pvUnpack(p, "b");
         s2 = pvUnpack(p, "variance");
    
         yh = b0 + x * b;
         res = y - yh;
         u = y[.,1] ./= 0;
    
         if ind[1];
             mm.function = u.*lnpdfmvn(res, s2) + (1-u).*(ln(cdfnc(yh/sqrt(s2))));
         endif;
    
         if ind[2];
             yh = yh/sqrt(s2);
             g1 = ((res~x.*res)/s2)~((res.*res/s2)-1)/(2*s2);
             g2 = (-(ones(rows(x), 1)~x)/sqrt(s2))~(yh/(2*s2));
             g2 = (pdfn(yh)./cdfnc(yh)).*g2;
             mm.gradient = u.*g1 + (1-u).*g2;
         endif;
         retp(mm);
    
      endp;

- :func:`maxlikmt` can efficiently handle large datasets by reading the data in chunks. This functionality is facilitated by specifying a DS structure with the dataset name and selected variables as one of the optional arguments. For example, to read from a GAUSS dataset named "maxlikmttobit" and select specific variables:

  ::

      struct DS d0;
      d0 = dscreate;
      d0.dname = "maxlikmttobit";
      d0.vnames = "Y" $| "X1" $| "X2" $| "X3";

