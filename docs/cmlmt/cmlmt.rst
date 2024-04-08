cmlmt
=====

Purpose
-------
Solve the nonlinear programming problem.

Format
------
.. function:: out = cmlmt(&modelProc, par [, ..., c1])

   :param &modelProc: Pointer to a procedure that computes the function to be minimized.
   :type &modelProc: function pointer

   :param par: An instance of a :class:`PV` structure. The par instance is passed to the user-provided procedure pointed to by &fct. par is constructed using the "pack" functions.
   :type par: struct

   :param ...: Optional input arguments. They can be any set of structures, matrices, arrays, strings required to compute the function. Can include GAUSS data types or a DS structure for dataset manipulation. Specific usage depends on the requirements of the `modelProc`.
   :type ...: various
   
   :param c1: An instance of a :class:`cmlmtControl` structure. It is an optional argument. If none is provided, default values will be set. Members of this instance can be set to other values to control various aspects of the optimization process.
   
        .. include:: include/cmlmtcontrolstruct.rst

   :type c1: struct

   :return out: An instance of a :class:`cmlmtResults` structure containing the optimization results, including parameter estimates and diagnostics.
   
        .. include:: include/cmlmtresultsstruct.rst

   :rtype out: struct

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

        // If the first element of the indicator
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

    //Declare 'out' to be a 'cmlmtResults' structure
    //to hold the estimation results
    struct cmlmtResults out;

    //Perform the estimation
    out = cmlmt(&lnlk, p0, y, x, ctl);
    
    //Print the results
    call cmlmtPrt(out);
    
Remarks
-------
- There is one required user-provided procedure, the one computing the log-likelihood function and optionally the first and/or second derivatives, and four other optional procedures, one each for computing the equality constraints, the inequality constraints, the Jacobian of the equality constraints, and the Jacobian of the inequality constraints.

- The main procedure, computing the log-likelihood and optionally the first and/or second derivatives, has an instance of type :class:`PV` struct containing the parameters, a second argument that is an instance of type :class:`struct DS` containing the data, and a third argument that is a vector of zeros and ones indicating which of the results, the function, first derivatives, or second derivatives, to be computed.

- The remaining optional procedures take just two arguments, the instance of the :class:`PV` structure containing the parameters and the instance of the :class:`DS` structure containing the data.

- The instance of the :class:`PV` structure is set up using the PV pack procedures, :func:`pvPack`, :func:`pvPackm`, :func:`pvPacks`, and :func:`pvPacksm`. These procedures allow for setting up a parameter vector in a variety of ways.

- The instance of the :class:`DS` structure containing the data is set up in two distinct ways depending on whether :func:`cmlmt` is to read the data in from a GAUSS data set.

- For example, the following procedure computes the log-likelihood and the first derivatives for a tobit model:

::

     proc lpr(struct PV p, x, y, ind);
        local s2,b0,b,yh,u,res,g1,g2;

        struct modelResults mm;

        b0 = pvUnpack(p,"b0");
        b = pvUnpack(p,"b");
        s2 = pvUnpack(p,"variance");

        yh = b0 + x * b;
        res = y - yh;
        u = y[.,1] ./= 0;

        if ind[1];
            mm.function = u.*lnpdfmvn(res,s2) + (1-u).*(ln(cdfnc(yh/sqrt(s2))));
        endif;

        if ind[2];
            yh = yh/sqrt(s2);
            g1 = ((res~x.*res)/s2)~((res.*res/s2)-1)/(2*s2);
            g2 = ( -( ones(rows(x),1)~x )/sqrt(s2) )~(yh/(2*s2));
            g2 = (pdfn(yh)./cdfnc(yh)).*g2;
            mm.gradient = u.*g1 + (1-u).*g2;
        endif;
        retp(mm);

     endp;

- The procedures for nonlinear equality and inequality constraints take two input arguments, an instance of a :class:`PV` parameters structure and an instance of a :class:`DS` data structure. For example, to constrain the sum of squares of the regression coefficients to be greater than one, provide the following procedure:

::

     proc ineqConst(struct PV par1, x, y);
          local b;
          b = pvUnpack(p,"b");
          retp(sumc(b^2) - 1);
     endp;


