
rndStateSkip
==============================================

Purpose
----------------

To advance a state vector by a specified number of values.

Format
----------------
.. function:: newState = rndStateSkip(n_skip, state)

    :param n_skip: the number of values to skip, 0 or more. Negative values are not supported; the result differs by platform and generator.
    :type n_skip: scalar

    :param state: opaque state vector
    :type state: vector

    :return newState: the advanced state.

    :rtype newState: Opaque vector

Examples
----------------

::

    seed = 9192834;

    // Create a state from the 118th substream of the
    // Wichmann-Hill RNG
    state = rndCreateState("wh-118", seed);

    // Create a new state that is advanced by 2 numbers.
    newState = rndStateSkip(2, state);

    // Create and compare numbers from the two state vectors
    { r, state } = rndu(4, 1, state );
    { r2, newState } = rndu(2, 1, newState);

::

         0.54973563
    r =  0.81642451
         0.68583300
         0.09105558

    r2 = 0.68583300
         0.09105558

Technical Notes
---------------

This function works with every generator except MT2203, for which it stops with error G0645. On macOS with Apple silicon, it works with the generators available there: SFMT19937, MT19937 and MRG32k3a. Each skip gives the same numbers as on Windows and Linux. With SFMT19937 and MT19937, a skip there takes time in proportion to its length, up to about 0.4 seconds for each 10\ :sup:`9` values skipped. For large skips use MRG32k3a, whose skips take no noticeable time. The example above uses Wichmann-Hill, which is not available on Apple silicon.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndn`, :func:`rndu`, :func:`rndBeta`, :func:`rndGamma`
