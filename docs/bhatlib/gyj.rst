gyj
==============================================
Purpose
----------------
Computes the gradient of the Yeo-Johnson transformation.

Format
----------------
.. function:: g = gyj(lamnew, x)

    :param lamnew: Lambda parameter (logit transformed).
    :type lamnew: scalar or vector

    :param x: Input data vector.
    :type x: vector

    :return g: Gradient vector.
    :rtype g: vector

Library
-------
bhatlib

Source
------
vecup.src