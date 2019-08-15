
hessMTTm
==============================================

Purpose
----------------

Computes numerical Hessian with mask using available threads.

Format
----------------
.. function:: h = hessMTTm(&fct, par1, data1, mask)

    :param fct: pointer to procedure returning either Nx1 vector or 1x1 scalar.
    :type fct: scalar

    :param par1: structure of type :class:`PV` containing parameter vector at which Hessian is to be evaluated
    :type par1: struct

    :param data1: structure of type :class:`DS` containing any data needed by *fct*
    :type data1: struct

    :param mask: elements in *h* corresponding to elements of *mask* set to zero are not computed otherwise are computed
    :type mask: KxK matrix

    :return h: Hessian

    :rtype h: KxK matrix

Remarks
-------

*par1* must be created using the :func:`pvPack` procedures. Only lower left part of *mask* looked at.


Examples
----------------

::

    // Define a PV structure
    struct PV p1;

    // Create p1 PV structure
    p1 = pvCreate;

    // Fill PV structure
    p1 = pvPack(p1, 0.1|0.2, "P");

    // Create data matrix
    x = seqa(1, 1, 15);

    // Mask
    mask = { 1 1
             1 0 };

    // Function to compute Hessian
    proc fct(struct PV p0, x);
       local p, y;

       // Unpack parameters
       p = pvUnpack(p0, "P");

       // Define Hessian
       y = p[1] * exp( -p[2] * x);

      retp(y);
    endp;

    // Find Hessian
    h = hessMTTm(&fct, p1, x, mask);

Source
------

hessmtt.src
