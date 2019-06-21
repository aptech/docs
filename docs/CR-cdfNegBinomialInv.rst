
cdfNegBinomialInv
==============================================

Purpose
----------------
Computes the quantile or inverse negative binomial cumulative distribution function.

Format
----------------
.. function:: cdfNegBinomialInv(p, s, prob)

    :param p: The probability of observing *f* failures before observing *s*. :math:`0 < f < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param s: ExE conformable with *p*. :math:`0 < s`.
    :type s: matrix

    :param prob: The probability of success on any given trial. ExE conformable with *p*. :math:`0 < prob < 1`.
    :type prob: matrix

    :returns: **f** (*NxK matrix, Nx1 vector or scalar*) - The number of failures that will be observed for each respective element in *p*.

Remarks
-------

For invalid inputs, :func:`cdfNegBinomialInv` will return a scalar error code
which, when its value is assessed by function :func:`scalerr`, corresponds to
the invalid input. If the first input is out of range, scalerr will
return a 1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Example
-------

Pat is required to sell candy bars to raise money for the 6th grade
field trip. There are thirty houses in the neighborhood, and Pat is not
supposed to return home until five candy bars have been sold. So the
child goes door to door, selling candy bars. At each house, there is a
0.4 probability of selling one candy bar and a 0.6 probability of
selling nothing.

If we know the probability that Pat finishes selling the last candy bar
is 17.36704%, then how many times of selling nothing?

::

   // p is the probability of selling the last candy bar
   p = 0.1736704;

   // Number of successes
   s = 5;

   // Probability of successes
   prob = 4;

   // f is number of failure times
   f = cdfNegBinomialInv(p, s, prob);

   print  "selling nothing times =";
   print f;

After running above code, the number of failure times is

::

   selling nothing times =
   3.0000000


.. seealso:: :func:`cdfBinomial`, :func:`cdfBinomialInv`, :func:`cdfNegBinomial`
