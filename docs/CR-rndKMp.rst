
rndKMp
==============================================

Purpose
----------------
Computes Poisson pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMp(r, c, lambda, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param lambda: r x c matrix or r x 1 vector, or 1 x c vector, or scalar, shape argument for Poisson distribution.
    :type lambda: matrix or vector or scalar

    :param state: 

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**
        
            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :return x: Poisson distributed random numbers.

    :type x: RxC matrix

    :return newstate: the updated state.

    :type newstate: 500x1 vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) =  lambda
   
   Var(x) =  lambdax  =  0, 1,....lambda  >  0

*r* and *c* will be truncated to integers if necessary.

Technical Notes
---------------
:func:`rndKMp` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src

