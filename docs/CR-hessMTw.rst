
hessMTw
==============================================

Purpose
----------------

Computes numerical Hessian with weights.

Format
----------------
.. function:: hessMTw(&fct, par1, data1, wgts)

    :param &fct: pointer to procedure returning Nx1 vector.
    :type &fct: scalar

    :param par1: 
    :type par1: an instance of structure of type PV containing parameter vector at which Hessian is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by  fct

    :param wgts: weights.
    :type wgts: Nx1 vector

    :returns: h (*KxK matrix*), Hessian.

Examples
----------------

::

    #includeoptim.sdf
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1,0.1|0.2, "P");
    
    struct DS d0;
    d0 = dsCreate;
    d0.dataMatrix = seqa(1,1,15);
    wgt = zeros(5,1) | ones(10,1);
     
    proc fct(&fct, struct PV p0, struct DS d0, wgt);
       local p,y;
     
       p = pvUnpack(p0, "P");
       y = p[1] * exp( -p[2] * d0.dataMatrix);
       retp(y);
    endp;
     
    h = hessMTw(&fct,p1,d0,wgt);

Source
++++++

hessmt.src

gradient Hessian derivative weight
