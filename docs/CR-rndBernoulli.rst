
rndBernoulli
==============================================

Purpose
----------------

Computes Bernoulli distributed random numbers.

Format
----------------
.. function:: rndBernoulli(r, c, prob)

    :param r: number of rows of the output matrix.
    :type r: Scalar

    :param c: number of columns of the output matrix.
    :type c: Scalar

    :param prob: probability parameter.
    :type prob: Scalar

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*r x c matrix*), Bernoulli random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------

::

    //Bernoulli random numbers can be used to model qualitative
    //binary data (i.e., yes/no, true/false), such as marital
    //status.
    
    //Set the random seed for repeatable numbers.
    rndseed 723940439;
    
    //The percentage of married people in the population we
    //would like to model.
    prob = 0.7;
    
    //Create 10,000 Bernoulli random numbers
    r = rndBernoulli(10000, 1, prob);
    
    //The mean of 'r' should approximately equal 'prob'
    mu = meanc(r);
    print mu;

::

    0.70270000

.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`

random number Bernoulli distribution
