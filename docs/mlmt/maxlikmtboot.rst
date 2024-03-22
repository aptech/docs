maxlikmtBoot
==============================================

Purpose
-------
Computes bootstrapped constrained maximum likelihood estimates.

Format
------
.. function:: out = maxlikmtBoot(&modelProc, par, ..., c1)

    :param &modelProc: Pointer to a procedure that computes the function to be minimized.
    :type &modelProc: pointer

    :param par: An instance of a PV structure, constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional arguments that will be passed to the user-provided log-likelihood function. Can include any GAUSS data type or a DS structure for dataset handling.
    :type ...: Various

    :param c1: Optional input. Instance of a :class:`maxlikmtControl` structure containing the following members:

        .. include:: include/mlmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`maxlikmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures.

        .. include:: include/mlmtresultsstruct.rst

    :rtype out: struct

Example
-------
Maximum Likelihood with Bounded Parameters and User-defined Gradient
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  new;
  library maxlikmt;

  //Procedure to compute log-likelihood
  proc lpr(struct PV parms, x, y, ind);
      local s2, b0, b, yh, u, res, g1, g2;
      
      struct modelResults mm;

      b0 = pvUnpack(parms, "b0");
      b = pvUnpack(parms, "b");
      s2 = pvUnpack(parms, "s2");

      yh = b0 + x * b;
      res = y - yh;
      u = y[.,1] ./= 0;

      //If the first element of 'ind' is non-zero
      //compute the function value
      if ind[1];
          mm.function = u.*lnpdfmvn(res,s2) + (1-u).*(ln(cdfnc(yh/sqrt(s2))));
      endif;

      //If the second element of 'ind' is non-zero
      //compute the gradient value
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

  //Starting values for parameters
  struct PV par;
  par = pvPack(pvCreate(), 1, "b0");
  par = pvPack(par, 1|1|1, "b");
  par = pvPack(par, 1, "s2");

  //Load all variables from dataset  
  z = loadd(getGAUSSHome("pkgs/maxlikmt/examples/maxlikmttobit.dat"));
  y = z[., 1];
  x = z[., 2:4];

  //Declare control structure
  struct maxlikmtControl c0;
  c0 = maxlikmtcontrolcreate;

  //Place bounds on coefficients
  // -10 < b0 < 10
  //- 10 < b1, b2, b3 < 10
  // 0.1 < s2 < 10
  c0.Bounds = { -10 10,
                -10 10,
                -10 10,
                -10 10,
                .1 10 };

  //Set number of observations
  c0.numObs = rows(z);

  /********************************
  Bootstrap Estimation
  *********************************/
  //Declare 'out' to be a maxlikmtResults
  struct maxlikmtResults out;
  out = maxlikmtBoot(&lpr, par, x, y, c0);

  call maxlikmtPrt(out);
