
stdc
==============================================

Purpose
----------------
Computes the sample standard deviation of the elements in each column of a matrix.

Format
----------------
.. function:: y = stdc(x)

    :param x: data
    :type x: NxK matrix

    :return y: the standard deviation of each column of *x*.

    :rtype y: Kx1 vector


Examples
----------------

::

    // Set the rng seed so that the random numbers produced will
    // be repeatable
    rndseed 94243524;

    // Create a vector of random normal numbers
    y = rndn(8100, 1);

    // Compute the standard deviation of the column vector 'y'
    std = stdc(y);

The standard deviation, in variable *std*, is equal to:

::

    1.00183907

Remarks
-------

This function essentially computes sample standard deviation, *s*:

.. math::

   s = \frac{1}{n−1}⁢×\sum_{i=1}^n(X_i−\bar{X})^2

Thus, the divisor is :math:`N-1` rather than :math:`N`, where :math:`N` is the number of
elements being summed.

To convert to the population's standard deviation, multiply by
:math:`\sqrt{\frac{n - 1}{n}}`:

.. math::

   \sigma = s*\frac{n−1}{n}

.. seealso:: Functions :func:`meanc`
