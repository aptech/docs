
hessMTT
==============================================

Purpose
----------------

Computes numerical Hessian using available threads.

Format
----------------
.. function:: hessMTT(&fct,par1,data1)

    :param fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type fct: scalar

    :param par1: 
    :type par1: structure of type PV containing parameter vector at which Hessian is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by  fct

    :returns: h (*KxK matrix*), Hessian

Examples
----------------

::

    #include optim.sdf
    struct PV p1;
    p1 = pvCreate;
    
    p1 = pvPack(p1,0.1|0.2, "P");
    struct DS d0;
    d0 = dsCreate;
    
    d0.dataMatrix = seqa(1,1,15);
    
    proc fct(struct PV p0, struct DS d0);
       local p,y;
       p = pvUnpack(p0, "P");
       y = p[1] * exp( -p[2] * d0.dataMatrix);
       retp(y);
    endp;
    
    h = hessMTT(&fct,p1,d0);

Source
++++++

hessmtt.src

gradient Hessian derivative weight mask thread
