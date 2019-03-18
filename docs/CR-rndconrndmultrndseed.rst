
rndcon, rndmult, rndseed
==============================================

Purpose
----------------

Resets the parameters of the linear congruential random number 
generator that is the basis for rndu, 
rndi and rndn.

Format
----------------
.. function:: rndcon crndmult a 
			  rndseed seed

    :param c: constant for the random number generator.
    :type c: scalar

    :param a: multiplier for the random number generator.
    :type a: scalar

    :param seed: initial seed for the random number generator.
    :type seed: scalar

