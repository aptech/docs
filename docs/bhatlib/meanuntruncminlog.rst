meanuntruncminlog
==============================================

Purpose
----------------

Computes the gradient of the mean of the untruncated univariate minlogistic distribution. 

Format
----------------
.. function:: mean_val = meanuntruncminlog(a, sig)


    :param a: Index values.
    :type a: K x 1 vector
    :param sig: Scale parameter of the minlogistic distribution.
    :type sig: Scalar

    :return mean_val: Mean of the untruncated minlogistic distribution.
    :rtype mean_val: K x 1 vector

Remarks
------------

- - The minlogistic distribution is characterized by its heavy tails and is often used
- in extreme value modeling and discrete choice modeling.
- - Ensure that `sig > 0` to maintain validity in scale parameterization.

Source
------------

gradients-mvn.src
