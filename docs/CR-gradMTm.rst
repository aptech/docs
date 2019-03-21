
gradMTm
==============================================

Purpose
----------------

Computes numerical gradient with mask.

Format
----------------
.. function:: gradMTm(&fct, par1, data1, mask)

    :param &fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type &fct: scalar

    :param par1: 
    :type par1: an instance of structure of type PV containing parameter vector at which gradient is to be evaluated

    :param data1: 
    :type data1: structure of type DS containing any data needed by  fct

    :param mask: elements in g corresponding
        to elements of  mask set to zero are not computed, otherwise they are computed.
    :type mask: Kx1 matrix

    :returns: g (*TODO*), NxK Jacobian or 1xK gradient.

Remarks
-------

par1 must be created using the pvPack procedures.


Examples
----------------

::

    #include optim.sdf
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1,0.1|0.2,"P");
     
    struct DS d0;
    d0 = dsCreate;
    d0.dataMatrix = seqa(1,1,15);
     
    proc fct(struct PV p0, struct DS d0);
       local p,y;
       p = pvUnpack(p0, "P");
       y = p[1] * exp(-p[2] * d0.dataMatrix);
       retp(y);
    endp;
     
     mask = { 0, 1 };
     g = gradMTm(&fct,p1,d0,mask);

Source
++++++

gradmt.src

gradient derivative mask
