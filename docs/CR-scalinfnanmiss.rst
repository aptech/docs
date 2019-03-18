
scalinfnanmiss
==============================================

Purpose
----------------

Returns true if the argument is a scalar infinity, NaN, or missing value.

Format
----------------
.. function:: scalinfnanmiss(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*scalar*), 1 if x is a scalar, infinity, NaN, or missing value, else 0.

Examples
----------------

::

    //Create an infinity
    x = 1/0;
    
    if scalInfNanMiss(x);
       print "x = " x;
    else;
       print "x is Not: a Nan, Infinity, or Missing";
    endif;

.. seealso:: Functions :func:`isinfnanmiss`, :func:`ismiss`, :func:`scalmiss`
