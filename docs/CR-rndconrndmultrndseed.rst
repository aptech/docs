
rndcon, rndmult, rndseed
==============================================

Purpose
----------------

Resets the parameters of the linear congruential random number 
generator that is the basis for :func:`rndu`, :func:`rndi` and :func:`rndn`.

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

.. DANGER:: how do we want to format the above block?

Remarks
-------

A linear congruential uniform random number generator is used by :func:`rndu`,
and is also called by :func:`rndn`. These statements allow the parameters of
this generator to be changed.

The procedure used to generate the uniform random numbers is as follows.
First, the current "seed" is used to generate a new seed:

.. DANGER:: fix equations

.. math::

   new_seed = (((a * seed) % 232)+ c) % 232

(where ``%`` is the mod operator). Then a number between 0 and 1 is created
by dividing the new seed by :math:`2\ :sup:`32``:

.. math::

   x =  new_seed / 232

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

