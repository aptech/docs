
rndcon, rndmult, rndseed
==============================================

Purpose
----------------

Resets the parameters of the deprecated linear congruential random number
generator that is the basis for :func:`_rndu`, :func:`_rndn` and :func:`_rndng10`.

.. _rndcon:
.. _rndmult:
.. _rndseed:

.. index:: rndcon, rndmult, rndseed

Format
----------------

::

    rndcon c;
    rndmult a;
    rndseed seed;

**Parameters**

    :c: (*scalar*) constant for the random number generator.
    
    :a: (*scalar*) multiplier for the random number generator.
    
    :seed: (*scalar*) initial seed for the random number generator.
    
    Parameter default values and ranges:
    
    ::
    
        seed    time(0)       0 < seed < 232a       1664525       0 < a < 232c       1013904223    0 < a < 232


Remarks
-------

Even though the current versions of :func:`rndn`, :func:`rndu`, :func:`rndBeta`, etc do not use the old linear congruential RNG, you may use ``rndseed`` to set the seed for the purpose of creating repeatable pseudo-random sequences.

In years passed, a linear congruential uniform random number generator was used by :func:`rndu`,
and :func:`rndn`. For backward compatibility, this generator may be accessed by the functions :func:`_rndu`, :func:`_rndn` and :func:`rndng10`. 

These statements allow the parameters of this generator to be changed.

The procedure used to generate the uniform random numbers is as follows.
First, the current "seed" is used to generate a new seed:

.. math::

   new\_seed = (((a * seed) \% 2^{32})+ c) \% 2^{32}

(where ``%`` is the mod operator). Then a number between 0 and 1 is created
by dividing the new seed by :math:`2^{32}`:

.. math::

   x =  \frac{new\_seed}{2^{32}}

`rndcon` resets *c*.

`rndmult` resets *a*.

`rndseed` resets *seed*. This is the initial seed for the generator. The
default is that GAUSS uses the clock to generate an initial seed when
GAUSS is invoked.

GAUSS goes to the clock to seed the generator only when it is first
started up. Therefore, if GAUSS is allowed to run for a long time, and
if large numbers of random numbers are generated, there is a possibility
of recycling (that is, the sequence of "random numbers" will repeat
itself). However, the generator used has an extremely long cycle, so
that should not usually be a problem.

The parameters set by these commands remain in effect until new commands
are encountered, or until GAUSS is restarted.

.. seealso:: Functions :func:`rndu`, :func:`rndn`, :func:`rndi`, :func:`rndLCi`, :func:`rndKMi`
