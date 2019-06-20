
pdflogistic
==============================================

Purpose
----------------

Computes the probability density function for the logistic distribution.

Format
----------------
.. function:: pdflogistic(x, a, b)

    :param x: data
    :type x: NxK matrix or an Nx1 vector or scalar

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix, Nx1 vector or scalar

    :returns: y (*NxK matrix, Nx1 vector or scalar*)



Remarks
-------

The probability density function for the logistic distribution is
defined as

.. DANGER:: fix equation

.. math::

   f(x)=exp⁡(z)b(1+exp⁡(z))2
   z=-⁡x-ab

.. seealso:: Functions :func:`cdflogistic`

