
gradMTT
==============================================

Purpose
----------------

Computes numerical gradient using available threads.

Format
----------------
.. function:: g = gradMTT(&fct,par1,data1)

    :param &fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type &fct: scalar

    :param par1: structure of type :class:`PV` containing parameter vector at which gradient is to be evaluated
    :type par1: struct

    :param data1: structure of type DS containing any data needed by *fct*
    :type data1: struct

    :return g: Jacobian or gradient.

    :rtype g: NxK or 1xK

Examples
----------------

::

    // Declare PV structure to store parameters
    struct PV p1;
    p1 = pvCreate;
    p1 = pvPack(p1, 0.1|0.2, "P");

    // Declare DS structure to store data
    struct DS d0;
    d0 = dsCreate;
    d0.dataMatrix = seqa(1, 1, 15);

    // Write function
    proc fct(struct PV p0, struct DS d0);

       local p,y;
       p = pvUnpack(p0, "P");
       y = p[1] * exp(-p[2] * d0.dataMatrix);

       retp(y);
    endp;

    g = gradMT(&fct, p1, d0);

Remarks
-------

*par1* must be created using the :func:`pvPack` procedures


Source
------

gradmtt.src
