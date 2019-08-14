
cdfRayleighInv
==============================================

Purpose
----------------

Computes the Rayleigh inverse cumulative distribution function.

Format
----------------
.. function:: x = cdfRayleighInv(p, shape)

    :param p: Probabilities at which to compute the Rayleigh inverse cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param shape: Shape parameter, ExE conformable with *p*. *shape* must be greater than 0.
    :type shape: NxK matrix, Nx1 vector or scalar

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - each value of *x* is the value such that the Rayleigh cumulative distribution function is equal to the corresponding value of *p*.

Remarks
-------

::

   cdfRayleighInv(cdfRayleigh(x, shape), shape) = x

Examples
----------------

::

  // Probabilities
  p = {0.1,0.25, 0.5,0.75,0.95};

  // Scale
  scale = 0.5;

  // Call Rayleigh function
  x = cdfRayleighInv(p, scale);

After running above code,

::

  x =
    0.2295
    0.3793
    0.5887
    0.8326
    1.2239
    
.. seealso:: :func:`pdfRayleigh`, :func:`cdfRayleigh`
