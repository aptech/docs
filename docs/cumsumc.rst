
cumsumc
==============================================

Purpose
----------------

Computes the cumulative sums of the columns of a matrix.

Format
----------------
.. function:: y = cumsumc(x)

    :param x:
    :type x: NxK matrix

    :return y: containing the cumulative sums of the columns of *x*.

    :rtype y: NxK matrix

Examples
----------------

::

    x = { 1 -3,
          2  2,
          3 -1 };

    y = cumsumc(x);

Now if you view *y*, you will see:

::

        1.000 -3.000
    y = 3.000 -1.000
        6.000 -2.000

Remarks
-------

This is based on the recursive series function :func:`recserar`. :func:`recserar` could
be called directly as follows:

::

    recserar(x, x[1, .], ones(1, cols(x)))

to accomplish the same thing.


Source
------------

cumsumc.src

.. seealso:: Functions :func:`cumprodc`, :func:`recsercp`, :func:`recserar`
