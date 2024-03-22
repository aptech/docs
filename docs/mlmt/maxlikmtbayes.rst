maxlikmtbayes
==============================================

Purpose
----------------

Bayesian confidence limits using weighted maximum likelihood bootstrap.

Format
----------------
.. function:: out = maxlikmtbayes(&modelProc, par, ..., c1)

    :param &modelProc: Pointer to a procedure that computes the function to be minimized.
    :type &modelProc: pointer

    :param par: An instance of a PV structure, constructed using the "pack" functions.
    :type par: PV structure instance

    :param ...: Optional arguments that will be passed to the user-provided log-likelihood function. Can include any GAUSS data type or a DS structure for dataset handling.
    :type ...: Various

    :param c1: Optional input. Instance of a :class:`maxlikmtControl` structure containing the following members:

        .. include:: include/mlmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`maxlikmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures.

        .. include:: include/mlmtresultsstruct.rst

    :rtype out: struct

Example
-------

The following example demonstrates the computation of Bayesian confidence limits for a tobit model using a weighted maximum likelihood bootstrap:

::

    // Load maxlikmt library
    library maxlikmt;
    
    // Likelihood function 
    proc lpr(struct PV p, y, x, ind);
       local s2, b0, b, yh, u, res, g1, g2;
    
       // Declare 'mm' to be a modelResults struct
        // to hold the function and gradient values
        struct modelResults mm;
    
        // Extract parameters from PV struct
        b0 = pvUnpack(p, "b0");
        b = pvUnpack(p, "b");
        s2 = pvUnpack(p, "variance");
    
        // Computations shared between function and gradient
        yh = b0 + x * b;
        res = y - yh;
        u = y[.,1] ./= 0;
    
        // Compute function value
        if ind[1];
            mm.function = u.*lnpdfmvn(res, s2) + (1-u).*(ln(cdfnc(yh/sqrt(s2))));
        endif;
    
        // Compute gradient if second element
        // of 'ind' is nonzero
        if ind[2];
            yh = yh/sqrt(s2);
            g1 = ((res~x.*res)/s2)~((res.*res/s2)-1)/(2*s2);
            g2 = (-(ones(rows(x), 1)~x)/sqrt(s2))~(yh/(2*s2));
            g2 = (pdfn(yh)./cdfnc(yh)).*g2;
            mm.gradient = u.*g1 + (1-u).*g2;
        endif;
    
    endp;
    
    // Create initial PV structure
    // and pack starting parameter values 
    struct PV p0;
    p0 = pvPack(pvCreate, 19.143, "b0");
    p0 = pvPack(p0, .5311, "b");
    
    // Declare maxlikmtControl structure 
    struct maxlikmtControl c0;
    c0 = maxlikmtControlCreate;
    
    // Set parameter bounds
    c0.Bounds = { -10 10, -10 10, -10 10, -10 10, .1 10 };
    
    // Load tobit data
    z = loadd("maxlikmttobit");
    
    // Separate x and y 
    y = z[., 1];
    x = z[., 2:4];
    
    // Declare instance of maxlikmtResults structure
    struct maxlikmtResults out;
    out = maxlikmtbayes(&lnlk, p0, y, x, c0);
    
    // Print results
    print out.bayesLimits;
