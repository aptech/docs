
stdc
==============================================

Purpose
----------------
Computes the standard deviation of the elements in each column of a matrix.

Format
----------------
.. function:: y = stdc(x[, divisor="sample"])

    :param x: data
    :type x: NxK matrix

    :param divisor: Optional string, ``"sample"`` (the default) divides by N-1;
        ``"population"`` divides by N. Other values are errors.
    :type divisor: string

    :return y: the standard deviation of each column of *x*.

    :rtype y: Kx1 vector


Examples
----------------

Keyword arguments
+++++++++++++++++

Arguments can be named to make their meaning clear::

    y = stdc({1,2,3,4}, divisor="population");

Omitting ``divisor`` keeps the sample standard deviation.
Positional arguments must come before named arguments. An argument cannot
be supplied twice, and unknown keyword names are errors.


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

By default, this function computes sample standard deviation, *s*:

.. math::

   s = \frac{1}{n−1}⁢×\sum_{i=1}^n(X_i−\bar{X})^2

Thus, the divisor is :math:`N-1` rather than :math:`N`, where :math:`N` is the number of
elements being summed.

To convert to the population's standard deviation, multiply by
:math:`\sqrt{\frac{n - 1}{n}}`:

.. math::

   \sigma = s \cdot \sqrt{\frac{n-1}{n}}

.. seealso:: Functions :func:`meanc`
