Maximum Likelihood Estimation with Nonlinear Inequality Constraints
====================================================================

This **GAUSS** maximum likelihood example demonstrates the use of **CMLMT** to estimate parameters of a tobit model with nonlinear inequality constraints. 

Key example features
++++++++++++++++++++++

- Usages of data from the file *cmlmttobit.dat* (included with **cmlmt**).
- User-defined likelihood function, :class:`lpr` with four inputs:  
    - A PV structure storing parameters.   
    - Additional *X* and *y* data matrices, which are passed to :func:`cmlmt`` as optional arguments.   
    - The required *ind* input.   
- The inclusion of analytic gradient computations, as specified in the :class:`lpr` function.
- A user-defined function :class:`ineqp` in combination with the *c0.ineqProc* member of the :class:`cmlmtControl` structure to specify the equality constraints. 

There are two equality constraints that are implemented in this example, one linear and one nonlinear:

.. math:: p[2] - p[1] \geq 0
.. math:: 1 - p[2] * p[3] \geq 0


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
    //    i.      p      - The PV parameter structure
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

        // Function computations
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

    // Bounds for estimation
    c0.bounds = { -10 10,
              -10 10,
              -10 10,
              -10 10,
              .1 10 };
    
    // Procedure to compute equality constraints
    // this must specify the constraint such that
    // ineqp(x) >= 0
    proc ineqp(p, x, y);
       local c, b0, b;

       // Extract parameters
       b0 = pvUnpack(p, "b0");
       b = pvUnpack(p, "b");

       // This will be returned and
       // it should be a vector of zeros
       // with the same number of rows as constraints
       c = zeros(2, 1);
       
       // First constraint
       c[1] = b[1] - b0;

       // Second constraint
       c[2] = 1 - b[2] * b[3];

       retp(c);
    endp;

    // Assign pointer for equality procedure
    c0.ineqProc = &ineqp;

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

  Log-likelihood        -99.8205
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
    Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
  ---------------------------------------------------------------------
  b0[1,1]          0.9690        0.0614      15.787   0.0000     61.1876
  b[1,1]           0.9690        0.0614      15.787   0.0000    -61.1611
  b[2,1]           0.5180        0.1027       5.045   0.0000      0.0442
  b[3,1]           0.3923        0.0876       4.479   0.0000     -0.0927
  variance[1,1]    0.5718        0.0872       6.560   0.0000     -0.0263

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`cmlmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 
- The results are consistent with our constraints:
  - b0 and b[1, 1] are equal (:math:`b[1, 1] - b0 \geq 0`).
  - 1 - b[2, 1]*b[3, 1]  = :math:`1 - 0.5180 * 0.3923 = 0.79678860 \geq 0`.
- The gradients are not equal to zero, which is indicative that the contraints are binding. 


Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1                1      -0.39397286     0.0035014088     -0.043476943 
               1                1      -0.39397286     0.0035014088     -0.043476943 
     -0.39397287      -0.39397287                1      -0.32458736      0.071588434 
    0.0035014049     0.0035014049      -0.32458735                1       0.03382182 
    -0.043476958     -0.043476958      0.071588438      0.033821801                1 

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit    Gradient
    ----------------------------------------------------------------------
    b0[1,1]          0.9690        0.8471        1.0908       61.1876
    b[1,1]           0.9690        0.8471        1.0908      -61.1611
    b[2,1]           0.5180        0.3141        0.7218        0.0442
    b[3,1]           0.3923        0.2184        0.5662       -0.0927
    variance[1,1]    0.5718        0.3987        0.7448       -0.0263

    Number of iterations    10
    Minutes to convergence     0.00007

