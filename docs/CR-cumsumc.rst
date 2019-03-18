
cumsumc
==============================================

Purpose
----------------

Computes the cumulative sums of the columns of a matrix.

Format
----------------
.. function:: cumsumc(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*TODO*), NxK matrix containing the cumulative sums of the
        columns of x.

Examples
----------------

::

    x = { 1 -3,
          2  2,
          3 -1 };
    
    y = cumsumc(x);

Now if you view y, you will see:

::

    1.000 -3.000 
    y = 3.000 -1.000 
        6.000 -2.000

Source
++++++

cumsumc.src

.. seealso:: Functions :func:`cumprodc`, :func:`recsercp`, :func:`recserar`
