
rndKMvm
==============================================

Purpose
----------------

Computes von Mises pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMvm(r, c, m, k, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param m: means for von Mises distribution, scalar or ExE conformable matrix with *r* and *c*.
    :type m: matrix, vector or scalar

    :param k: shape argument for von Mises distribution, scalar or ExE conformable matrix with *r* and *c*.
    :type k: matrix, vector or scalar

    :param state:

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**

            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :return x: von Mises distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: 500x1 vector

Remarks
-------

*r* and *c* will be truncated to integers if necessary.

Examples
----------------

::

    // Generate a 3x2 matrix of von Mises
    // random numbers with mean = pi, shape = 2
    // using a fixed seed for repeatable output
    { x, newstate } = rndKMvm(3, 2, 3.14, 2, 12345);
    print x;

The output is a 3x2 matrix of von Mises distributed values centered near the mean of 3.14 (pi):

::

      -1.9497965       -1.6210254
      -3.0063623       -2.2778588
       2.6152190        2.6730616

Technical Notes
---------------
:func:`rndKMvm` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src
