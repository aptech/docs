
hessMTgw
==============================================

Purpose
----------------

Computes numerical Hessian using gradient procedure with weights.

Format
----------------
.. function:: h = hessMTgw(&gfct, par1, data1, wgts)

    :param &gfct: pointer to procedure computing either NxK Jacobian.
    :type &gfct: scalar

    :param par1: an instance of structure of type :class:`PV` containing parameter vector at which Hessian is to be evaluated
    :type par1: struct

    :param data1: structure of type :class:`DS` containing any data needed by *gfct*
    :type data1: struct

    :param wgts: weights
    :type wgts: Nx1 vector

    :return h: Hessian.

    :rtype h: KxK matrix

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

    // Define weights
    wgts = zeros(5, 1) | ones(10, 1);

    // Function to compute Hessian
    proc gfct(struct PV p0, x);
       local p, g1, g2;

       // Unpack parameters
       p = pvUnpack(p0, "P");

       // Define gradients
       g1 = exp(-p[2] * x);
       g2 = -p[1] * x .* g1;

       retp(g1~g2);
    endp;

    // Find Hessian
    h = hessMTgw(&gfct, p1, x, wgts);

Remarks
-------

*par1* must be created using the :func:`pvPack` procedures.


Source
------

hessmt.src
