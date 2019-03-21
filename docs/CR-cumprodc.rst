
cumprodc
==============================================

Purpose
----------------

Computes the cumulative products of the columns of a matrix.

Format
----------------
.. function:: cumprodc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*NxK matrix*) containing the cumulative products of the columns of *x*.

Remarks
-------

This is based on the recursive series :func:`recsercp`. :func:`recsercp` could be called
directly as follows:

::

   recsercp(x, zeros(1,cols(x)));

to accomplish the same thing.

Examples
----------------

::
:func:`
    x` = { 1 -3,
          2  2,
          3 -1 };
    y = cumprodc(x);

Now if you view *y*, you will see:

::

    1.000 -3.000 
    y = 2.000 -6.000 
        6.000  6.000

Source
------------

cumprodc.src

.. seealso:: Functions :func:`cumsumc`, :func:`recsercp`, :func:`recserar`

