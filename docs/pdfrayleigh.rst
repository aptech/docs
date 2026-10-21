
pdfRayleigh
==============================================

Purpose
----------------

Computes the probability density function of the Rayleigh distribution.

Format
----------------
.. function:: p = pdfRayleigh(x, scale)

    :param x: *x* must be greater than 0.
    :type x: NxK matrix or an Nx1 vector or scalar

    :param scale: Scale parameter, ExE conformable with *x*. *scale* must be greater than 0.
    :type scale: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function of the Rayleigh distribution evaluated at *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function of the Rayleigh distribution is defined
as

.. math::

   f(x) = \frac{x}{scale^2}exp⁡(\frac{−x^2}{2 \cdot scale^2})

Examples
----------------

::

    // Data points
    x = { 0.5, 1, 2, 3 };

    // Rayleigh PDF with scale = 1
    p = pdfRayleigh(x, 1);
    print p;

After the code above, *p* is equal to:

::

       0.44124845
       0.60653066
       0.27067057
      0.033326990

.. seealso:: Functions :func:`cdfRayleighinv`
