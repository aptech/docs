
rndLCn
==============================================

Purpose
----------------
Returns a matrix of standard normal (pseudo) random variables and the state of the random number generator.

.. NOTE:: This function is deprecated--use :func:`rndn`--but remains for backward compatibility. 

Format
----------------
.. function:: { y, newstate } = rndLCn(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: 

        **scalar case**
        
            *state* = starting seed value only. System default values are used for the additive and multiplicative constants.
            
            The defaults are 1013904223, and 1664525, respectively. These may be changed with `rndcon` and `rndmult`.
            
            If *state* = -1, GAUSS computes the starting seed based on the system clock.

        **3x1 vector case**

            .. csv-table::
                :widths: auto
        
                "[1]", "the starting seed, uses the system clock if -1"
                "[2]", "the multiplicative constant"
                "[3]", "the additive constant"

        **4x1 vector case**
        
            *state* = the state vector returned from a previous call to one of the ``rndLC`` random number generators.

    :type state: scalar or vector

    :return y: of standard normal random numbers.

    :rtype y: RxC matrix

    :return newstate: 
    
        .. csv-table::
            :widths: auto
    
            "[1]", "the updated seed"
            "[2]", "the multiplicative constant"
            "[3]", "the additive constant"
            "[4]", "the original initialization seed"

    :rtype newstate: 4x1 vector

Examples
----------------

::

    state = 13;
    n = 2000000000;
    k = 1000000;
    c = 0;
    submean = {};
     
    do while c < n;
       { y,state } = rndLCn(k,1,state);
       submean = submean | meanc(y);
       c = c + k;
    endo;
     
    mean = meanc(submean);
    print mean;

Remarks
-------

*r* and *c* will be truncated to integers if necessary.

Technical Notes
----------------

The normal random number generator is based on the uniform random number
generator, using the fast acceptance-rejection algorithm proposed by
Kinderman, A.J. and J.G. Ramage, "Computer Generation of Normal Random
Numbers," *Journal of the American Statistical Association*, December
1976, Volume 71, Number 356, pp. 893-896. This algorithm calls the
linear congruential uniform random number generator multiple times for
each normal random number generated.

See :func:`rndLCu` for a description of the uniform random number generator algorithm.

.. seealso:: Functions :func:`rndLCu`, :func:`rndLCi`, :func:`rndcon`, :func:`rndmult`

