vartruncminlog
==============================================

Purpose
----------------

Computes the complement of the non-standard multivariate logistic cumulative distribution function (CDF). This calculates the probability that a multivariate logistic-distributed variable exceeds a given threshold. 

Format
----------------
.. function:: v = vartruncminlog(a, sig, c)


    :param a: (K x 1) vector of index values.
    :type a: (Specify type)
    :param sig: (1 x 1) scalar representing the scale parameter of the minlogistic distribution.
    :type sig: (Specify type)
    :param c: (1 x 1) scalar representing the truncation threshold (upper bound).
    :type c: (Specify type)

    :return v: (1 x 1) scalar, the variance of the truncated minlogistic distribution.
    :rtype v: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function computes the expected variance under truncation at `c`.
- - The minlogistic distribution is commonly used in extreme value theory and discrete choice modeling.
- - Ensure `sig > 0` for a valid variance computation.
- - This function assumes left-truncation (i.e., ? is truncated above at `c`).

Source
------------

gradients-mvn.src
