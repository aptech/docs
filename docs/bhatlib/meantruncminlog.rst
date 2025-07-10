meantruncminlog
==============================================

Purpose
----------------

Computes the variance of the untruncated univariate minlogistic distribution. 

Format
----------------
.. function:: z = meantruncminlog(a, sig, c)


    :param a: Index values.
    :type a: K x 1 vector
    :param sig: Scale parameter of the minlogistic distribution.
    :type sig: Scalar
    :param c: The truncation threshold (i.e., computing E[eta | eta < c]).
    :type c: Scalar

    :return z: The expected value of the truncated minlogistic distribution.
    :rtype z: Scalar

Remarks
------------

- - This function computes the expected value of ? given ? < c.
- - The minlogistic distribution is commonly used in discrete choice models and extreme value analysis.
- - Ensure `sig > 0` and `c` is appropriately chosen relative to `a` to maintain valid truncation.

Source
------------

gradients-mvn.src
