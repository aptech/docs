
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

.. math::

    f(x) = \frac{1}{b} exp \big( − \frac{x−a}{b} \big)

Examples
----------------

::

    // Data points
    x = { 0.5, 1, 2, 5 };

    // Exponential PDF with location = 0, scale = 1
    p = pdfexp(x, 0, 1);
    print p;

After the code above, *p* is equal to:

::

       0.60653066
       0.36787944
       0.13533528
     0.0067379470

.. seealso:: Functions :func:`cdfexp`
