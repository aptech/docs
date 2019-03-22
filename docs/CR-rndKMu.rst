
rndKMu
==============================================

Purpose
----------------
Returns a matrix of uniform (pseudo) random variables and the state
of the random number generator.

Format
----------------
.. function:: rndKMu(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: 2x1 vector, or 500x1 vector.
        Scalar case:state = starting seed value. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        2x1 vector case:
    :type state: scalar

    .. csv-table::
        :widths: auto

        "[1]    the starting seed, uses the system clock if -1"
        "[2]    0 for 0 ≤ y < 1"
        "1 for 0 ≤ y ≤ 1"
        "500x1 vector case:state = the state vector returned from a previous call to one of the rndKM random number generators."

    :returns: y (*r x c matrix*) of uniform
        random numbers, 0 ≤ y < 1.

    :returns: newstate (*500x1 vector*), the updated state.

Remarks
-------

r and c will be truncated to integers if necessary.


Examples
----------------
This example generates two thousand vectors of uniform random 
numbers, each with one million elements. The state of the random 
number generator after each iteration is used as an input to the 
next generation of random numbers.

::

    state = 13;
    n = 2000;
    k = 1000000;
    c = 0;
    submean = {};
     
    do while c < n;
       { y,state } = rndKMu(k,1,state);
       submean = submean | meanc(y);
       c = c + k;
    endo;
     
    mean = meanc(submean);
    print 0.5-mean;

.. seealso:: Functions :func:`rndKMn`, :func:`rndKMi`

Technical Notes
+++++++++++++++

rndKMu uses the recur-with-carry KISS-Monster algorithm described in the
rndKMi Technical Notes. Random integer seeds from 0 to 2\ 32-1 are
generated. Each integer is divided by 2\ 32 or 2\ 32-1.

uniform pseudo-random numbers
