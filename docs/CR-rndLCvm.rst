
rndLCvm
==============================================

Purpose
----------------

Computes von Mises pseudo-random numbers.
NOTE: This function is deprecated but remains for backward compatibility. 

Format
----------------
.. function:: rndLCvm(r, c, m, k, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param m: or rx1 vector,
        or 1xc vector, or scalar, means for vm distribution.
    :type m: r x c matrix

    :param k: or rx1 vector,
        or 1xc vector, or scalar, shape argument for vm distribution.
    :type k: r x c matrix

    :param state: or 3x1 vector, or 4x1 vector.
        Scalar case:state = starting seed value only. System default
        values are used for the additive and multiplicative constants.
        
        The defaults are 1013904223, and 1664525, respectively. These
        may be changed with rndcon and rndmult.
        
        If state = -1, GAUSS computes the starting seed
        based on the system clock.
        3x1 vector case:
    :type state: scalar

    .. csv-table::
        :widths: auto

        "[1]  the starting seed, uses the system clock if -1"
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "4x1 vector case:state = the state vector returned from a previouscall to one of the rndLC random number generators."

    :returns: x (*r x c matrix*), von Mises distributed random numbers.

    :returns: newstate (*TODO*), 4x1 vector:

    .. csv-table::
        :widths: auto

        "[1]  the updated seed"
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "[4]  the original initialization seed"



Remarks
-------

r and c will be truncated to integers if necessary.



Source
------

randlc.src

