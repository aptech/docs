Basic Optimization Example
===========================

This **GAUSS** optimization example demonstrates the minimization of a quadratic function as outlined in Luenberger's "Linear and Nonlinear Programming." 

Code for optimization
----------------------
The example:

- Creates a data matrix.
- Defines an objective function that takes 4 inputs. 

:: 

    new;
    cls;

    // Make optmt library available
    library optmt;

    // Create data needed by objective procedure
    omega = { 0.78 -0.02 -0.12 -0.14,
       -0.02  0.86 -0.04  0.06,
       -0.12 -0.04  0.72 -0.08,
       -0.14  0.06 -0.08  0.74 };

    b = { 0.76, 0.08, 1.12, 0.68 };

    // Objective procedure with 4 inputs:
    //    i.      x       - The parameter vector
    //    ii-iii. Q and b - Extra data needed by the objective procedure
    //    ii.     ind     - The indicator vector
    proc  qfct(x, omega, b, ind);
      
      // Declare 'mm' to be a modelResults
      // struct local to this procedure, 'qfct'
      struct modelResults mm;
     
      // If the first element of the indicator
      // vector is non-zero, compute function value
      // and assign it to the 'function' member
      // of the modelResults struct
      if ind[1];
          mm.function = 0.5*x'*omega*x - x'b;
      endif;
      
      // Return modelResults struct
      retp(mm);
    endp;

    // Starting parameter values
    x_strt = { 1, 1, 1, 1 };

    // Declare 'out' to be a optmtResults struct
    // to hold the results from the optimization
    struct optmtResults out;

    // Minimize objective function
    out = optmt(&qfct, x_strt, omega, b);

    // Print output to the screen
    call optmtPrt(out);

The code prints results to the **Command Window**. 

Results
-----------
Convergence details
++++++++++++++++++++
The first portion of the results provide details about convergence and performance. 

::

    Return code    = 0   
    Function value = -2.17466  
    Convergence    : normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`optmt` documentation. 

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]         1.5350      0.0000
    x[2,1]         0.1220      0.0000
    x[3,1]         1.9752      0.0000
    x[4,1]         1.4130      0.0000

In this example, the gradients are all 0 for the estimates, as is expected at or near an optimum. 

Computation time 
++++++++++++++++++
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    10
    Minutes to convergence     0.00013 