lnsumexp(x, dim)
================================================

Purpose
----------------

Computes the natural logarithm of the sum of the exponentials of the elements
of *x*, down each column, across each row, or over all elements. Use it to add
quantities that are stored as logarithms, such as log likelihoods or log
probabilities, without overflow, underflow or loss of small terms.

.. versionadded:: 27.0

Format
----------------
.. function:: y = lnsumexp(x)
              y = lnsumexp(x, dim)

    :param x: Real values.
    :type x: scalar or NxK matrix

    :param dim: Optional, the direction of the sum. Default = 1.

        .. csv-table::
            :widths: auto

            "1", "Sum down each column; *y* is Kx1."
            "2", "Sum across each row; *y* is Nx1."
            "0", "Sum over all elements; *y* is a scalar."

    :type dim: scalar

    :return y: :math:`\ln \sum \exp(x)` for each column, each row, or all elements.
    :rtype y: Kx1 vector, Nx1 vector or scalar

Examples
----------------

Sum each row of log contributions
++++++++++++++++++++++++++++++++++

::

    log_terms = { 1000 1001, -1000 -1001 };
    print lnsumexp(log_terms, dim=2);

::

         1001.3133
        -999.68674

Computing ``ln(sumc(exp(log_terms')))`` directly returns positive infinity for
the first row, because :math:`e^{1000}` overflows, and negative infinity for the
second, because :math:`e^{-1000}` underflows to zero.

Keep a small term
++++++++++++++++++++++++++++++++++

::

    x = 0 | -40;
    print lnsumexp(x);

The result is approximately 4.248e-18. ``ln(exp(0) + exp(-40))`` returns 0,
because 1 plus :math:`e^{-40}` rounds to 1 before the logarithm is taken.

Remarks
----------------

The sum is computed as :math:`m + \ln(1 + \sum_{i \ne k} e^{x_i - m})`, where
:math:`m = x_k` is the largest element, with compensated summation (Blanchard,
Higham and Higham, 2021).

As with :func:`sumc`, the default *dim* = 1 sums each column, so a 1xK row
vector returns its K elements as a Kx1 vector. Use *dim* = 2 or *dim* = 0 to
reduce a row vector to one value. A scalar *x* returns itself.

Negative infinity contributes nothing to a sum, and a sum of only negative
infinities is negative infinity. Any positive infinity gives positive infinity.
A missing value or NaN makes the result for its column, row or total missing,
and takes precedence over positive infinity; other columns or rows are not
affected. There is no omission of missing elements.

An empty *x* with *dim* = 0 returns negative infinity, the logarithm of an
empty sum. An empty *x* with *dim* = 1 or 2 generates an error.

*dim* must be 0, 1 or 2. N-dimensional arrays are not supported. Complex
storage is accepted only when every imaginary element is exactly zero. Strings,
structs, sparse matrices and dataframes are not accepted.

References
----------------

#. Blanchard, P., Higham, D. J. and Higham, N. J. (2021). Accurately computing
   the log-sum-exp and softmax functions. *IMA Journal of Numerical Analysis*,
   41(4), 2311–2330.

.. seealso:: Functions :func:`lndiffexp`, :func:`ln1p`, :func:`expm1`, :func:`sumc`, :func:`ln`
