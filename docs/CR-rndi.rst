
rndi
==============================================

Purpose
----------------

Returns a matrix of random integers from a user defined range.

Format
----------------
.. function:: y = rndi(r, c[, range])
              { y, newstate } = rndi(r, c, range, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param range: Optional argument. 2x1 matrix, the requested range of the random integers. The first element is the
        range minimum and the second element is the range maximum. If range is not supplied,
        the default range is :math:`0 ≤ y < 2^{32}`.
    :type range: matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return y: of random integers in the specified range.

    :rtype y: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

Basic example
+++++++++++++

::

    // Create a 10x5 vector of random
    // integers between 0 and 2^32 - 1
    r_int = rndi(10, 5);

Basic range
+++++++++++

::

    // Create a 10x1 vector of random
    // integers between 1 and 100
    range_start = 1;
    range_end = 100;
    idx = rndi(10, 1, range_start | range_end);

Sample with replacement from a dataset
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data from the 'fueleconomy' dataset
    // in the GAUSS examples directory
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";
    fueleconomy = loadd(file_name);

    // Create a 100x1 vector of random
    // integers between 1 and 100
    range_start = 1;
    range_end = rows(fueleconomy);
    idx = rndi(100, 1, range_start | range_end);

    // Draw a 100 observation sample from 'fueleconomy'
    fuel_sample = fueleconomy[idx, .];

Using a state-vector
++++++++++++++++++++

::

    // Create a 1050x1 vector of random
    // integers between 20 and 150
    seed_start = 5423432;
    range = { 20, 150 };
    { idx, state } = rndi(1050, 1, range, seed_start);

Remarks
-------

*r* and *c* will be truncated to integers if necessary.

This generator is automatically seeded using the system clock when GAUSS
first starts. However, that can be overridden using the `rndseed`
statement, or passing in a seed or state as the last input to :func:`rndi`.

.. seealso:: Functions :func:`rndu`, :func:`rndn`, :func:`rndseed`, :func:`rndCreateState`
