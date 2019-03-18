
gradMTT
==============================================

Purpose
----------------

Computes numerical gradient using available threads.

Format
----------------
.. function:: gradMTT(&fct,par1,data1)

    :param fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type fct: scalar

    :param par1: structure of type PV containing parameter vector at which gradient is to be evaluated
    :type par1: TODO

    :param data1: structure of type DS containing any data needed by  fct
    :type data1: TODO

    :returns: g (*TODO*), NxK Jacobian or 1xK gradient

Examples
----------------

::

    #include optim.sdf
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1, 0.1|0.2, "P");
    
    struct DS d0;
    d0 = dsCreate;
    d0.dataMatrix = seqa(1,1,15);
    
    proc fct(struct PV p0, struct DS d0);
       local p,y;
       p = pvUnpack(p0, "P");
       y = p[1] * exp(-p[2] * d0.dataMatrix);
       retp(y);
    endp;
    
    g = gradMT(&fct,p1,d0);

Source
++++++

gradmtt.src

gradient derivative thread
