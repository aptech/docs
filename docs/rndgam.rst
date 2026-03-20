
rndgam
==============================================

Purpose
----------------

Computes pseudo-random numbers with gamma distribution.

.. NOTE:: :func:`rndgam` is deprecated and should be replaced with :func:`rndGamma`.

Format
----------------
.. function:: x = rndgam(r, c, alpha)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param alpha: ExE conformable with r x c resulting matrix, shape parameters for gamma distribution.
    :type alpha: MxN matrix

    :return x: gamma distributed pseudo-random numbers.

    :rtype x: r x c matrix

Remarks
-------

The properties of the pseudo-random numbers in *x* are:


.. math::

   E(x) = \alpha\\
   Var(x) = \alpha\\
    x > 0\\
    \alpha > 0

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Generate a 3x2 matrix of gamma
    // random numbers with shape = 5
    x = rndgam(3, 2, 5);
    print x;

After the code above, *x* is:

::

       4.3270396        9.4093462
       3.9689646        4.7393241
       6.1082705        5.6436564

Source
------

random.src

.. seealso:: Functions :func:`rndGamma`
