Maximum Likelihood Estimation with Nonlinear Equality Constraints
==================================================================

This **GAUSS** maximum likelihood example demonstrates the use of **CMLMT** to estimate parameters of a tobit model with nonlinear equality constraints. 

Key example features
++++++++++++++++++++++

- Usages of data from the file *cmlmttobit.dat* (included with **cmlmt**).
- User defined likelihood function, :class:`lpr` with four inputs:
  - A PV structure storing parameters. 
  - Additional *X* and *y* data matrices, which are passed to :func:`cmlmt`` as optional arguments. 
  - The required *ind* input. 
- The inclusion of analytic gradient computations, as specified in the :class:`lpr` function.
- The second case uses a user-defined function :class:`eqp` in combination with the *c0.eqProc* member of the :class:`cmlmtControl` structure to specify the equality constraints. 

There are two equality constraints that are implemented in this example, one linear and one nonlinear:

.. math:: `p[1] - p[2] = 0`
.. math:: `p[2] * p[3] - 1 = 0`


where  :math:`p[1], p[2], \ldots, p[5]` are the parameters to be estimated. 


Code for estimation
----------------------

:: 

    /*
    **   Maximum likelihood tobit model 
    */
    new;
    library cmlmt;

    // Tobit likelihood function with 4 inputs
    //    i.      p      - The PV parameter structur
    //    ii-iii. x and y - Extra data needed by the objective procedure
    //    ii.     ind     - The indicator vector 
    proc lpr(struct PV p, x, y, ind);
        local s2, b0, b, yh, u, res, g1, g2;

        // Declare 'mm' to be a modelResults
        // struct local to this procedure
        struct modelResults mm;

        // Unpack parameters from PV structure
        b0 = pvUnpack(p, "b0");
        b = pvUnpack(p, "b");
        s2 = pvUnpack(p, "variance");

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
    struct PV p0;
    p0 = pvPack(pvCreate, 1, "b0");
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

    // Procedure to compute equality constraints
    // this must specify the constraint such that
    // eqp(x) = 0
    proc eqp(p, x, y);
       local c, b0, b;

       // Extract parameters
       b0 = pvUnpack(p, "b0");
       b = pvUnpack(p, "b");

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

  Log-likelihood        -129.935
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
    Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
  ---------------------------------------------------------------------
  b0[1,1]          0.7560        0.0862       8.775   0.0000     27.6776
  b[1,1]           0.7560        0.0862       8.775   0.0000    -27.6779
  b[2,1]           1.1077        0.1279       8.658   0.0000    -34.1711
  b[3,1]           0.9028        0.1043       8.658   0.0000    -41.9260
  variance[1,1]    1.2446        0.1883       6.610   0.0000      0.0085

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`cmlmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 
- The results are consistent with our constraints:
  - b0 and b[1, 1] are equal (:math:`b0 - b[1, 1] = 0`).
  - b[2, 1]*b[3, 1] - 1 = :math:`1.1077 * 0.9028 - 1 = 3.15e-05`.
- The gradients are not equal to zero, which is indicative that the contraints are binding. 


Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1                1      -0.27931016       0.27931016    -0.0049885835 
               1                1      -0.27931016       0.27931016    -0.0049885835 
     -0.27931016      -0.27931016                1               -1       0.01958035 
      0.27931016       0.27931016               -1                1      -0.01958035 
   -0.0049885909    -0.0049885909      0.019580346     -0.019580346                1

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit    Gradient
    ----------------------------------------------------------------------
    b0[1,1]          0.7560        0.5849        0.9270       27.6776
    b[1,1]           0.7560        0.5849        0.9270      -27.6779
    b[2,1]           1.1077        0.8537        1.3617      -34.1711
    b[3,1]           0.9028        0.6958        1.1098      -41.9260
    variance[1,1]    1.2446        0.8708        1.6184        0.0085

Number of iterations    10
Minutes to convergence     0.00012

