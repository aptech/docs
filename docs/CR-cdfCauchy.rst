
cdfCauchy
==============================================

Purpose
----------------

Computes the cumulative distribution function for the Cauchy distribution.

Format
----------------
.. function:: cdfCauchy(x, a, b)

    :param x: 
    :type x: NxK matrix, Nx1 vector or scalar.

    :param a: Location parameter. ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param b: Scale parameter. ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix, Nx1 vector or scalar

    :returns: y (*NxK matrix, Nx1 vector or scalar*)

Remarks
-------

The cumulative distribution function for the Cauchy distribution is
defined as:

.. math:: \frac{1}{2} + \frac{1}{\pi} arctan(\frac{x−a}{b})

.. DANGER:: Fix equation


.. seealso:: :func:`pdfCauchy`

