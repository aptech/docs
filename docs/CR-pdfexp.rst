
pdfexp
==============================================

Purpose
----------------

Computes the probability density function for the exponential distribution.

Format
----------------
.. function:: p = pdfexp(x, a, b)

    :param x: *x* must be greater than *a*.
    :type x: NxK matrix, Nx1 vector or scalar

    :param a: Location parameter. ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param b: the scale parameter. sometimes called *beta*. *b* must be greater than 0.
    :type b: scalar

    :return p: the probability density function for the exponential distribution for the elements in *x*.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

:func:`pdfExp` calculates the probability density function for the two-parameter
exponential distribution, which is defined as

.. DANGER:: Fix equations

.. math::

   f(x)=1bexp⁡(−x−ab)

.. seealso:: Functions :func:`cdfexp`
