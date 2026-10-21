
rndCauchy
==============================================

Purpose
----------------

Computes Cauchy random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndCauchy(r, c, loc, scale)
              { x, newstate } = rndCauchy(r, c, loc, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param loc: Cauchy location parameter, scalar or ExE conformable matrix with *r* and *c*
    :type loc: scalar or matrix

    :param scale: Cauchy scale parameter, scalar or ExE conformable matrix with *r* and *c*
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: Cauchy distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = \text{undefined} \\
   Var(x) = \text{undefined} \\
   Median(x) = \text{loc}

*r* and *c* will be truncated to integers if necessary.

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Generate a 3x1 vector of standard Cauchy random numbers
    // with location = 0 and scale = 1
    x = rndCauchy(3, 1, 0, 1);
    print x;

After the code above, *x* is:

::

       3.2446955
     -0.17323020
       1.0822839

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
