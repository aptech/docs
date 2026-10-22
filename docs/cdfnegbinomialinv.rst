
cdfNegBinomialInv
==============================================

Purpose
----------------
Computes the quantile or inverse negative binomial cumulative distribution function.

Format
----------------
.. function:: f = cdfNegBinomialInv(p, s, prob)

    :param p: The probability of observing *f* failures before observing *s* successes. :math:`0 \leq p \leq 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param s: ExE conformable with *p*, the number of successes. :math:`s \geq 0`.
    :type s: matrix

    :param prob: The probability of success on any given trial. ExE conformable with *p*. :math:`0 \leq prob \leq 1`.
    :type prob: matrix

    :return f: The number of failures that will be observed before *s* successes.

    :rtype f: NxK matrix, Nx1 vector or scalar

Remarks
-------

*f* is the smallest number of failures whose cumulative probability is at
least *p*. The number of failures has no upper limit, so *p* = 1 returns +INF
(unless *s* = 0 or *prob* = 1, when every result is 0). With *prob* = 0 no
success ever happens, so every *p* above 0 returns +INF.

If *p* is outside [0, 1], *s* is below 0, or *prob* is outside [0, 1],
:func:`cdfNegBinomialInv` returns a scalar error code and :func:`scalerr`
returns the position of that argument: 1 for *p*, 2 for *s*, 3 for *prob*. A
missing value in any argument returns a missing value.

Example
-------

Pat is supposed to sell five candy bars to raise money for the 6th grade
field trip. So he goes door to door, selling candy bars. At each house, there is a
0.4 probability of selling one candy bar and a 0.6 probability of
selling nothing.

If we know the probability that Pat sells all of his candy bars
is 17.36704%, how many failures should we expect before he sells all five candy bars?

::

   // The probability of selling all candy bars
   p = 0.1736704;

   // Number of successes (sold candy bars)
   s = 5;

   // Probability of success at each house
   prob = 0.4;

   // Compute the number of failures
   f = cdfNegBinomialInv(p, s, prob);

After running above code, the number of *f* will be equal to 3. This means that he has 8 houses to visit to sell all his candy bars, since he will fail 3 times and succeed 5 times.

.. seealso:: :func:`cdfBinomial`, :func:`cdfBinomialInv`, :func:`cdfNegBinomial`
