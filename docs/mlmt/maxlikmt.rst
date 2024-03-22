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

        .. include:: include/mlmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`maxlikmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures. Contains the following members:

        .. include:: include/mlmtresultsstruct.rst

    :rtype out: struct

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
  z = loadd(getGAUSSHome("pkgs/maxlikmt/examples/maxlikmttobit.dat"));
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

