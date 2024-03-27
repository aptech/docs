Optimization with Linear Equality Constraints
=================================================

This **GAUSS** optimization example demonstrates the use of **COMT** to perform optimization with linear equality constraints. 

Key example features
++++++++++++++++++++++
- The user-defined objective function :class:`fct` for computing the Woods Function. 
- The first case uses :class:`comtControl` linear equality members, *c0.A* and *c0.B*, to specify equality constraints.
- The second case uses a user-defined function :class:`eqp` in combination with the *c0.eqProc* member of the :class:`comtControl` structure to specify the equality constraints. 
- The *c0.bounds* member of the :class:`comtControl` stucture is used to set all parameter values between -10 and 10. 

There are four linear equality constraints that are implemented in this example:

.. math:: `x_1 + 3x_2 = 0`
.. math:: `x_3 + x_4 - 2x_5 = 0`
.. math:: `x_2 - x_5 = 0`

where  :math:`x_1, x_2, \ldots, x_5` are the parameters to be estimated. 

Case One: Specifying equality constraints with control structure matrices 
--------------------------------------------------------------------------
In this case, two members of the :class:`comtControl` are used to specify equality constraints. These set up the constraints based on the relationship:

.. math:: `A(\theta) = B`

The *c0.A* matrix is used to specify the LHS of the equality constraints:

- Each row represents one constraint. In other words, the matrix should have the same number of rows as there are constraints. 
- Each column reprents one parameter. In other words, the matrix should have the same number of columns as there are parameters. 
  
The *c0.B* vector is used to specify the RHS of the equality constraints:

- Each row represents one constraint. The matrix should have the same number of rows as there are constraints. 
- Always has one column. 
  
:: 

  new;
  cls;
  library comt;

  // Nonlinear objective function
  proc fct(x, ind);
      struct modelResults mm;
      
      if ind[1];
          // Calculate objective function value
          mm.function = (x[1] - x[2])^2 + (x[2] + x[3]- 2)^2 + (x[4] - 1)^2 + (x[5] - 1)^2;
      endif;
      
      // Return modelResults struct
      retp(mm);
  endp;

  // Declare 'c0' to be a comtControl struct
  // and fill with default settings
  struct comtControl c0;
  c0 = comtControlCreate();

  /*
  ** Specify equality constraints
  */
  // The c0.A matrix represents represents the LHS
  // of the equality constraints. 
  // Each row represents one constraint.
  // Each column represents a parameter. 
  // The matrix should have:
  //   - the same number of rows as constraints
  //   - the same number of columns as parameters 
  c0.A = {1 3 0 0 0,
          0 0 1 1 -2,
          0 1 0 0 -1};

  c0.B = 0;

  // Turn off trust radius
  c0.trustRadius = error(0);

  // Bound all parameters to be between -10 and +10
  c0.bounds = { -10 10 };

  // Use Newton descent method
  c0.algorithm = 3;

  // Starting parameter values
  x0 = { 2, 2, 2, 2, 2 };

  // Declare 'out' to be a comtResults
  // struct to hold optimization results
  struct comtResults out;

  // Minimize objective function
  out = comt(&fct, x0, c0);

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
    Function value = 4.09302   
    Convergence    : normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`comt` documentation. 

Parameter estimates
^^^^^^^^^^^^^^^^^^^^
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]        -0.7675     -2.0465
    x[2,1]         0.2558     -0.1861
    x[3,1]         0.6279     -2.2326
    x[4,1]        -0.1162     -2.2325
    x[5,1]         0.2558     -1.4884

Computation time 
^^^^^^^^^^^^^^^^^^
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    25
    Minutes to convergence  0.00028

Case Two: Specifying equality constraints with user-defined equality function 
------------------------------------------------------------------------------
In this case, the same optimization is performed, using a procedure to define the equality constraints. Whenan equation is used to specify constraints, a pointer to the function must be provided using the *c0.eqProc* member of the :class:`comtControl` structure. 

::

    new;
    cls;
    library comt;

    // Nonlinear objective function
    proc fct(x, ind);
        struct modelResults mm;
        
        if ind[1];
            // Calculate objective function value
            mm.function = (x[1] - x[2])^2 + (x[2] + x[3] - 2)^2 + (x[4] - 1)^2 + (x[5] - 1)^2;
        endif;
        
        // Return modelResults struct
        retp(mm);
    endp;

    // Procedure to compute equality constraints
    // this must specify the constraint such that
    // eqp(x) = 0
    proc eqp(x);
        local result;

        // This will be returned and
        // it should be a vector of zeros
        // with the same number of rows as constraints
        result = zeros(3, 1);
        
        // Constraint one 
        result[1] = x[1] + 3*x[2];
        
        // Constraint two 
        result[2] = x[3] + x[4] - 2 * x[5];
        
        // Constraint three 
        result[3] = x[2] - x[5];
        
        retp(result);
    endp;

    // Declare 'c0' to be a comtControl struct
    // and fill with default settings
    struct comtControl c0;
    c0 = comtControlCreate();

    // Turn off trust radius
    c0.trustRadius = error(0);

    // Assign pointer for equality procedure
    c0.eqProc = &eqp;

    // Bound all parameters to be between -10 and +10
    c0.bounds = { -10 10 };

    // Use Newton descent method
    c0.algorithm = 3;

    // Starting parameter values
    x0 = { 2, 2, 2, 2, 2 };

    // Declare 'out' to be a comtResults
    // struct to hold optimization results
    struct comtResults out;

    // Minimize objective function
    out = comt(&fct,x0,c0);

    // Print optimization results
    call comtPrt(out);

Results
++++++++++
We can confirm that these results match those from the first case. 

::

    Return code    = 0   
    Function value = 4.09302   
    Convergence    : normal convergence

    Parameters  Estimates    Gradient
    ---------------------------------------------------------------------
    x[1,1]        -0.7674     -2.0465
    x[2,1]         0.2558     -0.1861
    x[3,1]         0.6279     -2.2326
    x[4,1]        -0.1163     -2.2325
    x[5,1]         0.2558     -1.4884


    Number of iterations    63
    Minutes to convergence  0.00050   