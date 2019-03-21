
hessMTg
==============================================

Purpose
----------------

Computes numerical Hessian using gradient procedure.

Format
----------------
.. function:: hessMTg(&gfct, par1, data1)

    :param &gfct: pointer to procedure computing either 1xK gradient or NxK Jacobian.
    :type &gfct: scalar

    :param par1: 
    :type par1: an instance of structure of type PV containing parameter vector at
        which Hessian is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by  gfct

    :returns: h (*KxK matrix*), Hessian.

Examples
----------------

::

    #include optim.sdf
    struct PV p1;
    struct DS d0;
    p1 = pvCreate;
    p1 = pvPack(p1,0.1|0.2, "P");
    d0 = dsCreate;
    d0.dataMatrix = seqa(1,1,15);
     
    proc gfct(&fct, struct PV p0, struct DS d0);
       local p,y,g1,g2;
     
       p = pvUnpack(p0, "P");
       g1 = exp(-p[2] * d0.dataMatrix);
       y = p[1] * exp( -p[2] * d0.dataMatrix);
       g2 = -p[1] * d0.dataMatrix .* g1;
      retp(g1~g2);
    endp;
     
    h = hessMTg(&gfct,p1,d0);

Source
++++++

hessmt.src

gradient Hessian derivative
