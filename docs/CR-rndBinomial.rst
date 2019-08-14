
rndBinomial
==============================================

Purpose
----------------

Computes binomial pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: { x, newstate } = rndBinomial(r, c, trials, prob[, state])

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param trials: r x c matrix or rx1 vector, or 1xc vector, or scalar, the number of trials.
    :type trials: matrix or vector or scalar

    :param prob: r x c matrix or rx1 vector, or 1xc vector, or scalar, the probability of success of each trial.
    :type prob: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: binomially distributed random numbers.

    :type x: RxC matrix

    :return newstate: the updated state.

    :type newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   $\mu = np\\
   \sigma^2 = np(1 - p)\\
   \text{pmf } = {{n}\choose{k}}p^k(1 - p)^{n - k}\\
   \text{ }\\
   \text{n = number of trials}\\
   \text{p = probability of success}\\
   \text{k = number of successes}$

*r* and *c* will be truncated to integers if necessary.


Examples
----------------

Basic usage
+++++++++++

::

    // Set seed for repeatable random numbers
    rndseed 7345;
    
    // Simulate the number of successes from 1024 trials,
    // each of which have a 40% chance of success, 3 times
    n = 1024;
    p = 0.4;		
    k = rndBinomial(3, 1, n, p);

After the code above, *k* should equal:

::

    413
    390
    427

Pass seed and return state vector
+++++++++++++++++++++++++++++++++

::

    // Simulate the number of successes from 1024 trials,
    // each of which have a 40% chance of success, 3 times
    n = 1024;
    p = 0.4;
    
    // Pass in seed as optional final input argument
    // and return state vector as second output
    { k, state } = rndBinomial(3, 1, n, p, 7345);

After the code above, *k* should equal:

::

    413
    390
    427

Technical Notes
+++++++++++++++

The default generator for rndBinomial is the SFMT Mersenne-Twister
19937. You can specifiy a different underlying random number generator
with the function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

