
rndKMbeta
==============================================

Purpose
----------------
Computes beta pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMbeta(r, c, a, b, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param a: First shape argument for beta distribution. ExE conformable with the row and column dimensions of the return matrix, *r* and *c*.
    :type a: matrix or vector or scalar

    :param b: Second shape argument for beta distribution. ExE conformable with the row and column dimensions of the return matrix, *r* and *c*.
    :type b: matrix or vector or scalar

    :param state:

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**

            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :return x: Beta distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: 500x1 vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = \frac{a}{a+b}\\

   Var(x) = \frac{a*b}{(a+b+1)*(a+b^2)}\\

   0 < x < 1\\

   a > 0\\

   b > 0

*r* and *c* will be truncated to integers if necessary.

Technical Notes
---------------
:func:`rndKMbeta` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src
