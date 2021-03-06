
rndLCp
==============================================

Purpose
----------------
Computes Poisson pseudo-random numbers.

.. NOTE:: This function is deprecated--use :func:`rndPoisson`--but remains for backward compatibility.

Format
----------------
.. function:: { x, newstate } = rndLCp(r, c, lambda, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param lambda: mean parameter.
    :type lambda: scalar

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

    :return x: Poisson distributed random numbers.

    :rtype x: RxC matrix

    :return newstate:

        .. csv-table::
            :widths: auto

            "[1]", "the updated seed"
            "[2]", "the multiplicative constant"
            "[3]", "the additive constant"
            "[4]", "the original initialization seed"

    :rtype newstate: 4x1 vector

Technical Notes
---------------

This function uses a linear congruential method, discussed in Kennedy,
W.J. Jr., and J.E. Gentle, *Statistical Computing*, Marcel Dekker, Inc.
1980, pp. 136-147. Each seed is generated from the preceding seed using
the formula

.. math::

    new\_seed = (((a * seed) \% 2^{32})+ c) \% 2_{32}


where ``%`` is the mod operator and where *a* is the multiplicative constant
and *c* is the additive constant.

Source
------

randlc.src
