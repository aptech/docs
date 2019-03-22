
rndLCu
==============================================

Purpose
----------------

Returns a matrix of uniform (pseudo) random variables and the state
of the random number generator.
NOTE: This function is deprecated but remains for backward compatibility. 

Format
----------------
.. function:: rndLCu(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state: or 3x1 vector, or 4x1 vector.
        Scalar case:state = starting seed value only. System default
        values are used for the additive and multiplicative constants.
        
        The defaults are 1013904223, and 1664525, respectively. These
        may be changed with rndcon and rndmult.
        3x1 vector case:
    :type state: scalar

    .. csv-table::
        :widths: auto

        "[1]  the starting seed, uses the system clock if < 0"
        "If state < 0, GAUSS computes the starting seedbased on the system clock."
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "4x1 vector case:state = the state vector returned from a previouscall to one of the rndLC random number generators."

    :returns: y (*r x c matrix*) of uniform (0 < x < 1) random numbers.

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
and c is the additive constant. A number between 0 and 1 is created by
dividing new_seed by 2\ :sup:`32`.


Examples
----------------

::

    state = 13;
    n = 2000000000;
    k = 1000000;
    c = 0;
    submean = {};
     
    do while c < n;
       { y,state } = rndLCu(k,1,state);
       submean = submean | meanc(y);
       c = c + k;
    endo;
     
    mean = meanc(submean);
    print 0.5-mean;

.. seealso:: Functions :func:`rndLCn`, :func:`rndLCi`, :func:`rndcon`, :func:`rndmult`

Technical Notes
+++++++++++++++

This function uses a linear congruential method, discussed in Kennedy,
W. J. Jr., and J. E. Gentle, Statistical Computing, Marcel Dekker, Inc.,
1980, pp. 136-147.

| 
