Maximum Likelihood Estimation with Analytic Gradients
======================================================

This **GAUSS** maximum likelihood example demonstrates the use of **MAXLIKMT** to estimate parameters of a tobit modelwith analytic first derivatives. 

Key example features
++++++++++++++++++++++

- Usages of data from the file *maxlikmttobit.dat* (included with **maxlikmt**).
- User defined likelihood function, :class:`lpr` with four inputs:  
    - A parameter vector.   
    - Additional *X* and *y* data matrices, which are passed to :func:`maxlikmt`` as optional arguments.   
    - The required *ind* input.   
- The inclusion of analytic gradient computations, as specified in the :class:`lpr` function.

Code for estimation
----------------------

:: 

    /*
    **   Maximum likelihood tobit model 
    */
    new;
    library maxlikmt;

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

    // Set parameter starting values
    p0 = {1, 1, 1, 1, 1};
   
    // Load data
    z = loadd(getGAUSSHome("pkgs/maxlikmt/examples/maxlikmttobit.dat"));
   
    // Separate X and y
    y = z[., 1];
    x = z[., 2:4];

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

    // Declare 'out' to be a maxlikmtResults
    // struct to hold optimization results 
    struct maxlikmtResults out;
    out = maxlikmtprt(maxlikmt(&lpr, p0, x, y, c0));

Results
-----------
The :func:`maxlikmtprt` procedure prints three output tables:

- Estimation results. 
- Correlation matrix of parameters. 
- Wald confidence limits. 

Estimation results 
++++++++++++++++++++

::

  ===============================================================================
   MAXLIKMT Version 3.0.0                                       
  ===============================================================================

  return code =    0
  normal convergence

  Log-likelihood        -44.8988
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
  Parameters    Estimates     Std. err.  Est./s.e.    Prob.    Gradient
  ---------------------------------------------------------------------
  x[1,1]           1.4303        0.0338     42.348   0.0000      0.0000
  x[2,1]           0.4948        0.0355     13.953   0.0000      0.0000
  x[3,1]           0.4955        0.0413     12.011   0.0000      0.0000
  x[4,1]           0.4119        0.0355     11.596   0.0000      0.0000
  x[5,1]           0.1000        0.0132      7.587   0.0000     90.9995   

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`maxlikmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 

Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1      0.069139065      -0.24058113      0.056496522     -0.088492586 
     0.069139065                1      -0.30744504     -0.060911279       0.04713576 
     -0.24058113      -0.30744504                1      -0.31863882      0.054598226 
     0.056496522     -0.060911279      -0.31863882                1      0.036705333 
    -0.088492586       0.04713576      0.054598226      0.036705333                1 

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                  0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit      Gradient
    ----------------------------------------------------------------------
    x[1,1]           1.4303        1.3632          1.4973        0.0000
    x[2,1]           0.4948        0.4244          0.5652        0.0000
    x[3,1]           0.4955        0.4136          0.5774        0.0000
    x[4,1]           0.4119        0.3414          0.4824        0.0000
    x[5,1]           0.1000        0.0738          0.1262       90.9995

    Number of iterations    16
    Minutes to convergence     0.00442