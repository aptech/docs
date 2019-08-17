
rndNegBinomial
==============================================

Purpose
----------------

Computes negative binomial pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndNegBinomial(r, c, ns, prob)
              { x, newstate } = rndNegBinomial(r, c, ns, prob, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param ns: r x c matrix or rx1 vector, or 1xc vector, or scalar, "event" argument for negative binomial distribution.
    :type ns: matrix or vector or scalar

    :param prob: r x c matrix or rx1 vector, or 1xc vector, or scalar, "probability" argument for negative binomial distribution.
    :type prob: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: negative binomial distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = num_s*(1 - prob)/prob 

   Var(x) = num_s*(1 - prob)/prob2

   num_s > 0

   0 < prob < 1

.. DANGER:: fix equations

:func:`rndNegBinomial` has a different parameterization than the deprecated
:func:`rndnb`. To convert a call to :func:`rndnb` to an equivalent call to
:func:`rndNegBinomial`, pass in :math:`1 - prob` in place of *prob*. For example, the
following two calls are equivalent.

::

   x_1 = rndnb(1e6, 1, 15, 0.3);
   x_2 = rndNegBinomial(1e6, 1, 15, 0.7);

*r* and *c* will be truncated to integers if necessary.

Examples
----------------

Example 1
+++++++++

Simulate the number of failures before 30 successes where each trial has a 70% probability of success.

::

    num_obs = 100;
    
    num_s = 30;
    prob = 0.70;
    
    num_f = rndNegBinomial(num_obs, 1, num_s, prob);

Example 2
+++++++++

An alternative parameterization specifies the negative binomial distribution in terms of a dispersion parameter (*dp*) and a mean parameter (*mu*). If you would prefer to think of it in those terms, you may do so by passing in the dispersion parameter *dp*, in place of *num_s* and passing in :math:`dp/(dp + mu)` in place of *prob*.

::

    // dispersion parameter
    dp = 12;
    
    // mean parameter
    mu = 3;
    
    x = rndNegBinomial(100, 1, dp, dp./(dp + mu));

Technical Notes
----------------

The default generator for :func:`rndNegBinomial` is the SFMT Mersenne-Twister
19937. You can specifiy a different underlying random number generator
with the function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

