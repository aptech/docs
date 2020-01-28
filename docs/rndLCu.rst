
rndLCu
==============================================

Purpose
----------------

Returns a matrix of uniform (pseudo) random variables and the state
of the random number generator.
NOTE: This function is deprecated but remains for backward compatibility.

Format
----------------
.. function:: { y, newstate } = rndLCu(r, c, state)

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

    :return y: uniform (:math:`0 < x < 1`) random numbers.

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
       { y,state } = rndLCu(k,1,state);
       submean = submean | meanc(y);
       c = c + k;
    endo;

    mean = meanc(submean);
    print 0.5-mean;

Remarks
-------

*r* and *c* will be truncated to integers if necessary.

Each seed is generated from the preceding seed using the formula

.. math::

    new\_seed = (((a * seed) \% 2^{32})+ c) \% 2^{32}

where ``%`` is the mod operator and where *a* is the multiplicative constant
and *c* is the additive constant. A number between 0 and 1 is created by
dividing new_seed by :math:`2\ :sup:`32``.


Technical Notes
---------------

This function uses a linear congruential method, discussed in Kennedy,
W.J. Jr., and J.E. Gentle, *Statistical Computing*, Marcel Dekker, Inc.
1980, pp. 136-147.


.. seealso:: Functions :func:`rndLCn`, :func:`rndLCi`, :func:`rndcon`, :func:`rndmult`
