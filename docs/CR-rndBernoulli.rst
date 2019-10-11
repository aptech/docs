
rndBernoulli
==============================================

Purpose
----------------

Computes Bernoulli distributed random numbers.

Format
----------------
.. function:: r = rndBernoulli(r, c, prob)
              { r, newstate } = rndBernoulli(r, c, prob, state)

    :param r: number of rows of the output matrix.
    :type r: scalar

    :param c: number of columns of the output matrix.
    :type c: scalar

    :param prob: probability parameter.
    :type prob: scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return r: Bernoulli random numbers.

    :rtype r: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

::

    // Bernoulli random numbers can be used to model qualitative
    // binary data (i.e., yes/no, true/false), such as marital
    // status.
    
    // Set the random seed for repeatable numbers.
    rndseed 723940439;
    
    // The percentage of married people in the population we
    // would like to model.
    prob = 0.7;
    
    // Create 10,000 Bernoulli random numbers
    r = rndBernoulli(10000, 1, prob);
    
    // The mean of 'r' should approximately equal 'prob'
    mu = meanc(r);
    print mu;

::

    0.70270000

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(X) = prob

   Var(X) = prob * (1 - prob)


.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`

