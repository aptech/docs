
rndKMu
==============================================

Purpose
----------------
Returns a matrix of uniform (pseudo) random variables and the state of the random number generator.

Format
----------------
.. function:: { y, newstate } = rndKMu(r, c, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param state:

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.


        **500x1 vector case**

            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or vector

    :return y: of uniform random numbers, :math:`0 \leq y < 1`.

    :rtype y: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: 500x1 vector

Examples
----------------
This example generates two thousand vectors of uniform random
numbers, each with one million elements. The state of the random
number generator after each iteration is used as an input to the
next generation of random numbers.

::

    state = 13;
    n = 2000;
    k = 1000000;
    c = 0;
    submean = {};

    do while c < n;
       { y, state } = rndKMu(k, 1, state);
       submean = submean | meanc(y);
       c = c + k;
    endo;

    mean = meanc(submean);
    print 0.5-mean;

Remarks
-------

*r* and *c* will be truncated to integers if necessary.

Technical Notes
-----------------

:func:`rndKMu` uses the recur-with-carry KISS-Monster algorithm described in the
:func:`rndKMi` Technical Notes. Random integer seeds from :math:`0` to :math:`2^{32}-1` are
generated. Each integer is divided by :math:`2^{32}` or :math:`2^{32}-1`.

.. seealso:: Functions :func:`rndKMn`, :func:`rndKMi`
