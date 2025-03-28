Comparing CML and CMLMT in GAUSS
================================

Introduction
------------

The **Constrained Maximum Likelihood (CML)** was initially the core tool for constrained maximum likelihood in GAUSS. 
**Constrained Maximum Likelihood MT (CMLMT)** modernized constrained maximum likelihood in GAUSS, allowing users to take advantage of 
significant performance improvements, greater flexibility, and an easier-to-use parameter handling system.

This guide explores the **key features, differences, and benefits of upgrading from CML to CMLMT**, along with 
a practical example to help users transition their code.

Key Features Comparison
-----------------------

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Feature
     - CML (2.0)
     - CMLMT (3.0)
   * - Optimization Algorithm
     - Sequential Quadratic Programming (SQP) with BFGS, DFP, and Newton-Raphson methods.
     - SQP with improved secant algorithms and Cholesky updates for Hessian approximation.
   * - Parallel Computing Support
     - No multi-threading support.
     - Multi-threading enabled for numerical derivatives and bootstrapping.
   * - Log-Likelihood Computation
     - Function and derivatives computed separately, requiring redundant calculations.
     - Unified procedure for computing log-likelihood, first derivatives, and second derivatives, reducing redundant computations.
   * - Parameter Handling
     - Supports only a **simple parameter vector**, which allows flexible parameter management but increases coding complexity.
     - Supports both a **simple parameter vector (easier to use)** and a **PV structure (for advanced parameter management)**. This allows flexible parameter management.
   * - Line Search Methods
     - STEPBT (quadratic/cubic fitting), BRENT, HALF, and BHHHSTEP.
     - Introduces **Augmented Lagrangian Penalty** method for constrained models. Also includes STEPBT (quadratic/cubic fitting), BRENT, HALF, and BHHHSTEP.
   * - Statistical Inference
     - Basic hypothesis testing.
     - Enhanced hypothesis testing for constrained models, including **profile likelihoods, bootstrapping, and Lagrange multipliers**.
   * - Handling of Fixed Parameters
     - Global variables used to fix parameters.
     - Uses **cmlmtControl** structure for setting fixed parameters.
   * - Run-Time Adjustments
     - Uses global variables to modify settings.
     - **Control structures** enable flexible tuning of optimization settings.
   * - Software Requirements
     - Compatible with older GAUSS versions.
     - Requires GAUSS 18+.
   * - output
     - Basic output, returns estimates, likelihood, covariance, and error return code. 
     - Uses an output structure to return estimates, likelihood, covariance, error return code, and additional model information.


Distinct Differences Between CML and CMLMT
------------------------------------------

1. **Threading & Multi-Core Support**: CMLMT enables multi-threading, significantly speeding up numerical derivatives and bootstrapping, whereas CML is single-threaded.
2. **Enhanced Parameter Handling**: Only CMLMT supports both a **simple parameter vector (easier to use)** and the **PV structure** for advanced models. In addition, CMLMT allows for dynamic arguments, making it easier to pass data to the
log-likelihood function.
3. **More Efficient Log-Likelihood Computation**: CMLMT integrates the computation of log-likelihood, first derivatives, and second derivatives into a **single procedure**, reducing redundancy.
4. **Augmented Lagrangian Method**: CMLMT introduces an **Augmented Lagrangian Penalty Line Search** for handling constrained optimization, which is absent in CML.
5. **Enhanced Statistical Inference**: CMLMT includes **bootstrapping, profile likelihoods, and hypothesis testing improvements**, which are limited in CML.

Advantages of Updating from CML to CMLMT
----------------------------------------

- **Easier Parameter Management**: Users can **choose between a simple parameter vector or a PV structure**, making modeling more flexible and intuitive.
- **Improved Performance**: Multi-threading reduces computation time, particularly for large datasets or complex models.
- **More Robust Constraint Handling**: The **cmlmtControl** structure makes managing constraints more explicit and user-friendly.
- **Better Numerical Stability**: Enhanced secant algorithms improve convergence and reduce numerical instability.
- **Accurate Statistical Inference**: Supports **heteroskedastic-consistent covariance estimation**, profile likelihood tests, and bootstrapping.
- **Future Compatibility**: Required for **GAUSS 18+**, ensuring continued support for modern GAUSS features.

Example: Converting a CML Model to CMLMT
-----------------------------------------

This example demonstrates how to transition from CML to CMLMT, focusing on moving from global parameters to the control structure.

**Step 1: Original CML Code**

:: 

    new;
    library cml;
    #include cml.ext;
    cmlset;

    // Load data
    data = loadd(getGAUSSHome("pkgs//cmlmt//examples//cmlmtpsn"));

    // Set constraints for first two coefficients
    // to be equal
    _cml_A = { 1 -1 0 };   
    _cml_B = { 0 };  

    // Specify starting parameters
    beta0 = .5|.5|.5;

    // Run optimization
    { _beta, f0, g, cov, retcode } = CMLprt(cml(data, 0, &logl, beta0));

    // Specify log-likelihood function
    proc logl(b, data);
        local m, x, y;
        
        // Extract x and y
        y = data[., 1];
        x = data[., 2:4];
        
        m = x * b;
        
        retp(y .* m - exp(m));
    endp;
    
This prints the following output:

::

  Mean log-likelihood       -0.670058
  Number of cases     100

  Covariance of the parameters computed by the following method:
  Inverse of computed Hessian

  Parameters    Estimates     Std. err.    Gradient
  ------------------------------------------------------------------
  P01              0.1199        0.1010      0.0670
  P02              0.1199        0.1010     -0.0670
  P03              0.8343        0.2648      0.0000

  Number of iterations    5
  Minutes to convergence     0.00007

**Step 2: Updated CMLMT Code with Control Structure**

::

    new;
    library cmlmt;

    // Load data
    x = loadd(getGAUSSHome("pkgs//cmlmt//examples//cmlmtpsn"));

    // Extract x and y
    y = x[., 1];
    x = x[., 2:4];

    //Declare and initialize control structure
    struct cmlmtControl ctl;
    ctl = cmlmtControlCreate();

    // Set constraints for first two coefficients
    // to be equal
    ctl.A = { 1 -1 0 };   
    ctl.B = { 0 };       

    // Specify starting parameters
    beta0 = .5|.5|.5;

    // Run optimization
    struct cmlmtResults out;
    out = cmlmtPrt(cmlmt(&logl, beta0, y, x, ctl));

    // Specify log-likelihood function
    proc logl(b, y, x, ind);
        local m;
        struct modelResults mm;

        m = x * b;
        
        if ind[1];
            mm.function = y .* m - exp(m);
        endif;

        retp(mm);
    endp;

This prints the following output:

::
  
  Log-likelihood        -67.0058
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
    Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
  ---------------------------------------------------------------------
  x[1,1]    0.1199        0.1010       1.188   0.2350     -6.7011
  x[2,1]    0.1199        0.1010       1.188   0.2350      6.7002
  x[3,1]    0.8343        0.2648       3.151   0.0016     -0.0002

  Correlation matrix of the parameters
                1                1      -0.88718269 
                1                1      -0.88718269 
      -0.88718269      -0.88718269                1 



  Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit   Gradient
  ----------------------------------------------------------------------
  x[1,1]    0.1199       -0.0805        0.3202       -6.7011
  x[2,1]    0.1199       -0.0805        0.3202        6.7002
  x[3,1]    0.8343        0.3087        1.3598       -0.0002

  Number of iterations    8
  Minutes to convergence     0.00002
    

**Step 3: Key Changes Explained**

1. **Moving from Global Variables to Control Structures**: Instead of using `_cml_A` and , `_cml_B` the new code explicitly defines `ctl.A` and `ctl.B` inside a `cmlmtControl` structure.
2. **Simpler Parameter and Data Handling**: Pass `Y` and  `X` separately in **CMLMT**. Dynamic arguments allows us to pass an unlimited number of data vectors and fixed parameter vectors. This can reduce the complexity of the log-likelihood function, and speed up optimization. 
3. **New Log-Likelihood Return Structure**: The **log-likelihood function** now returns a **`modelResults` structure** in CMLMT.
4. **New Output Structure**: Optimization in **CMLMT** returns a **cmlmtOut**.

Conclusion
----------

Upgrading from **CML to CMLMT** provides **faster performance, improved numerical stability, and easier parameter management**. 
The addition of multi-threading, better constraint handling, and enhanced statistical inference makes CMLMT a powerful update for GAUSS users.

If you're still using CML, consider transitioning to CMLMT for a **more efficient and flexible modeling experience**!
