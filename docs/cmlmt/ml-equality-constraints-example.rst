Maximum Likelihood Estimation with Analytic Gradient Computations
==================================================================

This **GAUSS** maximum likelihood example demonstrates the use of **CMLMT** to estimate parameters of a tobit model with equality constraints. 

Key example features
++++++++++++++++++++++

- Usages of data from the file *cmlmttobit.dat* (included with **cmlmt**).
- User defined likelihood function, :class:`lpr` with four inputs:
  - A parameter vector. 
  - Additional *X* and *y* data matrices, which are passed to :func:`cmlmt`` as optional arguments. 
  - The required *ind* input. 
- The inclusion of analytic gradient computations, as specified in the :class:`lpr` function.
- The second case uses a user-defined function :class:`eqp` in combination with the *c0.eqProc* member of the :class:`cmlmtControl` structure to specify the equality constraints. 

There are two equality constraints that are implemented in this example, one linear and one nonlinear:

.. math:: `p[1] - p[2] = 0`
.. math:: `p[2] * p[3] - 1 = 0`


where  :math:`p[1],p[2], \ldots, p[5]` are the parameters to be estimated. 


Code for estimation
----------------------

:: 

    /*
    **   Maximum likelihood tobit model 
    */
    new;
    library cmlmt;

    // Tobit likelihood function with 4 inputs
    //    i.      p      - The parameter vector
    //    ii-iii. x and y - Extra data needed by the objective procedure
    //    ii.     ind     - The indicator vector 
    proc lpr(p, x, y, ind);
        local s2, b0, b, yh, u, res, g1, g2;

        // Declare 'mm' to be a modelResults
        // struct local to this procedure
        struct modelResults mm;

        // Unpack parameters from PV structure
        b0 = pvUnpack(p,"b0");
        b = pvUnpack(p,"b");
        s2 = pvUnpack(p,"variance");

        yh = b0 + x * b;
        res = y - yh;
        u = y[., 1] ./= 0;

        // If first element of 'ind' is non-zero,
        // compute function evaluation
        if ind[1];
            mm.function = u.*lnpdfmvn(res, s2) + (1 - u).*(ln(cdfnc(yh/sqrt(s2))));
        endif;

        // If second element of 'ind' is non-zero,
        // compute function evaluation
        if ind[2];
          yh = yh/sqrt(s2);
          g1 = ((res~x.*res)/s2) ~ ((res.*res/s2) - 1)/(2*s2);
          g2 = ( -( ones(rows(x), 1) ~ x )/sqrt(s2) ) ~ (yh/(2*s2));
          g2 = (pdfn(yh)./cdfnc(yh)).*g2;
          mm.gradient = u.*g1 + (1 - u).*g2;
        endif;

        // Return modelResults struct
        retp(mm);

    endp;

    // Pack parameters into PV structure
    // note that first call to pvPack 
    p0 = pvPack(p0, 1, "b0");
    p0 = pvPack(p0, 1|1|1, "b");
    p0 = pvPack(p0, 1, "variance");
   
    // Load data
    z = loadd(getGAUSSHome("pkgs/cmlmt/examples/cmlmttobit.dat"));
   
    // Separate X and y
    y = z[., 1];
    x = z[., 2:4];

    // Declare 'c0' to be a cmlmtControl struct
    // and fill with default settings
    struct cmlmtControl c0;
    c0 = cmlmtControlCreate();

    c0.
    // Procedure to compute equality constraints
    // this must specify the constraint such that
    // eqp(x) = 0
    proc eqp(p, x, y);
       local c, b0, b;

       // Extract parameters
       b0 = p[1];
       b = p[2:4];

       // This will be returned and
       // it should be a vector of zeros
       // with the same number of rows as constraints
       c = zeros(2, 1);
       
       // First constraint
       c[1] = b0 - b[1];

       // Second constraint
       c[2] = b[2] * b[3] - 1;

       retp(c);
    endp;

    // Assign pointer for equality procedure
    c0.eqProc = &eqp;

    // Declare 'out' to be a cmlmtResults
    // struct to hold optimization results 
    struct cmlmtResults out;
    out = cmlmtprt(cmlmt(&lpr, p0, x, y, c0));

Results
-----------
The :func:`cmlmtprt` procedure prints three output tables:

- Estimation results. 
- Correlation matrix of parameters. 
- Wald confidence limits. 

Estimation results 
++++++++++++++++++++

::

  ===============================================================================
   CMLMT Version 3.0.0                                       
  ===============================================================================

  return code =    0
  normal convergence

  Log-likelihood        -43.9860
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
  Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
  ---------------------------------------------------------------------
  x[1,1]        1.4253        0.0376      37.925   0.0000      0.0000
  x[2,1]        0.4976        0.0394      12.642   0.0000      0.0000
  x[3,1]        0.4992        0.0458      10.889   0.0000      0.0000
  x[4,1]        0.4141        0.0394      10.506   0.0000      0.0000
  x[5,1]        0.1231        0.0196       6.284   0.0000      0.0000

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`cmlmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 

Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1      0.067006788      -0.24418626       0.05530654      -0.10868104 
     0.067006788                1      -0.30495236     -0.061965451       0.05808199 
     -0.24418626      -0.30495236                1       -0.3165649      0.067030893 
      0.05530654     -0.061965451       -0.3165649                1       0.04466025 
     -0.10868104       0.05808199      0.067030893       0.04466025                1 

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit   Gradient
    ----------------------------------------------------------------------
    x[1,1]        1.4253        1.3507        1.4999        0.0000
    x[2,1]        0.4976        0.4195        0.5757        0.0000
    x[3,1]        0.4992        0.4082        0.5903        0.0000
    x[4,1]        0.4141        0.3358        0.4923        0.0000
    x[5,1]        0.1231        0.0842        0.1620        0.0000

