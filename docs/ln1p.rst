ln1p(x)
================================================

Purpose
----------------

Computes the natural logarithm of one plus each element of *x*.
Use it to retain small changes when *x* is close to zero.

.. versionadded:: 27.0

Format
----------------
.. function:: y = ln1p(x)

    :param x: Real values.
    :type x: scalar, NxK matrix or N-dimensional array

    :return y: Elementwise results, with the same shape as *x*.
    :rtype y: scalar, NxK matrix or N-dimensional array

Examples
----------------

::

    p = 1e-20;
    log_survival = ln1p(-p);
    event_probability = -expm1(log_survival);
    print log_survival event_probability;

The results are approximately -1e-20 and 1e-20. The keyword call is also
supported::

    log_survival = ln1p(x=-p);

Remarks
----------------

*x* must be greater than or equal to -1. At -1 the result is negative
infinity. Values below -1, including negative infinity, generate an
argument-out-of-range error. Positive infinity returns positive infinity.

Missing values and NaNs propagate element by element. Signed zero and
representable subnormal results are preserved. An empty input stays empty.
There is no clipping or omission of missing elements.

Complex storage is accepted only when every imaginary element is exactly
zero. Any nonzero imaginary element generates an error, regardless of the
complex-number setting or imaginary tolerance. Strings, structs, sparse
matrices and dataframes are not accepted.

.. seealso:: Functions :func:`ln`, :func:`exp`, :func:`expm1`, :func:`lnsumexp`, :func:`lndiffexp`
