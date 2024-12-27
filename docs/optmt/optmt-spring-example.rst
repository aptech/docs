Optimization of a Spring Example
=================================

This **GAUSS** optimization example demonstrates the optimization of the equilibrium of a spring system.  

Code for optimization
----------------------

:: 

    new;
    cls;

    library optmt;


    //Objective function
    proc fct(x, k, F, ind);
        
        //Declare 'mm' to be a modelResults
        //struct, local to this procedure
        struct modelResults mm;

        //If the first element of the indicator vector
        //is non-zero, calculate the objective function
        if ind[1];
            //Assign the value of the objective function to the
            //'function' member of the 'modelResults' struct
            mm.function = k[1] * (sqrt(x[1]^2 + (x[2] + 1)^2) - 1)^2 + k[2] * (sqrt(x[1]^2 + (x[2] - 1)^2) - 1)^2 - (F'x);
        endif;
        
        //Return the modelResults structure
        retp(mm);
    endp; 

    // Starting values
    x0 = { 1, 1 };

    //Extra data needed by function
    k = { 100, 90 };
    F = { 20, 40 };

    //Declare 'out' to be an optmtResults struct
    //to hold the optimization results
    struct optmtResults out;

    //Declare 'ctl' to be an optmtControl structure
    struct optmtControl ctl;

    //Fill 'ctl' with default options
    ctl = optmtControlCreate();

    //Print report on every 5th iteration
    ctl.PrintIters = 5;

    //Use Newton Algorithm
    ctl.Algorithm = 3;

    //Use Strong Wolfe Conditions
    ctl.LineSearch = 4;

    //Minimize objective function
    //Pass in extra data needed by objective function
    //between starting parameters and control structure
    out = optmt(&fct, x0, k, F, ctl);

    //Print optimization results
    call optmtPrt(out);

The code prints results to the **Command Window**. 

Results
-----------
Convergence details
++++++++++++++++++++
The first portion of the results provide details about convergence and performance. 

::

    Return code    =    0
    Function value =   -9.65623
    Convergence    :    normal convergence

These results indicate that the optimization converged normally, with a return code of 0. Any return Code other than 0 would indicate some issue with the convergence. The exact meaning of the return code can be found in the :func:`optmt` documentation. 

Parameter estimates
++++++++++++++++++++
The next section of the results reports the parameter estimates and the associated gradients.

::

    Parameters  Estimates   Gradient
    ---------------------------------------------------------------------
    x[1,1]      0.5044      0.0000
    x[2,1]      0.1219      0.0000

In this example, the gradients are all 0 for the estimates, as is expected at or near an optimum. 

Computation time 
++++++++++++++++++
The final section of the results reports the number of iterations and computation time. 

::

    Number of iterations    6
    Minutes to convergence     0.00123