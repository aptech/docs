
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

Examples
----------------

::

    // Generate a 3x2 matrix of beta random numbers
    // with shape parameters a = 2, b = 5
    // using a fixed seed for repeatable output
    { x, newstate } = rndKMbeta(3, 2, 2, 5, 12345);
    print x;

The output is a 3x2 matrix of beta-distributed values between 0 and 1. The sample mean is approximately 0.29, consistent with the theoretical mean of a/(a+b) = 2/7:

::

      0.19288089       0.38057594
      0.51686669       0.57522795
      0.31832075       0.14046662

Technical Notes
---------------
:func:`rndKMbeta` uses the recur-with-carry KISS+Monster algorithm described in the :func:`rndKMi` Technical Notes.

Source
------

randkm.src
