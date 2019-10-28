
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

Technical Notes
---------------
:func:`rndKMvm` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src
