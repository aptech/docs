Optimization with Analytic Gradient Computations
=================================================

This **GAUSS** optimization example demonstrates the use of **COMT** to estimate parameters using the sum of the squared residuals. This example moves beyond basic optimization and uses a user-defined function to  compute the analytical first derivatives. 

Key example features
++++++++++++++++++++++

- The user-defined objective function :class:`ssq` for computing the sum of the squared residuals. 
- The user-defined gradient function :class:`grd` used for computing the first derivatives. 

Code for optimization
----------------------

:: 

  new;
  cls;

  library comt;

  // Create dependent and independent variables
  y = { 109,
        149,
        149,
        191,
        213,
        224 };

  x = { 1,
        2,
        3,
        5,
        7,
        10 };

  // Starting parameter values
  b_strt =  { 100, 0.75 };

  // Objective procedure, to compute sum of squared residuals, with 4 inputs:
  //    i.      x       - The parameter vector.
  //    ii-iii. y and x - Dependent and independent variable
  //                      for nonlinear least squares estimation.
  //    ii.     ind     - The indicator vector.

  proc (1) = ssq(b, y, x, ind);
      // Declare 'mm' to be a modelResults
      // struct local to this procedure
      struct modelResults mm;
      
      local f,g;
      
      // Calculate 'f' once, for use
      // in computation of function value
      // and gradient calculation
      f = b[1] * (1 - exp(-b[2]*x));
      
      // If first element of 'ind' is non-zero,
      // compute function evaluation
      if ind[1];
          mm.function = (y - f)'(y - f);
      endif;
      
      // If second element of 'ind' is non-zero,
      // compute gradient calculation
      if ind[2];
          g = grd(b, y, x);
          mm.gradient = -2 * g'(y - f);
      endif;
      
      // Return modelResults struct
      retp(mm);
  endp;

  // Procedure used in gradient computation
  // Note this procedure must take the same inputs as 
  // the objective function (excluding 'ind')
  proc grd(b, y, x);
      local f,g;
      
      g = zeros(rows(x),rows(b));
      
      f = exp(-b[2]*x);
      
      g[.,1] = 1 - f;
      g[.,2] = b[1]*x.*f;
      
      retp(g);
  endp;

  // Declare 'ctl' to be a comtControl struct
  // and fill with default settings
  struct comtControl ctl;
  ctl = comtControlCreate();

  // Print numerical and analytical gradient
  // on first iteration for comparison and debugging
  ctl.gradCheck = 1;

  // Declare 'out' to be a comtResults struct
  // to hold the results from the optimization
  struct comtResults out;

  // Minimize objective function
  // and print output to the screen
  out = comtPrt(comt(&ssq, b_strt, y, x, ctl));

There code prints results to the **Command Window**. 

Results
-----------
Gradient comparisons
++++++++++++++++++++
The first notable component of the results is the printed comparison of the analytical and numerical gradients. This is done because the *ctl.gradCheck* member of the :class:`comtControl` structure was set to 1. 

::

    analytical gradient        numerical gradient
    -932.8196153813061073     -932.8196069540683766
    -18609.6357937713837600     -18609.6345830073878460 

Convergence details
++++++++++++++++++++
The first portion of the results provide details about convergence and performance. 

::

    Return code    = 0   
    Function value = 1168.00888
    Convergence    : normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`comt` documentation. 

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]       213.8094      0.0000
    x[2,1]         0.5472      0.0002


Computation time 
++++++++++++++++++
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    2572
    Minutes to convergence  0.00793

Extension
-----------
Though the printed results do not include the standard errors of the parameters or the other key inference statistics, these can be easily computed the :class:`grd` function and the results stored in the :class:`comtResults` structure. 

::

    // Extract estimated parameters
    b_hat = pvGetParVector(out.par);

    // Calculate gradient at the estimated parameters
    g = grd(b_hat, y, x);

    // Compute covariance matrix using 
    // the final function value and 
    // the gradient at estimated parameters
    cov = (out.fct/rows(y))*invpd(g'*g);

    // Find standard errors of estimates 
    sd = sqrt(diag(cov));
    print "Standard errors of parameters:";
    print sd';

    // Find t-stats of estimates 
    t_stats = (b_hat./sd)';
    print "Parameter t-statistics:";
    print t_stats; 

This prints the standard errors and t-statistics.

::

    Standard errors of parameters:
       10.087419      0.085372828 
    Parameter t-statistics:
       21.195650        6.4099726 