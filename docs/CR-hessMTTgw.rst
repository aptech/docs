
hessMTTgw
==============================================

Purpose
----------------

Computes numerical Hessian using gradient procedure with weights and using available threads.

Format
----------------
.. function:: hessMTTgw(&gfct, par1, data1, wgts)

    :param gfct: pointer to procedure computing either 1xK gradient or NxK Jacobian
    :type gfct: scalar

    :param par1: 
    :type par1: structure of type PV containing parameter vector at which Hessian is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by fct

    :param wgts: weights
    :type wgts: Nx1 vector

    :returns: h (*KxK matrix*), Hessian

Remarks
-------

par1 must be created using the pvPack procedures.


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
    wgts = zeros(5,1) | ones(10,1);
    
    proc gfct(&fct, struct PV p0, struct DS d0);
       local p,y,g1,g2;
       p = pvUnpack(p0, "P");
       g1 = exp(-p[2] * d0.dataMatrix);
       y = p[1] * exp( -p[2] * d0.dataMatrix);
       g2 = -p[1] * d0.dataMatrix .* g1;
       retp(g1~g2);
    endp;
    
    h = hessMTTg(&gfct,p1,d0,wgts);

Source
++++++

hessmtt.src

gradient Hessian derivative thread weight
