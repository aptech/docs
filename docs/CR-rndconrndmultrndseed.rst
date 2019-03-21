
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



Remarks
-------

A linear congruential uniform random number generator is used by rndu,
and is also called by rndn. These statements allow the parameters of
this generator to be changed.

The procedure used to generate the uniform random numbers is as follows.
First, the current ''seed'' is used to generate a new seed:

::

   new_seed = (((a * seed) % 232)+ c) % 232

(where % is the mod operator). Then a number between 0 and 1 is created
by dividing the new seed by 2\ :sup:`32`:

::

   x =  new_seed / 232

rndcon resets c.

rndmult resets a.

rndseed resets seed. This is the initial seed for the generator. The
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

