cmlmtProfile
==============================================

Purpose
-------
Computes profile likelihood traces and profile t traces for models estimated using maximum likelihood.

Format
------
.. function:: out = cmlmtProfile(&logl, par [, ..., c1])
          
    :param &logl: Pointer to a procedure that returns the log-likelihood for one observation or a vector of log-likelihoods for a matrix of observations.
    :type &logl: pointer

    :param par: Instance of a PV structure, constructed using the "pack" functions.
    :type par: struct

    :param ...: Optional arguments to be passed to the user-provided log-likelihood function. Can be any GAUSS data type, including DS structures for dataset handling.
    :type ...: Various

    :param c1: Optional input. Instance of a :class:`cmlmtControl` structure containing the following members:

        .. include:: include/cmlmtcontrolstruct.rst

    :type c1: struct

    :return out: An instance of a :class:`cmlmtResults` structure. Contains the results of the optimization problem, including parameter estimates, function evaluations, and various statistical measures.

        .. include:: include/cmlmtresultsstruct.rst

    :rtype out: struct

Example
-------
Biochemical Oxygen Demand (BOD) Analysis
++++++++++++++++++++++++++++++++++++++++

This example demonstrates the application of :func:`cmlmtProfile` to model the Biochemical Oxygen Demand (BOD) data using a log-likelihood function.

::

    library cmlmt;
    
    // Define the log-likelihood function
    proc lnlk(struct PV p, struct DS d, ind);
        local dev, s2, m, r, b0, b;
        
        struct modelResults mm;
        
        // Unpack parameters
        b0 = pvUnpack(p, 1);
        b = pvUnpack(p, 2);
        
        // Calculate model predictions
        r = exp(-b * d[2].dataMatrix);
        m = 1 - r;
        
        // Calculate deviations
        dev = d[1].dataMatrix - b0 * m;
        s2 = dev'dev/rows(dev);
        
        // Calculate log-likelihood
        if ind[1];
            mm.function = lnpdfmvn(dev, s2);
        endif;
        
        // Calculate gradient, if requested
        if ind[2];
            mm.gradient = (dev / s2) .* (m ~ b0 * d[2].dataMatrix .* r);
        endif;
        
        retp(mm);
    endp;
    
    // Data setup
    struct DS d0;
    d0 = reshape(dsCreate, 2, 1);
    d0[1].dataMatrix = {8.3, 10.3, 19.0, 16.0, 15.6, 19.8};
    d0[2].dataMatrix = {1, 2, 3, 4, 5, 7};
    
    // Parameter setup
    struct PV p0;
    p0 = pvPacki(pvCreate, 19.143, "b0", 1);
    p0 = pvPacki(p0, .5311, "b", 2);
    
    // Control structure setup
    struct cmlmtControl c0;
    c0 = cmlmtControlCreate;
    c0.Bounds = {10 35, 0 2};  // Set parameter bounds
    
    // Perform the profile likelihood analysis
    struct cmlmtResults out;
    out = cmlmtProfile(&lnlk, p0, d0, c0);


Remarks
-------
- :func:`cmlmtProfile` is utilized to explore the parameter space of maximum likelihood estimates more thoroughly, offering insights into the confidence intervals and sensitivity of the estimates.
- This function is especially useful in complex models where the standard error may not provide a complete picture of parameter uncertainty.
- The control structure allows extensive customization of the profiling process, making it adaptable to a wide range of models and research questions.
