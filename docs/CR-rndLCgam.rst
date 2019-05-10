
rndLCgam
==============================================

Purpose
----------------

Computes Gamma pseudo-random numbers.

.. NOTE:: This function is deprecated--use :func:`rndGamma`--but remains for backward compatibility. 

Format
----------------
.. function:: rndLCgam(r, c, alpha, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: r x c matrix or rx1 vector, or 1xc vector, or scalar, shape argument for gamma distribution.
    :type alpha: matrix or vector or scalar

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

    :returns: x (*RxC matrix*), gamma distributed random numbers.

    :returns: newstate (*4x1 vector*)

        .. csv-table::
            :widths: auto
    
            "[1]", "the updated seed"
            "[2]", "the multiplicative constant"
            "[3]", "the additive constant"
            "[4]", "the original initialization seed"


Technical Notes
---------------

This function uses a linear congruential method, discussed in Kennedy,
W.J. Jr., and J.E. Gentle, *Statistical Computing*, Marcel Dekker, Inc.
1980, pp. 136-147. Each seed is generated from the preceding seed using
the formula

.. math::

    new_seed = (((a * seed) % 232)+ c) % 232

.. DANGER:: fix equations

where ``%`` is the mod operator and where *a* is the multiplicative constant
and *c* is the additive constant.

Source
------

randlc.src

