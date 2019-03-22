
rndLCi
==============================================

Purpose
----------------

Returns a matrix of random integers, 0 ≤ y < 232, and the 
state of the random number generator.
NOTE: This function is deprecated but remains for backward compatibility. 

Format
----------------
.. function:: rndLCi(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: or 3x1 vector, or 4x1 vector.
        Scalar case:state = starting seed value only. System default
        values are used for the additive and multiplicative constants.
        
        The defaults are 1013904223, and 1664525, respectively. These
        may be changed with rndcon and rndmult.
        
        If state < 0, GAUSS computes the starting seed
        based on the system clock.3x1 vector case:
    :type state: scalar

    .. csv-table::
        :widths: auto

        "[1]  the starting seed, uses the system clock if < 0"
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "4x1 vector case:state = the state vector returned from a previous call to one of the rndLC random number generators."

    :returns: y (*r x c matrix*) of random
        integers between 0 and 232 - 1, inclusive.

    :returns: newstate (*4x1 vector*) :

    .. csv-table::
        :widths: auto

        "[1]  the updated seed"
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "[4]  the original initialization seed"

Remarks
-------

r and c will be truncated to integers if necessary.

Each seed is generated from the preceding seed, using the formula

::

   new_seed = (((a *  seed) % 232)+ c) % 232

where % is the mod operator and where a is the multiplicative constant
and c is the additive constant. The new seeds are the values returned.


Examples
----------------

::

    state = 13;
    n = 2000000000;
    k = 1000000;
    c = 0;
    min = 2^32+1;
    max = -1;
     
    do while c < n;
       { y,state } = rndLCi(k,1,state);
       min = minc(min | minc(y));
       max = maxc(max | maxc(y));
       c = c + k;
    endo;
     
    print "min " min;
    print "max " max;

.. seealso:: Functions :func:`rndLCn`, :func:`rndLCu`, :func:`rndcon`, :func:`rndmult`
