
QNewton
==============================================

Purpose
----------------
Optimizes a function using the BFGS descent algorithm.

Format
----------------
.. function:: { x, f, g, ret } = QNewton(&fct, start)

    :param &fct: pointer to a procedure that computes the function to be minimized. This procedure must have one input
        argument, a vector of parameter values, and one output argument, the value of the function evaluated
        at the input vector of parameter values.
    :type &fct: function pointer

    :param start: start values.
    :type start: Kx1 vector

    :return x: coefficients at the minimum of the function.

    :type x: Kx1 vector

    :return f: value of function at minimum.

    :type f: scalar

    :return g: gradient at the minimum of the function.

    :type g: Kx1 vector

    :return ret: return code.

        .. csv-table::
            :widths: auto
    
            "0     normal convergence"
            "1     forced termination"
            "2     max iterations exceeded"
            "3     function calculation failed"
            "4     gradient calculation failed"
            "5     step length calculation failed"
            "6     function cannot be evaluated at initial parameter values"

    :type ret: scalar

Global Input
------------

:_qn_RelGradTol: (*scalar*), convergence tolerance for relative gradient of estimated coefficients. Default = 1e-5.

:_qn_GradProc: (*scalar*), pointer to a procedure that computes the gradient of the function with respect 
    to the parameters. This procedure must have a single input argument, a Kx1 vector of parameter values,
    and a single output argument, a Kx1 vector of gradients of the function with respect to the parameters 
    evaluated at the vector of parameter values. If *_qn_GradProc* is 0, :func:`QNewton` uses :func:`gradp`.

:_qn_MaxIters: (*scalar*), maximum number of iterations. Default = 1e+5. Termination can be forced by pressing :kbd:`C` on the keyboard.

:_qn_PrintIters: (*scalar*), if 1, print iteration information. Default = 0. Can be toggled during iterations by 
    pressing :kbd:`P` on the keyboard.

:_qn_ParNames: (*Kx1 vector*), labels for parameters.

:_qn_PrintResults: (*scalar*), if 1, results are printed.


Remarks
-------

If you are running in terminal mode, GAUSS will not see any input until
you press :kbd:`ENTER`. Pressing :kbd:`C` on the keyboard will terminate iterations,
and pressing :kbd:`P` will toggle iteration output.

To reset global variables for this function to their default values,
call :func:`QNewtonSet`.


Examples
----------------
This example computes maximum likelihood coefficients and standard
errors for a Tobit model:

::

    /***qnewton.e - a Tobit model***/
    // Get data
    z = loadd("tobit");
    b0 = { 1, 1, 1, 1 };
    {b,f,g,retcode} = qnewton(&lpr,b0);
     
    // Covariance matrix of parameters
    h = hessp(&lpr,b);
    output file = qnewton.out reset;
     
    print "Tobit Model";
    print;
    print "coefficients standard errors";
    print b~sqrt(diag(invpd(h)));
     
    output off;
     
    // Log-likelihood proc 
    proc lpr(b);
       local s,m,u;
       s = b[4];
       if s <= 1e-4;
          retp(error(0));
       endif;
       m = z[.,2:4]*b[1:3,.];
       u = z[.,1] ./= 0;
       retp(-sumc(u.*lnpdfmvn(z[.,1]-m,s) + (1-u).*(ln(cdfnc(m/sqrt(s))))));
    endp;

::

    Tobit Model
    coefficients standard errors
     
      0.010417884 0.080220019
     -0.20805753  0.094551107
     -0.099749592 0.080006676
      0.65223067  0.099827309

Source
------

qnewton.src

