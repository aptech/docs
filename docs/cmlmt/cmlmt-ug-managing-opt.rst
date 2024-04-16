Managing Optimization
======================

The critical elements in optimization are scaling, starting point, and the condition of the model. When the data are scaled, the starting point is reasonably close to the solution, and the data and
model go together well, the iterations converge quickly and without difficulty.

For best results, therefore, you want to prepare the problem so that model is well-specified, the data scaled, and that a good starting point is available.
The tradeoff among algorithms and step length methods is between speed and demands on the starting point and condition of the model. The less demanding methods are generally time
consuming and computationally intensive, whereas the quicker methods (either in terms of time or number of iterations to convergence) are more sensitive to conditioning and quality of starting point.

Scaling
----------

For best performance, the diagonal elements of the Hessian matrix should be roughly equal. If some diagonal elements contain numbers that are very large and/or very small with respect to the others, **CMLMT** has difficulty converging. How to scale the diagonal elements of the Hessian may not be obvious, but it may suffice to ensure that the constants (or "data") used in the model are about the same magnitude.

Condition
----------

The specification of the model can be measured by the condition of the Hessian. The solution of the problem is found by searching for parameter values for which the gradient is zero. If, however, the Jacobian of the gradient (i.e., the Hessian) is very small for a particular parameter, then **CMLMT** has difficulty determining the optimal values since a large region of the function appears virtually flat to **CMLMT**. When the Hessian has very small elements, the inverse of the Hessian has very large elements and the search
direction gets buried in the large numbers.

Poor condition can be caused by bad scaling. It can also be caused by a poor specification of the model or by bad data. Bad models and bad data are two sides of the same coin. If the problem is highly nonlinear, it is important that data be available to describe the features of the curve described by each of the parameters. For example, one of the parameters of the Weibull function describes the shape of the curve as it approaches the upper asymptote. If data are not available on that portion of the curve, then that parameter is poorly estimated. The gradient of the function with respect to that parameter is very flat, elements of the Hessian associated with that parameter is very small, and the inverse of the Hessian contains very large numbers. In this case it is necessary to respecify the model in a way that excludes that parameter.

Starting Values
----------------
When the model is not particularly well-defined, the starting point can be critical. When the optimization doesn’t seem to be working, try different starting points. A closed form solution may exist for a simpler problem with the same parameters. For example, ordinary least squares estimates may be used for nonlinear least squares problems or nonlinear regressions like probit or logit. There are no general methods for computing start values and it may be necessary to attempt the estimation from a variety of starting points.

Algorithmic Derivatives 
------------------------
**Algorithmic Derivatives** is a program that can be used to generate a **GAUSS** procedure to compute derivatives of the log-likelihood function. If you have **Algorithmic Derivatives**, be sure to read its manual for details on doing this.

First, copy the procedure computing the log-likelihood to a separate file. Second, from the
command line enter

::

    ad file_name d_file_name

where ``file_name`` is the name of the file containing the input function procedure, and ``d_file_name`` is the name of the file containing the output derivative procedure. If the input function procedure is named ``lpr``, the output derivative procedure has the name ``d_A_lpr`` where the addition to the ``_A_`` indicates that the derivative is with respect to the first of the two arguments.

For example, put the following function into a file called ``lpr.fct``.

::

    proc lpr(c,x,y);
        local b, b0, yh, res, yh, u, logl;

        // Procedure computations
        yh = b0 + x * b;
        res = y - yh;

        // Check for non-zero y values 
        u = y[., 1] ./= 0;

        // Log-likelihood
        logl = u.*lnpdfmvn(res, s2) + (1 - u).*(ln(cdfnc(yh/sqrt(s2))));

    retp(logl);
    endp;   

Then enter the following at the **GAUSS** command line

::

    library ad;
    ad lpr.fct d_lpr.fct;

If successful, the following is printed to the screen

::
    java -jar d:\gauss18\src\GaussAD.jar lpr.fct d_lpr.fct

and the derivative procedure is written to file named d_lpr.fct:

::

    /* Version:1.1 */
    /* Generated from:lpr.src */
    /* Taking derivative with respect to argument 1 */
    proc(1)=d_A_lpr(c, x, y);
    
        Clearg _AD_fnValue;
        Local b, b0, yh, res, yh, u, logl;
    
        b0 = c[(1)] ;
        b = c[(2):(4)] ;
        yh = b0 + (x*b);
        res = y - yh;
        u = y[.,(1)] ./= 0;
        logl = (u .* lnpdfmvn(res, s2))+((1-u) .*
        ln(cdfnc(yh /sqrt(s2))));
        _AD_fnValue = logl;
        /* retp(_AD_fnValue); */
                /* endp; */
        struct _ADS_optimum _AD_d_c,_AD_d_b,_AD_d_b0,
        _AD_d_yh,_AD_d_logl,_AD_d_res,_AD_d__AD_fnValue;
        /* _AD_d_b = 0; _AD_d_b0 = 0; _AD_d_yh = 0;
        _AD_d_logl = 0; _AD_d_res = 0; */
        _AD_d__AD_fnValue = _ADP_d_x_dx(_AD_fnValue);
        _AD_d_logl = _ADP_DtimesD(_AD_d__AD_fnValue,
        _ADP_d_x_dx(logl));
        _AD_d_yh = _ADP_DtimesD(_AD_d_logl,_ADP_DtimesD(
        _ADP_d_yplusx_dx(u .* lnpdfmvn(res,s2),(1-u) .*
        ln(cdfnc(yh/sqrt(s2)))),_ADP_DtimesD(
        _ADP_d_ydotx_dx(1 - u, ln(cdfnc(yh/sqrt((s2)))),
        _ADP_DtimesD(_ADP_d_ln(cdfnc(yh/sqrt(s2))),
        _ADP_DtimesD(_ADP_internal(d_cdfnc(yh/sqrt(s2))),
        _ADP_DtimesD(_ADP_d_xdivy_dx(yh,sqrt(s2)),
        _ADP_d_x_dx(yh)))))));
        _AD_d_res = _ADP_DtimesD(_AD_d_logl,_ADP_DtimesD
        (_ADP_d_xplusy_dx(u .* lnpdfmvn(res, s2),
        (1 - u) .* ln(cdfnc(yh/sqrt(s2)))),
        _ADP_DtimesD(_ADP_d_ydotx_dx(u,lnpdfmvn(res, s2)),
        _ADP_DtimesD (_ADP_internal(d_A_lnpdfmvn(res, s2)),
        _ADP_d_x_dx(res)))));
        /* u = y[.,(1)] ./= 0; */
        _AD_d_yh = _ADP_DplusD(_ADP_DtimesD(_AD_d_res,
        _ADP_DtimesD(_ADP_d_yminusx_dx(y, yh),
        _ADP_d_x_dx(yh))),_AD_d_yh);
        _AD_d_b = _ADP_DtimesD(_AD_d_yh, _ADP_DtimesD
        (_ADP_d_yplusx_dx(b0,x * b),_ADP_DtimesD
        (_ADP_d_yx_dx(x, b),_ADP_d_x_dx(b))));
        _AD_d_b0 = _ADP_DtimesD(_AD_d_yh,
        _ADP_DtimesD(_ADP_d_xplusy_dx(b0, x * b),
        _ADP_d_x_dx(b0)));
        Local _AD_s_c;
        _AD_s_c = _ADP_seqaMatrix(c);
        _AD_d_c = _ADP_DtimesD(_AD_d_b,
        _ADP_d_xIdx_dx(c,_AD_s_c[(2):(4)] ));
        _AD_s_c = _ADP_seqaMatrix(c);
        _AD_d_c = _ADP_DplusD(_ADP_DtimesD(_AD_d_b0,
        _ADP_d_xIdx_dx(c, _AD_s_c[(1)] )), _AD_d_c);
        retp(_ADP_external(_AD_d_c));
        endp;

::

    java -jar d:\gauss18\src\GaussAD.jar lpr.fct d_lpr.fct
    Command ’java -jar d:\gauss18\src\GaussAD.jar lpr.fct d_lpr.fct’
    exit status 1

the exit status 1 indicating that an error has occurred. The output file then contains the reason for the error:

::

    /* Version:1.1 - May 15, 2013 */
    /* Generated from:lpr.src */
    /* Taking derivative with respect to argument 1 */
    proc lpr(c,x,y);
    
    local b,b0,yh,res,yh,u,logl;
    
    b0 = c[1];
    b = c[2:4];

    yh = b0 + x * b;
    res = y - yh;
    u = y[.,1] ./= 0;
    logl = u.*lnpdfmvn(res,s2)+(1-u).*(ln(cdfnc
    (yh/sqrt(s2)));
    Error: lpr.src:12:64: expecting ’)’, found ’;’

Finally, call the above procedure from your log-likelihood procedure, for example,

::

    proc lpr(struct PV p, y, x, ind);
        local s2,b0,b,yh,u,res,g1,g2;
        
        // Declare 'modelResults' structure
        struct modelResults mm;
        
        // Unpack parameters 
        b0 = pvUnpack(p, "b0");
        b = pvUnpack(p, "b");
        s2 = pvUnpack(p, "variance");
        
        // Computations 
        yh = b0 + x * b;
        res = y - yh;
        u = y[.,1] ./= 0;
        
        // Computed function values
        if ind[1];
            mm.function = u.*lnpdfmvn(res,s2) + (1-u).*
            (ln(cdfnc(yh/sqrt(s2))));
        endif;
        
        // Compute gradient using AD function
        if ind[2];
            mm.gradient = d_A_lpr(pvGetParvector(p),y,x);
        endif;
        
        retp(mm);
        endp;