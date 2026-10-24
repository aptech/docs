
pdfBinomial
==============================================

Purpose
----------------

Computes the binomial probability density function.

Format
----------------
.. function:: p = pdfBinomial(x, trials, prob)

    :param x: The number of successes. An *x* within 1e-9 (relative) of a whole number is treated as that whole number. Any other non-whole *x* returns 0, as does an *x* below 0 or above *trials*.
    :type x: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *x*. The number of trials, :math:`trials \geq 0`.
    :type trials: NxK matrix, Nx1 vector or scalar

    :param prob: The probability of success on any given trial. ExE conformable with *x*. :math:`0 \leq prob \leq 1`.
    :type prob: NxK matrix, Nx1 vector or scalar

    :return p: The probability of *x* successes.
    :rtype p: NxK matrix, Nx1 vector or scalar

Examples
----------------
A polling company randomly selects 1,024 prospective voters in a region where 55% support
their candidate. What is the probability that exactly 600 of those selected support their candidate?

::

    p = pdfBinomial(600, 1024, 0.55);

After running the code above, *p* is equal to:

::

    0.0017226334

Continuing with the example above, what would be the probability of selecting the same number
of voters that support their candidate if their candidate's support in the region was 50% or 60%?

::

    p_support = { 0.5, 0.6 };
    p = pdfBinomial(600, 1024, p_support);

After running the code above, *p* is equal to:

::

    6.3351627e-09
      0.016621105

Remarks
-------
The probability mass function for the binomial distribution is
defined as:

:math:`P\left( x = k \middle| n,p \right) =`
:math:`\begin{pmatrix}
n \\
k \\
\end{pmatrix}p^{k}\left( 1 - p \right)^{n - k}`

where *k* is the number of successes (*x*), *n* is the number of trials (*trials*) and *p* is
the probability of success on each trial (*prob*).

If *trials* is below 0 or infinite, or *prob* is outside [0, 1], :func:`pdfBinomial`
returns a scalar error code and :func:`scalerr` returns the position of that
argument: 2 for *trials*, 3 for *prob*. An *x* that cannot occur is not an
error: it returns 0. A missing value in any argument returns a missing value.

.. seealso:: Functions :func:`cdfBinomial`, :func:`cdfBinomialInv`
