
cdfNegBinomial
==============================================

Purpose
----------------
Computes the cumulative distribution function for the negative binomial distribution.

Format
----------------
.. function:: cdfNegBinomial(f,s,prob)

    :param f: Nx1 vector or scalar. 0 < f.
    :type f: NxK matrix

    :param s: ExE conformable with  f. 0 < s.
    :type s: TODO

    :param prob: The probability of success on any given trial. ExE conformable with f.
        0 < prob < 1.
    :type prob: TODO

    :returns: p (*NxK matrix*), Nx1 vector or scalar. The probability of observing  f failures before observing
        s .

