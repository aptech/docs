
cdfNegBinomialInv
==============================================

Purpose
----------------
Computes the quantile or inverse negative binomial cumulative distribution function.

Format
----------------
.. function:: cdfNegBinomialInv(p, s, prob)

    :param p: Nx1 vector or scalar. 0 < f < 1.
    :type p: NxK matrix

    :param s: ExE conformable with  p. 0 < s.
    :type s: TODO

    :param prob: The probability of success on any given trial. ExE conformable with  p.
        0 < prob < 1.
    :type prob: TODO

    :returns: f (*NxK matrix*), Nx1 vector or scalar.

