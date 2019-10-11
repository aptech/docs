
rndKMi
==============================================

Purpose
----------------

Returns a matrix of random integers, :math:`0 ≤ y < 2_32`, and the state of the random number generator.

.. DANGER:: fix equations

Format
----------------
.. function:: { y, newstate } = rndKMi(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: 

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**
        
            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :return y: of random integers between :math:`0` and :math:`2_32 - 1`, inclusive.

    :rtype y: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: 500x1 vector

Examples
----------------
This example generates two thousand vectors of random integers, 
each with one million elements. The state of the random number 
generator after each iteration is used as an input to the next 
generation of random numbers.

::

    state = 13;
    n = 2000;
    k = 1000000;
    c = 0;
    min = 2^32+1;
    max = -1;
     
    do while c < n;
       { y,state } = rndKMi(k,1,state);
       min = minc(min | minc(y));
       max = maxc(max | maxc(y));
       c = c + k;
    endo;
     
    print "min " min;
    print "max " max;

Remarks
-------

*r* and *c* will be truncated to integers if necessary.


Technical Notes
---------------

:func:`rndKMi` generates random integers using a KISS+Monster algorithm
developed by George Marsaglia. KISS initializes the sequence used in the
recur-with-carry Monster random number generator.

.. seealso:: Functions :func:`rndKMn`, :func:`rndKMu`

