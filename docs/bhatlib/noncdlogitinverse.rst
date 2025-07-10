noncdlogitinverse
==============================================
Purpose
----------------
Computes the complement of the inverse cumulative distribution function for the logit distribution.

Format
----------------
.. function:: x = noncdlogitinverse(p)

    :param p: Probability values (0 < p < 1).
    :type p: scalar or vector

    :return x: Computed complement quantile values.
    :rtype x: scalar or vector

Library
-------
bhatlib

Source
------
gradients-mvn.src