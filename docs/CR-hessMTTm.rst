
hessMTTm
==============================================

Purpose
----------------

Computes numerical Hessian with mask using available threads.

Format
----------------
.. function:: hessMTTm(&fct, par1, data1, mask)

    :param fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type fct: scalar

    :param par1: 
    :type par1: structure of type PV containing parameter vector at which Hessian is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by  fct

    :param mask: elements in  h corresponding to elements of mask set to zero are not computed otherwise are computed
    :type mask: KxK matrix

    :returns: h (*KxK matrix*), Hessian

Remarks
-------

par1 must be created using the pvPack procedures. Only lower left part
of mask looked at.


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
    
    mask = { 1 1
             1 0 };
    
    proc fct(struct PV p0, struct DS d0);
       local p,y;
       p = pvUnpack(p0, "P");
       y = p[1] * exp( -p[2] * d0.dataMatrix);
      retp(y);
    endp;
    
    h = hessMTTm(&fct,p1,d0,mask);

Source
++++++

hessmtt.src

gradient Hessian derivative mask thread
