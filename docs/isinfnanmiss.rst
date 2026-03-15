
isinfnanmiss
==============================================

Purpose
----------------

Returns true if the argument contains an infinity, NaN, or missing value.

Format
----------------
.. function:: y = isinfnanmiss(x)

    :param x: data
    :type x: NxK matrix

    :return y: 1 if *x* contains any infinities, NaNs, or missing values, else 0.

    :rtype y: scalar

Examples
----------------

::

    // Matrix with no special values
    x = { 1 2, 3 4 };
    print (isinfnanmiss(x));

    // Matrix with a missing value
    x = { 1 2, 3 . };
    print (isinfnanmiss(x));

The code above produces the following output:

::

    0.0000000
    1.0000000

.. seealso:: Functions :func:`scalinfnanmiss`, :func:`ismiss`, :func:`scalmiss`
