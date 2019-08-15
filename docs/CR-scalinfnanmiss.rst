
scalinfnanmiss
==============================================

Purpose
----------------

Returns true if the argument is a scalar infinity, NaN, or missing value.

Format
----------------
.. function:: y = scalinfnanmiss(x)

    :param x: data
    :type x: NxK matrix

    :return y: 1 if x is a scalar, infinity, NaN, or missing value, else 0.

    :rtype y: scalar

Examples
----------------

::

    // Create an infinity
    x = 1/0;
    
    if scalInfNanMiss(x);
       print "x = " x;
    else;
       print "x is Not: a Nan, Infinity, or Missing";
    endif;

.. seealso:: Functions :func:`isinfnanmiss`, :func:`ismiss`, :func:`scalmiss`

