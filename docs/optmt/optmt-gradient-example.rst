Optimization with Analytic Gradient Computations
=================================================
This **GAUSS** optimization example demonstrates nonlinear least squares estimation. The data for this example is taken from G.P.Y Cleark,  "Approximate Confidence  Limits for a Parameter Function in Nonlinear Regression", JASA, 82:221-230, 1987.

The key feature of this example is the use of user-defined analytical first derivatives. 

Code for optimization
----------------------
The example:

- Creates a data matrix.
- Defines an objective function that takes 5 inputs. 
- Specifies analytical computations for the gradients. 

:: 

    new;
    cls;

    // Make optmt library available
    library optmt;

    /*
    ** data  -  weight of cut grass from 10 randomly sited quadrants taken
    **          each week for 13 weeks from a grazing pasture.
    */
    y = { 3.183,
        3.059,
        2.871,
        2.622,
        2.541,
        2.184,
        2.110,
        2.075,
        2.018,
        1.903,
        1.770,
        1.762,
        1.550 };

    x = seqa(1, 1, 13);

    // number of observations
    n = 10;

    // The Mitcherlitz Equation
    proc Mitcherlitz(b, x);
        
        // Calculate and return Mitcherlitz equation
        retp(b[3] + b[2]*exp(-b[1]*x));
    endp;

    // The Gradient
    proc dMitcherlitz(b, x);
        local w;
        
        w = exp(-b[1]*x);
        retp(((-b[2]*x.*w)~w~ones(rows(w), 1)));
    endp;


    // The objective function
    proc fct(b, x, y, nobs, ind);
        local dev;
        struct modelResults mm;
        
        dev = y - Mitcherlitz(b,x);
        
        // If first element of 'ind' is non-zero,
        // calculate and return objective function
        if ind[1];
            mm.function = dev'dev/nobs;
        endif;
        
        // If the second element of 'ind' is non-zero,
        // calculate and return gradient
        if ind[2];
            mm.gradient = -2*(dMitcherlitz(b,x)'dev)/nobs;
        endif;
        
        retp(mm);
    endp;

    // 3x1 vector of starting values
    b0 = { 1, 1, 0 };

    // Declare 'out' to be an optmtResults structure
    // to hold the results of the optimization
    struct optmtResults out;

    // Optimize function
    out = optmt(&fct, b0, x, y, n);

    // Print summary report of optimization results
    call optmtPrt(out);

The code prints results to the **Command Window**. 

Results
-----------
Convergence details
++++++++++++++++++++
The first portion of the results provide details about convergence and performance. 

::

    Return code    =    0
    Function value =    0.00535
    Convergence    :    normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`optmt` documentation. 

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

   Parameters  Estimates   Gradient
   ---------------------------------------------------------------------
   x[1,1]      0.1031      0.0000
   x[2,1]      2.5190      0.0000
   x[3,1]      0.9631      0.0000

In this example, the gradients for parameters all parameters are zero, as is expected at or near an optimum. 

Computation time 
++++++++++++++++++

::

    Number of iterations    28
    Minutes to convergence     0.00013

Extension
-----------
Though the printed results do not include the standard errors of the parameters or the other key inference statistics, these can be easily computed the :class:`dMitcherlitz` function and the results stored in the :class:`optmtResults` structure. 

::

    // Extract estimated parameters 
    bhat = pvGetParvector(out.par);
    
    // Compute gradients
    grad = dMitcherlitz(bhat,x);
    
    // Find covariance matrix
    cov = out.fct*invpd(grad'*grad);

    // Print results
    print;
    print "standard errors of parameters";
    sd = sqrt(diag(cov));
    print sd';
    print;
    print "Correlation matrix of parameters";
    print cov./sd./sd';
    print;
    print "t-statistics";
    print (bhat./sd)'; 

The results printed are:

::

    standard errors of parameters
         0.025504306       0.26577209       0.32158853 

    Correlation matrix of parameters

           1.0000000     -0.92330571       0.98410596 
         -0.92330571       1.0000000      -0.97238973 
          0.98410596     -0.97238973        1.0000000 

    t-statistics
          4.0406689        9.4780502        2.9948710