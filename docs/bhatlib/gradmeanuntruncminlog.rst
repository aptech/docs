gradmeanuntruncminlog
==============================================

Purpose
----------------

Computes the mean of the truncated univariate minlogistic distribution. 

Format
----------------
.. function:: { z, ga, gsig } = gradmeanuntruncminlog(a, sig)


    :param a: Index values.
    :type a: Kx1 vector
    :param sig: Thehe scale parameter of the minlogistic distribution.
    :type sig: scalar

    :return z: The mean of the untruncated minlogistic distribution.
    :rtype z: scalar
    :return ga: Gradient of the mean with respect to the index values `a`.
    :rtype ga: Kx1 vector
    :return gsig: Gradient of the mean with respect to the scale parameter `sig`.
    :rtype gsig: Kx1 vector

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The minlogistic distribution is often used in discrete choice modeling and extreme value theory.
- - Ensure that `sig > 0` to maintain a valid scale parameterization.
- - Verified in test cases located at `g:\gauss\com\MDCEVtwostage\test`.

Source
------------

gradients-mvn.src
