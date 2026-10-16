lndiffexp(a, b)
================================================

Purpose
----------------

Computes :math:`\ln(e^a - e^b)` for :math:`a \ge b`, element by element. Use it
to subtract quantities that are stored as logarithms, such as the probability
of an interval from two log cumulative probabilities, without overflow,
underflow or loss of a small difference.

.. versionadded:: 27.0

Format
----------------
.. function:: y = lndiffexp(a, b)

    :param a: Real values, the logarithm of the larger quantity.
    :type a: scalar, NxK matrix or N-dimensional array

    :param b: Real values, the logarithm of the smaller quantity, :math:`b \le a`.
    :type b: scalar, NxK matrix or N-dimensional array

    :return y: Elementwise results, with the shape of the non-scalar input.
    :rtype y: scalar, NxK matrix or N-dimensional array

Examples
----------------

Subtract large exponentials
++++++++++++++++++++++++++++++++++

::

    print lndiffexp(1000, 999);

::

         999.54132

``ln(exp(1000) - exp(999))`` returns a missing value, because both
exponentials overflow to infinity.

Keep a small difference
++++++++++++++++++++++++++++++++++

::

    print lndiffexp(1, 0.9999999999999999);
    print lndiffexp(0, -40);

The results are approximately -35.7368 and -4.248e-18. The direct formula
returns negative infinity for the first, because the two exponentials round to
the same value, and 0 for the second, because 1 minus :math:`e^{-40}` rounds
to 1.

Interval probability from log probabilities
++++++++++++++++++++++++++++++++++++++++++++

::

    // log P(1 < Z <= 2) for a standard normal Z
    log_p = lndiffexp(lncdfn(2), lncdfn(1));
    print exp(log_p);

::

        0.13590512

Remarks
----------------

With :math:`t = b - a`, the result is computed as :math:`a + \ln(-\mathrm{expm1}(t))`
for :math:`t \ge -\ln 2` and :math:`a + \mathrm{ln1p}(-e^t)` otherwise, so both
a small difference and a small correction are kept. The inputs must already be
accurate: when *a* and *b* round to the same value, the result is negative
infinity, and no hidden precision can be recovered.

*a* must be greater than or equal to *b*. Equal inputs, including two negative
infinities, return negative infinity. If *b* is negative infinity, the result
is *a*. If *a* is positive infinity and *b* is not, the result is positive
infinity. *a* < *b*, or both positive infinity, generates an
argument-out-of-range error.

Missing values and NaNs propagate element by element and are checked before
the order of *a* and *b*. An empty input with an empty or scalar input returns
an empty result.

*a* and *b* must have the same dimensions, or one of them must be a scalar.
There is no row or column expansion. Complex storage is accepted only when
every imaginary element is exactly zero. Strings, structs, sparse matrices and
dataframes are not accepted.

.. seealso:: Functions :func:`lnsumexp`, :func:`ln1p`, :func:`expm1`, :func:`lncdfn`, :func:`ln`
