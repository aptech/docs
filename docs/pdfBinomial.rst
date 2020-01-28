
pdfBinomial
==============================================

Purpose
----------------

Computes the binomial probability density function.

Format
----------------
.. function:: p = pdfBinomial(successes, trials, prob)

    :param successes: must be a positive number and < *trials*
    :type successes: NxK matrix, Nx1 vector or scalar

    :param trials: ExE conformable with *successes*. *trials* must be > *successes*.
    :type trials: NxK matrix, Nx1 vector or scalar

    :param prob: The probability of success on any given trial. ExE conformable with *successes*. :math:`0 < prob < 1`.
    :type prob: NxK matrix, Nx1 vector or scalar

    :return p: The probability of the specified number of *successes*.
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
The probability density function for the binomial distribution is
defined as:

:math:`P\left( x = k \middle| n,p \right) =`
:math:`\begin{pmatrix}
n \\
k \\
\end{pmatrix}p^{k}\left( 1 - p \right)^{n - k}`

where *k* is the number of successes, *n* is the number of trials and *p* is
the probability of success on each trial.

For invalid inputs, :func:`pdfBinomial` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

.. seealso:: Functions :func:`cdfBinomial`, :func:`cdfBinomialInv`
