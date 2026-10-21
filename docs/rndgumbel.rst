
rndGumbel
==============================================

Purpose
----------------

Computes Gumbel distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndGumbel(r, c, loc, scale)
              { x, newstate } = rndGumbel(r, c, loc, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param loc: location parameter, scalar or ExE conformable matrix with *r* and *c*
    :type loc: scalar or matrix

    :param scale: scaler parameter, scalar or ExE conformable matrix with *r* and *c*
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: Gumbel distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

This function uses the definition of the Gumbel distribution
corresponding to the minimum extreme. The properties of the
pseudo-random numbers in *y* are:

.. math::

   E(y) = loc - \gamma*scale \approx\\
   loc - 0.5772*scale\\
   \gamma = \text{Euler-Mascheroni constant}\\
   Var(y) = \frac{(\pi*scale)^2}{6}

*r* and *c* will be truncated to integers if necessary.

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Generate a 3x2 matrix of Gumbel
    // random numbers with location = 0, scale = 1
    x = rndGumbel(3, 2, 0, 1);
    print x;

After the code above, *x* is:

::

      -2.3025980      -0.21222789
      -1.3054204       0.71538115
     -0.39450916        1.0224755

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
