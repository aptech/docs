
rndWishart
==============================================

Purpose
----------------

Computes Wishart distributed random numbers given a scale matrix.

Format
----------------
.. function:: r = rndWishart(num, scale, df)
              { r, newstate } = rndWishart(num, scale, df, state)

    :param num: number of Wishart random matrices to create.
    :type num: scalar

    :param scale: NxM scale matrix. The draws average *df* times *scale*.
    :type scale: matrix

    :param df: degrees of freedom.
    :type df: scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

            *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return r: Wishart random matrices.

    :rtype r: num * rows(scale) x N matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // scale matrix
    scale = {  1   0.5,
             0.5     1 };

    // degrees of freedom
    df = 7;

    X = rndWishart(1, scale, df);
    print X;

::

       4.8754749        2.4840462
       2.4840462        5.3526816

Remarks
-------

The properties of the pseudo-random numbers in *X* are:

.. math::

   E(X) = df * scale\\

   Var(X_{ij}) = df * (scale_{ij}^2 + scale_{ii}*scale_{jj})


.. seealso:: Functions :func:`rndWishartInv`, :func:`rndMVn`, :func:`rndCreateState`
