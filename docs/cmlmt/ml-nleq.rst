Maximum Likelihood Nonlinear Simultaneous Equation Model Estimation
====================================================================

The source code below estimates the coefficients of a general nonlinear system of simultaneous equations:

    .. math::  U = f(Y, X, B)

where :math:`U`` is a :math:`N \times K` matrix of residuals and :math:`f()` is an arbitrary function of :math:`Y`, a :math:`N \times K` matrix of endogenous variables, :math:`X`, an :math:`N \times L` matrix of exogenous variables, and :math:`B`, an :math:`M \times 1` vector of coefficients.  Thus
there are :math:`N` observations, and :math:`f()` represents :math:`K` simultaneous equations.

This example also illustrates constraining the Jacobians.  For a model to be "dynamically stable" the absolute value of the
eigenvalues of I - the Jacobian of the residuals  w.r.t. the endogenous variables must be on the unit interval.  The example below provides for such constraints.

In this example, a procedure is provided for computing the Jacobian of the function with respect to the endogenous variables. This proc, :class:`_nseq_EndoJcb`, is provided, time of computation is reduced significantly.

Code for estimation
----------------------

After loading the library, the first step is to set up the system of nonlinear simultaneous equations:  

    .. math::  Y_1 = b_1 Y_2 + c_1 Y_2 * X_1 + g_1 X_1 + d_1 + U_1
    .. math::  Y_2 = b_2 Y_1 + g_2 X_2 + d_2 + U_2

where :math:`Y_1` and :math:`Y_2` are endogenous, :math:`X_1` and :math:`X_2` are exogenous, and :math:`U_1` and :math:`U_2` are residuals. 
The objective is to estimate the parameter vector :math:`\theta = {b_1, c_1, g_1, d_1, b_2, g_2, d_2` using maximum likelihood.

:: 

    new;
    library cmlmt;

    // Procedure for computing the residuals from 
    // the nonlinear simultaneous equations.  
    proc _nseq_Fct(b, z);
        local u;

        u = zeros(rows(z), 2);

        u[.,1] = z[.,1] - b[1]*z[.,2] - b[2]*z[.,2].*z[.,3] - b[3]*z[.,3] - b[4];
        u[.,2] = z[.,2] - b[5]*z[.,1] - b[6]*z[.,4] - b[7];
        
        retp(u);
    endp;

    // Procedure used in computing the Jacobians of the function
    proc _nseq_EndoJcb(b, xx);
        local j;
        j = zeros(2, 2);
        
        j[1, 1] = 1;
        j[1, 2] = -b[1] - b[2] * xx[., 3];
        j[2, 1] = -b[5];
        j[2, 2] = 1;
        
        retp(j);
    endp;

Next, we'll set up some basic controls for computation of the nonlinear system:

:: 

    /*
    **  Set endoIndices to the indices of the endogenous variables
    **  in the dataset.
    */
    endoIndices = { 1, 2 };


    /*
    **  If Proc _nseq_EndoJcb is NOT provided, set endoJcb to zero.
    **  else if Proc _nseq_EndoJcb IS provided, set endoJcb to 1.
    */

    endoJcb = 1; 

Next, we'll provide the likelihood function and the computational Jacobian function:

::
    
    /*
    **  Likelihood function
    */

    proc lpr(b, z, endoIndices, endoJcb, ind);

        local dev, psi_, g0, oldt, ldet0, ipsi, jb;

        dev = _nseq_Fct(b,z);

        psi_ = dev'dev/rows(z);
        
        // Set trap to check for invertibility
        oldt = trapchk(1);
        trap 1, 1;
            ipsi = invpd(psi_);
        trap oldt, 1;
        
        // Return error if non-invertible
        if scalmiss(ipsi);
            retp(error(0));
        endif;


        ldet0 = ln(detl);
        dev = dev * chol(ipsi)';

        jb = _nseq_Jcb(b, z, endoIndices, endoJcb, 1); /* absolute value of log det of Jacobian */
                                                                            /* of Fct w.r.t. endo. vars. */

        struct modelResults mm;
        mm.function = _ln2pi + jb - 0.5*(ldet0 + sumc((dev.*dev)'));

        retp(mm);
    endp;


    /*
    **  Jacobian of function w.r.t. endogenous variables
    **
    **  ind = 1, compute log of the absolute value of the determinant
    **  ind = 2, compute maximum absolute eigenvalue
    */

    proc _nseq_Jcb(b,  z, endoIndices, endoJcb, ind);
        local i, j, f0, dh, x0, jb, abx, sgnx, ret, en, xx;

        ret = zeros(rows(z), 1);

        i = 1;
        do until i > rows(z);
            xx = z[i,.];
            if endoJcb == 1;
                if ind == 1;
                    ret[i] = ln(abs(det(_nseq_EndoJcb(b, xx))));
                else;
                    jb = _nseq_EndoJcb(b,xx);
                    ret[i] = maxc(abs(eig(eye(rows(jb))-jb)));
                endif;
            else;
                jb = zeros(rows(endoIndices),rows(endoIndices));
                f0 = _nseq_Fct(b, xx);

                x0 = xx[i,endoIndices];
                x0 = x0 + 1e-2*(x0 == 0);
                abx = abs(x0);
                sgnx = x0./abx;

                dh = (1e-8)*maxc(abx|(1e-2)*ones(1, cols(x0))).*sgnx';

                j = 1;
                do until j > cols(x0);
                    en = endoIndices[j];
                    xx[en] = xx[en] + dh[en];
                    jb[j,.] = _nseq_Fct(b, xx);
                    j = j + 1;
                endo;
                if ind == 1;
                    ret[i] = ln(abs(det((jb-f0)./dh)));
                else;
                    jb = (jb-f0)./dh;
                    ret[i] = maxc(abs(eig(eye(rows(jb))-jb)));
                endif;

            endif;
            i = i + 1;
        endo;

        retp(ret);
    endp; 

Now, we're ready to set up the :func:`cmlmt` optimization: 

::

    // Load the data
    z = loadd(getGAUSSHome("pkgs/cmlmt/examples/cmlmtnleq"));

    // Vector of starting values for our 7 parameters
    b0 = { .2, .0, .2, .2, .2, .2, .2 };

    // Declare 'c0' to be a cmlmtControl struct
    // and fill with default settings
    struct cmlmtControl c0;
    c0 = cmlmtControlCreate();
    
    /*
    **   Convergence can sometimes fail because a feasible line search can't
    **   be found.  Thus the line search feasibility test is turned off.
    */
    c0.feasibleTest = 0;

    /*
    **  Constraining the eigenvalues of the Jacobians
    **
    **  The code below illustrates a method for constraining the
    **  absolute value of the eigenvalues of I - the Jacobian of the
    **  residuals w.r.t. the endogenous variables to a unit interval.
    **  If the system of equations being estimated here is a cross-
    **  sectional representation of a dynamic system, this constraint
    **  ensures that it is a "stable" system, i.e., one in a
    **  dynamic equilibrium.
    **
    **  If there are lagged variables in the system, you will need
    **  a more complicated constraint.  See Greene, Econometric
    **  Analysis, page 641ff, for details.
    */
    proc neqp(b, z, endoIndices, endoJcb);
        retp(.99-_nseq_Jcb(b,z,endoIndices,endoJcb,2));
    endp;

    c0.ineqProc = &neqp;

    // Constant used in log-likelihood procedure
    // pulled out of procedure for computational efficiency
    _ln2pi = -0.5 * rows(endoIndices) * ln(2*pi); 

    // Declare 'out' to be a cmlmtResults
    // struct to hold optimization results 
    struct cmlmtResults out;
    out = cmlmt(&lpr,b0, z, endoIndices, endoJcb, c0);

    // Print results
    call cmlmtprt(out);

Results
-----------
The :func:`cmlmtprt` procedure prints three output tables:

- Estimation results. 
- Correlation matrix of parameters. 
- Wald confidence limits. 

Estimation results 
++++++++++++++++++++

::

  ===============================================================================
   CMLMT Version 3.0.0                                       
  ===============================================================================

  return code =    0
  normal convergence

  Log-likelihood        -265.265
  Number of cases     100

  Covariance of the parameters computed by the following method:
  ML covariance matrix
    Parameters    Estimates     Std. err.  Est./s.e.  Prob.    Gradient
  ---------------------------------------------------------------------
  x[1,1]   -0.1224        0.4956      -0.247   0.8050      0.0000
  x[2,1]    0.1176        0.0863       1.362   0.1731      0.0000
  x[3,1]    0.6036        0.3093       1.951   0.0510      0.0000
  x[4,1]    0.6122        0.3734       1.640   0.1011      0.0000
  x[5,1]    0.7219        0.1851       3.899   0.0001      0.0000
  x[6,1]    0.2951        0.1097       2.690   0.0071     -0.0011
  x[7,1]    0.3362        0.1348       2.495   0.0126     -0.0001

The estimation results reports:

- That the model has converged normally with a return code of 0. Any return code other than 0, indicates an issue with convergence. The :func:`cmlmt` documentation provides details on how to interpret non-zero return codes. 
- The log-likelihood value and number of cases. 
- Parameter estimates, standard errors, t-statistics and associated p-values, and gradients. 

Parameter correlations
+++++++++++++++++++++++

::

    Correlation matrix of the parameters
               1      -0.50689926      -0.92087721      -0.95115909       0.22738692      -0.33543423       -0.1759722 
     -0.50689926                1       0.32167663       0.38002565     -0.079802709       0.13764327       0.06266076 
     -0.92087721       0.32167663                1       0.90688866       -0.3135579       0.31601986       0.23706339 
     -0.95115909       0.38002565       0.90688866                1      -0.22985309       0.32358823        0.1165813 
      0.22738692     -0.079802709       -0.3135579      -0.22985309                1      -0.59469942      -0.73925046 
     -0.33543423       0.13764327       0.31601986       0.32358823      -0.59469942                1       0.46284909 
      -0.1759722       0.06266076       0.23706339        0.1165813      -0.73925046       0.46284909                1 

Confidence intervals
+++++++++++++++++++++++

::

    Wald Confidence Limits

                                0.95 confidence limits
    Parameters    Estimates     Lower Limit   Upper Limit    Gradient
    ----------------------------------------------------------------------
    x[1,1]          -0.1224       -1.1065        0.8618        0.0000
    x[2,1]           0.1176       -0.0538        0.2889        0.0000
    x[3,1]           0.6036       -0.0106        1.2178        0.0000
    x[4,1]           0.6122       -0.1293        1.3537        0.0000
    x[5,1]           0.7219        0.3542        1.0895        0.0000
    x[6,1]           0.2951        0.0773        0.5130       -0.0011
    x[7,1]           0.3362        0.0686        0.6038       -0.0001

    Number of iterations    9
    Minutes to convergence     0.00292

