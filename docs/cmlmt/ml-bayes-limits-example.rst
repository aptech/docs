Maximum Likelihood Estimation with Bayesian Inference
==================================================================

This **GAUSS** maximum likelihood example demonstrates the use of **CMLMT** to estimate parameters of a tobit model with Bayesian inferences.


Key example features
++++++++++++++++++++++

- Usages of data from the file *cmlmttobit.dat* (included with **cmlmt**).
- User defined likelihood function, :class:`lpr` with four inputs:
  - A PV structure storing parameters. 
  - Additional *X* and *y* data matrices, which are passed to :func:`cmlmt`` as optional arguments. 
  - The required *ind* input. 
- The inclusion of analytic gradient computations, as specified in the :class:`lpr` function.
- The use of the :func:`cmlmtBayes` procedure to compute Bayesian bootstrapped coefficients. 
- Use of the :func:`cmlmtKernelDensity` function to compute and plot the kernel density estimate.

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

    // Specify number of observations
    c0.numObs = rows(z);
    
    // Number of samples
    c0.numSamples = 200;
    
    // Bayes files for storage
    c0.bayesFileName = "bayes";
    
    // Specify the unit normal prior
    proc prior(b);
       retp(prodc(pdfn(b)));
    endp;
    
    c0.priorProc = &prior;
    
    // Declare 'out' to be a cmlmtResults
    // struct to hold optimization results 
    struct cmlmtResults out1;
    out1 = cmlmtBayes(&lpr, p0, y, x, c0);

Results
-----------
The :func:`cmlmtprt` procedure prints three output tables:

- Estimation results. 
- Correlation matrix of parameters. 
- Wald confidence limits. 

In addition to the printed tables, the bootstrapped coefficients are automatically saved to a file named, *bayes.dat*. 

Estimation results 
++++++++++++++++++++

::

    ===============================================================================
     CMLMT Version 3.0.0                                       
    ===============================================================================

    return code =    0
    normal convergence

    Log-likelihood        -50.8773
    Number of cases     200

    Covariance of the parameters computed by the following method:
    Bayesian Bootstrap
      Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
    ---------------------------------------------------------------------
    b0[1,1]          1.4266        0.0556      25.645   0.0000     -1.9867
    b[1,1]           0.5000        0.0545       9.171   0.0000     -2.6873
    b[2,1]           0.5029        0.0718       7.002   0.0000     -4.3997
    b[3,1]           0.4135        0.0539       7.673   0.0000     -2.0459
    variance[1,1]    0.1132        0.0251       4.508   0.0000    118.0353

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`cmlmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 


Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1      -0.13227858      -0.47319401       0.15158244       -0.2380634 
     -0.13227858                1      -0.31695919      -0.13999438       0.20494961 
     -0.47319401      -0.31695919                1      -0.23705915      0.040469787 
      0.15158244      -0.13999438      -0.23705915                1     -0.024213787 
      -0.2380634       0.20494961      0.040469787     -0.024213787                1 


Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit    Gradient
    ----------------------------------------------------------------------
    b0[1,1]          1.4266        1.3033        1.4102       -1.9867
    b[1,1]           0.5000        0.3583        0.5058       -2.6873
    b[2,1]           0.5029        0.3268        0.5147       -4.3997
    b[3,1]           0.4135        0.2552        0.3981       -2.0459
    variance[1,1]    0.1132        0.0782        0.1335      118.0353

    Number of iterations    48
    Minutes to convergence     0.00041

Extension
--------------
The :func:`cmlmtKernelDensity` is useful after the :func:`cmlmtBayes` procedure to visualize the coefficient distributions. It takes the output file from :func:`cmlmtBayes`, *bayes.dat*, and a :class:`cmlmtKernelDensityControl` structure. 

:: 

    call cmlmtKernelDensity("bayes",cmlmtKernelDensityControlCreate);

This will generate a kernel density plot for each of the bootstrapped coefficients. 
