Optimization with Nonlinear Ineqaulity Constraints
==================================================

This **GAUSS** optimization example demonstrates the use of **COMT** to perform optimization with nonlinear inequality constraints. This example is adapted from: Arora, Rajesh, 'Optimization: Algorithms and Applications',  2015, CRC-Press

Key example features
++++++++++++++++++++++
- The user-defined objective function :class:`fct` with specifications for computing analytical gradients. 
- This examples uses a user-defined function :class:`ineqp` in combination with the *c0.ineqProc* member of the :class:`comtControl` structure to specify the inequality constraints. 


There are two nonlinear inequality constraints that are implemented in this example:

.. math:: `x_1^2 - x_2 + 4 = 0`
.. math:: `(x_1 - 2)^2 - x_2 + 3 = 0`

where  :math:`x_1, x_2` are the parameters to be estimated. 

Specifying inequality constraints 
--------------------------------------------------------------------------
Because the constraints in this example are nonlinear, the only option for specifying is with a user defined function. A pointer to the function must be provided using the *c0.ineqProc* member of the :class:`comtControl` structure.

:: 

  new;
  cls;

  library comt;

  // Nonlinear objective function
  proc fct(x, y, z, ind);
      struct modelResults mm;
      
      if ind[1];
          // Calculate objective function value
          mm.function = (x[1] - y).^2 + (x[2] - z).^2;
      endif;
      
      if ind[2];
          // Calculate analytical gradient
          mm.gradient = zeros(2, 1);
          mm.gradient[1] = 2 .* (x[1] - y);
          mm.gradient[2] = 2 .* (x[2] - z);
      endif;
      
      retp(mm);
  endp;

  // Procedure to compute inequality constraints
  // Add '...' as input so this procedure will
  // ignore extra arguments 'y' and 'z' that
  // will be passed by 'comt'
  proc ineqp(x, ...);
      local constraint_1, constraint_2;
      
      constraint_1 = x[1].^2 - x[2] + 4;
      constraint_2 = (x[1] - 2).^2 - x[2] + 3;
      
      retp(constraint_1 | constraint_2);
  endp;


  // Declare 'c0' to be a comtControl struct
  // and fill with default settings
  struct comtControl c0;
  c0 = comtControlCreate();

  // Assign pointer for nonlinear inequality procedure
  c0.ineqProc = &ineqp;

  // Expand trustRadius for quicker descent
  c0.trustRadius = 1;

  // Starting parameter values
  b0 = { 1, 1 };

  // Extra data needed by objective procedure
  y = 1;
  z = 5;

  // Declare 'out' to be a comtResults
  // struct to hold optimization results
  struct comtResults out;

  // Minimize objective function
  out = comt(&fct, b0, y, z, c0);

  // Print optimization results
  call comtPrt(out);

There code prints results to the **Command Window**. 

Results
++++++++++

Convergence details
^^^^^^^^^^^^^^^^^^^^
The first portion of the results provide details about convergence and performance. 

::

    Return code    = 0   
    Function value = 0.25391   
    Convergence    : normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`comt` documentation. 

Parameter estimates
^^^^^^^^^^^^^^^^^^^^
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]         0.7500     -0.5000
    x[2,1]         4.5625     -0.8750

Computation time 
^^^^^^^^^^^^^^^^^^
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    6
    Minutes to convergence  0.00022
