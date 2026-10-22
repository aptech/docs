
cdfNegBinomial
==============================================

Purpose
----------------
Computes the cumulative distribution function for the negative binomial distribution.

Format
----------------
.. function:: p = cdfNegBinomial(x, s, prob)

    :param x: Number of failures. An *x* below 0 returns 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param s: ExE conformable with *x*, the number of successes. :math:`s \geq 0`.
    :type s: matrix

    :param prob: The probability of success on any given trial. ExE conformable with *x*. :math:`0 \leq prob \leq 1`.
    :type prob: matrix

    :return p: The probability of observing *x* failures before observing *s* successes.

    :rtype p: NxK matrix, Nx1 vector or scalar

Remarks
-------

If *s* is below 0 or *prob* is outside [0, 1], :func:`cdfNegBinomial` returns a
scalar error code and :func:`scalerr` returns the position of that argument: 2
for *s*, 3 for *prob*. An *x* below 0 is not an error: it returns 0. A missing
value in any argument returns a missing value.

Example
-------

Pat has to sell five candy bars to raise money for the 6th grade
field trip. So the child goes door to door, selling candy bars. At each house, there is a
0.4 probability of selling one candy bar and a 0.6 probability of
selling nothing.

What's the probability that Pat finishes on or before reaching houses five through 
eight?

::

   // x is number of failures, x = 0, 1, 2, 3
   x = seqa(0, 1, 4);

   // Probability of selling each candy bar is 0.4
   prob = 0.4;

   // Number of successes (sold candy bars)
   s = 5;

   p = cdfNegBinomial(x, s, prob);

   // 5 successes + x failures = total houses visited
   h = x + 5;

   print  "After nth try, the probability =";
   print h~p;

After running above code, the probability that Pat finishes on or before
reaching the eighth house is 0.1736704 or 17.36704%. The other probabilities are also listed below.

::

   After nth try, the probability =

   5.0000000      0.010240000
   6.0000000      0.040960000
   7.0000000      0.096256000
   8.0000000       0.17367040

.. seealso:: :func:`cdfBinomial`, :func:`cdfBinomialInv`, :func:`cdfNegBinomialInv`
