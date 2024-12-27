Optimization with Analytic Hessian Computations
=================================================

This GAUSS optimization example demonstrates the use of **COMT** to estimate the parameters of the Woods Function. This example moves beyond basic optimization and uses a user-defined function to analytically compute both the first derivatives and second derivatives. 

The Wood Function is a common function for testing optimization performance. Notably, it converges at { 1, 1, 1, 1 } with a function value of 0.

Key example features
++++++++++++++++++++++

- The user-defined objective function :class:`fct` for computing the Woods Function. 
- The specification of analytic gradients inside :class:`fct`.
- The specification of the analytic Hessian inside :class:`fct`

Code for optimization
----------------------

:: 

  new;
  library comt;

  // Create extra data needed for
  // Hessian calculation
  H = { 0   0   0   0, 
        0 220.2 0  19.8,
        0   0   0   0,
        0  19.8 0 200.2 };

  // Starting parameter vector
  x_strt = { -3, -1, -3, -1 };

  // Objective procedure
  proc fct(x, H, ind);
      local h0;
      struct modelResults mm;
     
      // If first element of indicator vector is non-zero,
      // compute objective function
      if ind[1];
          // Compute objective function
          mm.function = 100*(x[2]-x[1]^2)^2 + (1-x[1])^2 + 90*(x[4]-x[3]^2)^2 +
            (1-x[3])^2 + 10.1*((x[2]-1)^2 + (x[4]-1)^2) + 19.8*(x[2]-1)*(x[4]-1);
      endif;

      if ind[2];
          // Compute gradient
          local a,b;
          a = x[2] - x[1]^2;
          b = x[4] - x[3]^2;
          mm.gradient = zeros(1,4);
          mm.gradient[1] = -2*(200*x[1]*a + 1 - x[1]);
          mm.gradient[2] = 2*(100*a + 10.1*(x[2]-1) + 9.9*(x[4]-1));
          mm.gradient[3] = -2*(180*x[3]*b + 1 - x[3]);
          mm.gradient[4] = 2*(90*b + 10.1*(x[4]-1) + 9.9*(x[2]-1));
      endif;


      if ind[3];
          // Compute Hessian
          mm.hessian = H;
          mm.hessian[1,1] = -2*(200*(x[2]-x[1]^2) - 400*x[1]^2 - 1);
          mm.hessian[1,2] = -400*x[1];
          mm.hessian[2,1] = mm.hessian[1,2];
          mm.hessian[3,3] = -2*(180*(x[4]-x[3]^2) - 360*x[3]^2 - 1);
          mm.hessian[4,3] = -360*x[3];
          mm.hessian[3,4] = mm.hessian[4,3];
       endif;

       // Return modelResults struct
       retp(mm);
  endp;

  // Declare 'out' to be a comtResults struct
  struct comtResults out;

  // Minimize objective function
  out = comt(&fct, x_strt, H);

  // Print results of the optimization
  call comtPrt(out);

The code prints results to the **Command Window**. 

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
    Function value = 0.00000   
    Convergence    : normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`comt` documentation. 

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]         1.0000      0.0000
    x[2,1]         1.0000      0.0000
    x[3,1]         1.0000      0.0000
    x[4,1]         1.0000      0.0000


Computation time 
++++++++++++++++++
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    2572
    Minutes to convergence  0.00793