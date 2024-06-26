maxlikmtProfileLimits
==============================================

Purpose
-------

Computes confidence limits by inversion of the likelihood ratio statistic.

Format
------

.. function:: out1 = maxlikmtProfileLimits(&logl, out0 [, ...., c1])

    :param &logl: Pointer to log-likelihood function used to generate results of an estimation by a call to :func:`maxlikmt`.
    :type &logl: pointer

    :param out0: Instance of :class:`maxlikmtResults` structure containing results of an estimation generated by a call to :func:`maxlikmt`.
    :type out0: struct

    :param ...: Optional input arguments. They can be any set of structures, matrices, arrays, strings, required to compute the log-likelihood function.
    :type ...: Various

    :param c1: The set of optional input arguments must contain the instance of the :class:`maxlikmtResults` structure used in the call to 
    :func:`maxlikmt` that produced the results in *out0*.

            .. include:: include/mlmtcontrolstruct.rst

    :type c1: struct

    :return out1: Instance of :class:`maxlikmtResults` structure that is a duplicate of *out0* except that the member, *out1.profileLimits*, has been set to the confidence limits by inversion of the likelihood ratio statistic.

    :rtype out1: struct

Example
-------

::

    library maxlikmt;
    
    // Define the log-likelihood function
    proc lpr(struct PV p, y, x, ind);
        local s2, b0, b, yh, u, res, g1, g2;
        
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
            g2 = (-(ones(rows(x),1)~x)/sqrt(s2))~(yh/(2*s2));
            g2 = (pdfn(yh)./cdfnc(yh)).*g2;
            mm.gradient = u.*g1 + (1-u).*g2;
        endif;
        
        retp(mm);
    endp;
    
    struct PV p0;
    p0 = pvPack(pvCreate, 1, "b0");
    p0 = pvPack(p0, 1|1|1, "b");
    p0 = pvPack(p0, 1, "variance");
    
    struct maxlikmtControl c0;
    c0 = maxlikmtcontrolcreate;
    c0.title = "Tobit Example";
    c0.Bounds = {-10 10, -10 10, -10 10, -10 10, .1 10};
    
    z = loadd(getGAUSSHome("pkgs/maxlikmt/examples/maxlikmttobit.dat"));
    y = z[., 1];
    x = z[., 2:4];
    
    struct maxlikmtResults out1;
    out1 = maxlikmt(&lpr, p0, y, x, c0);
    
    // Compute limits by inversion of likelihood ratio statistic
    out1 = maxlikmtProfileLimits(&lpr, out1, y, x, c0);
    
    // Print the results
    call maxlikmtPrt(out1);

