cmlmtBoot
==============================================

Purpose
-------
Computes bootstrapped constrained maximum likelihood estimates.

Format
------
.. function:: out = cmlmtBoot(&modelProc, par [, ..., c1])

    :param &modelProc: Pointer to a procedure that computes the function to be minimized.
    :type &modelProc: pointer

    :param par: An instance of a PV structure, constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional arguments that will be passed to the user-provided log-likelihood function. Can include any GAUSS data type or a DS structure for dataset handling.
    :type ...: Various

    :param c1: Optional input. Instance of a :class:`cmlmtControl` structure containing the following members:

        .. include:: include/cmlmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`cmlmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures.

        .. include:: include/cmlmtresultsstruct.rst

    :rtype out: struct

Example
-------
Examples
----------
The following is a complete example. It applys the Biochemical Oxygen Demand model to data
taken from Douglas M. Bates and Donald G. Watts, **Nonlinear Regression Analysis and Its
Applications**, page 270.

::

    new;
    library cmlmt;
    
    // Likelihood function
    proc lnlk(struct PV p, y, x, ind);
    local dev,s2,m,r,b0,b;
    
        // Declare 'mm' to be a modelResults
        // struct local to this procedure, 'lnlk'
        struct modelResults mm;
        
        // Unpack parameters
        b0 = pvUnpack(p, 1);
        b = pvUnpack(p, 2);
        
        // Function computations
        r = exp(-b*x);
        m = 1 - r;
        dev = y - b0*m;
        s2 = dev'dev/rows(dev);
        
        // If the first element of the indicator
        // vector is non-zero, compute function value
        // and assign it to the 'function' member
        // of the modelResults struct
        if ind[1];
            mm.function = lnpdfmvn(dev,s2);            
        endif;

        / If the first element of the indicator
        // vector is non-zero, compute gradient value
        // and assign it to the 'gradient' member
        // of the modelResults struct
        if ind[2];
            mm.gradient = (dev/s2) .*
            (m ~ b0*x.*r);
        endif;
        retp(mm);
    endp;

    // Enter data
    y = { 8.3,
    10.3,
    19.0,
    16.0,
    15.6,
    19.8 };

    x = { 1,
    2,
    3,
    4,
    5,
    7 };

    // Pack starting values into 
    // PV structure
    struct PV p0;
    p0 = pvPacki(pvCreate,19.143,"b0",1);
    p0 = pvPacki(p0,0.5311,"b",2);

    // Declare instance of cmlmtControl structure
    struct cmlmtControl ctl;
    ctl = cmlmtControlCreate();

    // Set parameter bounds to 
    //   10 <= b0 <= 35
    //   0 <= b <= 2
    ctl.bounds = { 10 35,
                   0 2 };
    
    // Number of observations 
    c0.NumObs = rows(y);

    //Declare 'out' to be a 'cmlmtResults' structure
    //to hold the estimation results
    struct cmlmtResults out;

    //Perform the estimation
    out = cmlmtboot(&lnlk, p0, y, x, ctl);
 