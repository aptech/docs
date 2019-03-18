
rndKMn
==============================================

Purpose
----------------

Returns a matrix of standard normal (pseudo) random variables and 
the state of the random number generator.

Format
----------------
.. function:: rndKMn(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: scalar or 500x1 vector.
        Scalar case:state = starting seed value. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        500x1 vector case:state = the state vector returned from a previous
        call to one of the rndKM random number generators.
    :type state: TODO

    :returns: y (*TODO*), r x c matrix of standard
        normal random numbers.

    :returns: newstate (*500x1 vector*), the updated state.

Examples
----------------
This example generates two thousand vectors of standard normal 
random numbers, each with one million elements. The state of the 
random number generator after each iteration is used as an input to
the next generation of random numbers.

::

    state = 13;
    n = 2000;
    k = 1000000;
    c = 0;
    submean = {};
     
    do while c < n;
       { y,state } = rndKMn(k,1,state);
       submean = submean | meanc(y);
       c = c + k;
    endo;
     
    mean = meanc(submean);
    print mean;

.. seealso:: Functions :func:`rndKMu`, :func:`rndKMi`

Technical Notes
+++++++++++++++

rndKMn calls the uniform random number generator that is the basis for
rndKMu multiple times for each normal random number generated. This is
the recur-with-carry KISS+Monster algorithm described in the rndKMi
Technical Notes. Potential normal random numbers are filtered using the
fast acceptance-rejection algorithm proposed by Kinderman, A.J. and J.G.
Ramage, "Computer Generation of Normal Random Numbers," Journal of the
American Statistical Association, December 1976, Volume 71, Number 356,
pp. 893-896. It employs the error correction from Tirler et al. (2004),
"An error in the Kinderman-Ramage method and how to fix it,"
Computational and Data Analysis, Vol. 47, 433-40.

standard normal pseudo-random numbers
