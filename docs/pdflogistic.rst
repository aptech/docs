
pdflogistic
==============================================

Purpose
----------------

Computes the probability density function for the logistic distribution.

Format
----------------
.. function:: p = pdflogistic(x, a, b)

    :param x: data
    :type x: NxK matrix or an Nx1 vector or scalar

    :param a: Location parameter, ExE conformable with *x*.
    :type a: NxK matrix, Nx1 vector or scalar

    :param b: Scale parameter, ExE conformable with *x*. *b* must be greater than 0.
    :type b: NxK matrix, Nx1 vector or scalar

    :return p: the probability density function for the logistic distribution at the elements in *x*.
    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

The probability density function for the logistic distribution is
defined as

.. math::

   f(x) = \frac{exp⁡(z)}{b(1 + exp⁡(z))^2}\\
   z = -⁡ \bigg(\frac{x-a}{b}\bigg)

Examples
----------------

::

    // Data points
    x = { -2, 0, 1, 2 };

    // Logistic PDF with location = 0, scale = 1
    p = pdflogistic(x, 0, 1);
    print p;

After the code above, *p* is equal to:

::

       0.10499359
       0.25000000
       0.19661193
       0.10499359

.. seealso:: Functions :func:`cdflogistic`
