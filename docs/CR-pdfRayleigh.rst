
pdfRayleigh
==============================================

Purpose
----------------

Computes the probability density function of the Rayleigh distribution.

Format
----------------
.. function:: p = pdfRayleigh(x, b)

    :param x: *x* must be greater than 0.
    :type x: NxK matrix or an Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function of the Rayleigh distribution evaluated at *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function of the Rayleigh distribution is defined
as

.. DANGER:: fix equation

.. math::

   fx=xb2exp⁡(−x22b2)

.. seealso:: Functions :func:`cdfRayleighinv`
