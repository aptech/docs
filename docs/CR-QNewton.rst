
QNewton
==============================================

Purpose
----------------
Optimizes a function using the BFGS descent algorithm.

Format
----------------
.. function:: QNewton(&fct, start)

    :param &fct: pointer to a procedure that computes the function to be minimized. This procedure must have one input
        argument, a vector of parameter values, and one output argument, the value of the function evaluated
        at the input vector of parameter values.
    :type &fct: TODO

    :param start: start values.
    :type start: Kx1 vector

    :returns: x (*Kx1 vector*), coefficients at the minimum of the function.

    :returns: f (*scalar*), value of function at minimum.

    :returns: g (*Kx1 vector*), gradient at the minimum of the function.

    :returns: ret (*scalar*), return code.

    .. csv-table::
        :widths: auto

        "0     normal convergence"
        "1     forced termination"
        "2     max iterations exceeded"
        "3     function calculation failed"
        "4     gradient calculation failed"
        "5     step length calculation failed"
        "6     function cannot be evaluated at initial parameter values"

Remarks
-------

If you are running in terminal mode, GAUSS will not see any input until
you press ENTER. Pressing C on the keyboard will terminate iterations,
and pressing P will toggle iteration output.

To reset global variables for this function to their default values,
call QNewtonSet.


Examples
----------------
This example computes maximum likelihood coefficients and standard
errors for a Tobit model:

::

    /***qnewton.e - a Tobit model***/
    //Get data
    z = loadd("tobit");
    b0 = { 1, 1, 1, 1 };
    {b,f,g,retcode} = qnewton(&lpr,b0);
     
    //Covariance matrix of parameters
    h = hessp(&lpr,b);
    output file = qnewton.out reset;
     
    print "Tobit Model";
    print;
    print "coefficients standard errors";
    print b~sqrt(diag(invpd(h)));
     
    output off;
     
    //Log-likelihood proc 
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

optimize function BFGS descent algorithm
