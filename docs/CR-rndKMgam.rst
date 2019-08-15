
rndKMgam
==============================================

Purpose
----------------

Computes Gamma pseudo-random numbers.

Format
----------------
.. function:: { x, newstate } = rndKMgam(r, c, alpha, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: r x c matrix or rx1 vector, or 1xc vector, or scalar, shape argument for gamma distribution.
    :type alpha: matrix or vector or scalar

    :param state: 

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **500x1 vector case**
        
            *state* = the state vector returned from a previous call to one of the ``rndKM`` random number functions.

    :type state: scalar or 500x1 vector

    :return x: gamma distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: 500x1 vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = alphaVar(x) = alphax > 0alpha > 0

To generate ``gamma(alpha, theta)`` pseudo-random numbers where *theta* is a
scale parameter, multiply the result of :func:`rndKMgam` by theta.

Thus

::

   z =  theta * rndgam(1,1, alpha);

has the properties

.. math::

   E(z) = alpha * thetaVar(z) = alpha * theta2z > 0alpha > 0theta > 0

*r* and *c* will be truncated to integers if necessary.

Technical Notes
---------------
:func:`rndKMgam` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src

