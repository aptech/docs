
rndLCgam
==============================================

Purpose
----------------

Computes Gamma pseudo-random numbers.

.. NOTE:: This function is deprecated--use :func:`rndGamma`--but remains for backward compatibility.

Format
----------------
.. function:: { x, newstate } = rndLCgam(r, c, alpha, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: shape argument for gamma distribution, scalar or ExE conformable matrix with *r* and *c*.
    :type alpha: matrix, vector or scalar

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

    :return x: gamma distributed random numbers.

    :rtype x: RxC matrix

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

    // Generate a 3x2 matrix of gamma random numbers
    // with shape alpha = 5, using a fixed seed for repeatable output
    { x, newstate } = rndLCgam(3, 2, 5, 12345);
    print x;

The output is a 3x2 matrix of gamma-distributed values. The sample mean is approximately 5, consistent with the theoretical mean of alpha:

::

       4.3270396        9.4093462
       3.9689646        4.7393241
       6.1082705        5.6436564

Technical Notes
---------------

This function uses a linear congruential method, discussed in Kennedy,
W.J. Jr., and J.E. Gentle, *Statistical Computing*, Marcel Dekker, Inc.
1980, pp. 136-147. Each seed is generated from the preceding seed using
the formula

.. math::

    new\_seed = (((a * seed) \% 2^{32})+ c) \% 2^{32}


where ``%`` is the mod operator and where *a* is the multiplicative constant
and *c* is the additive constant.

Source
------

randlc.src
