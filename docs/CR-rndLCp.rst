
rndLCp
==============================================

Purpose
----------------
Computes Poisson pseudo-random numbers.
NOTE: This function is deprecated--use rndPoisson--but remains for backward compatibility.

Format
----------------
.. function:: rndLCp(r, c, lambda, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param lambda: mean parameter.
    :type lambda: scalar

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

    :returns: x (*TODO*), r x c matrix of Poisson distributed random
        numbers.

    :returns: newstate (*TODO*), 4x1 vector:

    .. csv-table::
        :widths: auto

        "[1]  the updated seed"
        "[2]  the multiplicative constant"
        "[3]  the additive constant"
        "[4]  the original initialization seed"

