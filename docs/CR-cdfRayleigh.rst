
cdfRayleigh
==============================================

Purpose
----------------
Computes the Rayleigh cumulative distribution function.

Format
----------------
.. function:: cdfRayleigh(x, b)

    :param x: must be greater than or equal to 0.
    :type x: NxK matrix or an Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix or Nx1 vector or scalar

    :returns: y (*NxK matrix or Nx1 vector or scalar*)

Remarks
------------

The Rayleigh cumulative distribution function is defined as

.. math::

1 − exp⁡(\frac{-x^2}{2\sigma^2})

.. DANGER:: FIX EQUATION

Examples
----------------
Here is an example show the Rayleigh cumulative distribution plot with different scale parameters.

::

    x = seqa(0,0.1,100);
    b = 0.5~1~2~3~4;
    y = cdfRayleigh(x,b);
    plotxy(x,y);

After running above code,

.. figure:: _static/images/cdfRayleigh.png

.. seealso:: Functions :func:`cdfRayleighInv`, :func:`pdfRayleigh`
