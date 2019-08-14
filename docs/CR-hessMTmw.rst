
hessMTmw
==============================================

Purpose
----------------

Computes numerical Hessian with mask and weights.

Format
----------------
.. function:: h = hessMTmw(&fct, par1, data1, mask, wgts)

    :param &fct: pointer to procedure returning Nx1 vector.
    :type &fct: scalar

    :param par1: an instance of structure of type :class:`PV` containing parameter vector at which Hessian is to be evaluated
    :type par1: struct

    :param data1: structure of type :class:`DS` containing any data needed by *fct*
    :type data1: struct

    :param mask: elements in *h* corresponding to elements of *mask* set to zero are not computed, otherwise are computed.
    :type mask: KxK matrix

    :param wgts: weights
    :type wgts: Nx1 vector

    :returns: **h** (*KxK matrix*) - Hessian.

Remarks
-------

*fct* must evaluate to an Nx1 vector conformable to the weight vector.

*par1* must be created using the :func:`pvPack` procedures.


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
  wgts = zeros(5,1) | ones(10,1);

  // Mask
  mask = { 1 1,
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
  h = hessMTmw(&fct, p1, x, mask, wgts);

Source
------

hessmt.src
