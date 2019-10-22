
rndu
==============================================

Purpose
----------------

Computes uniform random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: y = rndu(r, c)
              { y, newstate } = rndu(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return y: of uniform random numbers, :math:`0 <= y < 1`.

    :rtype y: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

Example 1
+++++++++

Basic usage.

If a state or seed is not passed in, then only the random numbers are returned.

::

    // Create a 100x1 vector of uniform random numbers
    y = rndu(100, 1);

Example 2
+++++++++

:func:`rndu` can be used to create a vector of random integers in a specified range. The example below, creates 30 random integers in the range :math:`[1, 1000]`.

::

    // Largest number in integer range
    size = 1000; 
    
    // Number of integers to calculate
    num_indices = 30;
    
    idx = ceil(size .* rndu(num_indices, 1));

Example 3
+++++++++

This example generates two thousand vectors of uniform random 
numbers, each with one million elements. The state of the random 
number generator after each iteration is used as an input to the 
next generation of random numbers.

::

    // starting seed
    state = 13;
    
    // Number of submeans to calculate
    n_iters = 2000;
    
    // Number of random numbers to generate
    // on each iteration
    k = 1000000;
    
    // Pre-allocate 'submean' vector
    submean = zeros(n_iters, 1);
     
    for i(1, n_iters, 1);
       { y,state } = rndu(k,1,state);
       submean[i] = meanc(y);
    endfor;
     
    mean = meanc(submean);
    print 0.5-mean;

Remarks
-------

*r* and *c* will be truncated to integers if necessary.


Technical Notes
---------------

The default generator for rndu is the SFMT Mersenne-Twister 19937. You
can specifiy a different underlying random number generator with the
function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

