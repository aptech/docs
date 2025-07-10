varuntruncminlog
==============================================

Purpose
----------------

Computes the variance of the truncated univariate minlogistic distribution. Specifically, it calculates the variance of ? given that ? < c. 

Format
----------------
.. function:: v = varuntruncminlog(a, sig)


    :param a: (K x 1) vector of index values.
    :type a: (Specify type)
    :param sig: (1 x 1) scalar representing the scale parameter of the minlogistic distribution.
    :type sig: (Specify type)

    :return v: (1 x 1) scalar, the variance of the untruncated minlogistic distribution.
    :rtype v: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The variance of the minlogistic distribution depends on the scale parameter `sig`.
- - The minlogistic distribution is commonly used in extreme value theory and discrete choice modeling.
- - Ensure `sig > 0` to maintain a valid variance computation.

Source
------------

gradients-mvn.src
