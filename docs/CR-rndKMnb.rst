
rndKMnb
==============================================

Purpose
----------------

Computes negative binomial pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMnb(r, c, k, p, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param k: r x c matrix or rx1 vector, or 1xc vector, or scalar, "event" argument for negative binomial distribution.
    :type k: matrix or vector or scalar

    :param p: r x c matrix or rx1 vector, or 1xc vector, or scalar, "probability" argument for negative binomial distribution.
    :type p: matrix or vector or scalar

    :param state: 

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**
        
            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :returns: x (*RxC matrix*), negative binomial distributed random numbers.

    :returns: newstate (*500x1 vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = (k * p)/(1 - p)

   Var(x) = (k * p)/(1 - p)2x = 0, 1,....k > 00 < p < 1

*r* and *c* will be truncated to integers if necessary.

Technical Notes
---------------
:func:`rndKMnb` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src

