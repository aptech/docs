Basic Maximum Likelihood Estimation
====================================

This **GAUSS** maximum likelihood example demonstrates the estimation of parameters of a tobit model.  

Key features
+++++++++++++++

- Usages of data from the file *cmlmttobit.dat* (included with *cmlmt*).
- User defined likelihood function, :clas:`lpr` with four inputs:
  - The required PV structure. 
  - Additional *X* and *y* data matrices, which are passed to *cmlmt* as optional arguments. 
  - The required *ind* input. 
- Comparison of parameter vector versus *PV* structure to pass parameters. 

Case One: Use of parameter vector
----------------------------------

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

        // Parameters
        b0 = p[1];
        b = p[2:4];
        s2 = p[5];

        yh = b0 + x * b;
        res = y - yh;
        u = y[., 1] ./= 0;

        // If first element of 'ind' is non-zero,
        // compute function evaluation
        if ind[1];
            mm.function = u.*lnpdfmvn(res, s2) + (1 - u).*(ln(cdfnc(yh/sqrt(s2))));
        endif;

        retp(mm);

    endp;

    // Set parameter starting values
    p0 = {1, 1, 1, 1, 1};
   
    // Load data
    loadd(getGAUSSHome("pkgs/cmlmt/examples/cmlmttobit.dat"));
   
    // Separate X and y
    y = z[., 1];
    x = z[., 2:4];

    // Declare 'out' to be a comtResults
    // struct to hold optimization results 
    struct cmlmtResults out;
    out = cmlmtprt(cmlmt(&lpr, p0, x, y));



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
    CMLMT Version 3.0.0                                       3/25/2024  11:23 pm
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
               1      0.067007218      -0.24418499       0.05530801       -0.1086616 
     0.067007218                1      -0.30495203     -0.061964254      0.058089917 
     -0.24418499      -0.30495203                1      -0.31656527      0.067029865 
      0.05530801     -0.061964254      -0.31656527                1      0.044663539 
      -0.1086616      0.058089917      0.067029865      0.044663539                1 

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                              0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit   Gradient
    ----------------------------------------------------------------------
    x[1,1]           1.4253        1.3507        1.4999        0.0000
    x[2,1]           0.4976        0.4195        0.5757        0.0000
    x[3,1]           0.4992        0.4082        0.5903        0.0000
    x[4,1]           0.4141        0.3358        0.4923        0.0000
    x[5,1]           0.1231        0.0842        0.1620        0.0000

Case Two: Use of PV Structure
----------------------------------
The :func:`cmlmt` also allows the use of the PV parameter structure to pass parameter values to the likelihood function. 

While the parameter vector is generally a simpler method, the PV structure can be useful in certain cases:

-  It allows you to name parameters for easier interpretation of results. 
-  It can be used to fix certain parameters at their start values with :func:`pvPackM`. 
-  It can be used to specify that parameters are a symmetric matrix with :func:`pvPackSM`. 

The code below performs the same estimation as that above but uses the PV structure, in combination with the **pack** procedures to pass parameters. 

::

   new;
   library cmlmt;

   // Tobit likelihood function with 4 inputs
   //    i.      p      - The PV parameter structure
   //    ii-iii. x and y - Extra data needed by the objective procedure
   //    ii.     ind     - The indicator vector 
   proc lpr(struct PV p, x, y, ind);
       local s2, b0, b, yh, u, res;

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
       
       // Return modelResults struct
       retp(mm);

   endp;

   // Declare instance of PV structure
   struct PV p0;
   p0 = pvCreate;

   // Pack parameters into PV structure
   // note that first call to pvPack 
   p0 = pvPack(p0, 1, "b0");
   p0 = pvPack(p0, 1|1|1, "b");
   p0 = pvPack(p0, 1, "variance");

   // Load data
   loadd(getGAUSSHome("pkgs/cmlmt/examples/cmlmttobit.dat"));
   
   // Separate X and y
   y = z[., 1];
   x = z[., 2:4];

   // Declare 'out' to be a comtResults
   // struct to hold optimization results 
   struct cmlmtResults out;
   out = cmlmtprt(cmlmt(&lpr, p0, x, y));


Results
-----------
For the sake of brevity, we won't separate the sections of the results. 

:: 

   ===============================================================================
    CMLMT Version 3.0.0                                       3/25/2024  11:23 pm
   ===============================================================================

   return code =    0
   normal convergence

   Log-likelihood        -43.9860
   Number of cases     100

   Covariance of the parameters computed by the following method:
   ML covariance matrix
     Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
   ---------------------------------------------------------------------
   b0[1,1]          1.4253        0.0376      37.925   0.0000      0.0000
   b[1,1]           0.4976        0.0394      12.642   0.0000      0.0000
   b[2,1]           0.4992        0.0458      10.889   0.0000      0.0000
   b[3,1]           0.4141        0.0394      10.506   0.0000      0.0000
   variance[1,1]    0.1231        0.0196       6.284   0.0000      0.0000

   Correlation matrix of the parameters
                  1      0.067007218      -0.24418499       0.05530801       -0.1086616 
        0.067007218                1      -0.30495203     -0.061964254      0.058089917 
        -0.24418499      -0.30495203                1      -0.31656527      0.067029865 
         0.05530801     -0.061964254      -0.31656527                1      0.044663539 
         -0.1086616      0.058089917      0.067029865      0.044663539                1 



   Wald Confidence Limits

                                 0.95 confidence limits
     Parameters    Estimates     Lower Limit   Upper Limit   Gradient
   ----------------------------------------------------------------------
   b0[1,1]          1.4253        1.3507        1.4999        0.0000
   b[1,1]           0.4976        0.4195        0.5757        0.0000
   b[2,1]           0.4992        0.4082        0.5903        0.0000
   b[3,1]           0.4141        0.3358        0.4923        0.0000
   variance[1,1]    0.1231        0.0842        0.1620        0.0000

   Number of iterations    20
   Minutes to convergence     0.00065


The notable feature of these results, is that parameter names are now included in the output tables. This is because they were provided to the PV structure when the starting values were packed. 

