noncdfmmvlogitc
==============================================

Purpose
----------------

Computes the gradients of the non-standard multivariate minlogistic cumulative distribution function (cdf) combined with its complement (sdf), where X follows a multivariate minlogistic distribution. 

Format
----------------
.. function:: w = noncdfmmvlogitc(a, c, mu, sig, indxcomp)


    :param a: Matrix of coefficients (Q x K) for the minlogistic distribution.
    :type a: Q x K matrix 
    :param c: Abscissae at which to compute the cumulative distribution.
    :type c: K x 1 vector
    :param mu: Location parameters.
    :type mu: K x 1 vector
    :param sig: Scale parameters.
    :type sig: K x 1 vector
    :param indxcomp: Index vector indicating which components of the multivariate distribution to consider for the computation of the cdf and sdf.
    :type indxcomp: K x 1 vector

    :return w: Probability Pr(X < c) for certain components
    :rtype w: Scalar

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);


Source
------------

gradients-mvn.src
