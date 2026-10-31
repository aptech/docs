expm1
================================================

Purpose
----------------

Computes the exponential of each element of *x*, minus one.
Use it to retain small changes when *x* is close to zero.

.. versionadded:: 27.0

Format
----------------
.. function:: y = expm1(x)

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

    event_probability = -expm1(x=log_survival);

Remarks
----------------

All real inputs are accepted. Negative infinity returns -1 and positive
infinity returns positive infinity. Finite inputs whose result overflows
return positive infinity.

Missing values and NaNs propagate element by element. Signed zero and
representable subnormal results are preserved. An empty input stays empty.
There is no clipping or omission of missing elements.

Complex storage is accepted only when every imaginary element is exactly
zero. Any nonzero imaginary element generates an error, regardless of the
complex-number setting or imaginary tolerance. Strings, structs, sparse
matrices and dataframes are not accepted.

.. seealso:: Functions :func:`ln`, :func:`exp`, :func:`ln1p`, :func:`lnsumexp`, :func:`lndiffexp`
