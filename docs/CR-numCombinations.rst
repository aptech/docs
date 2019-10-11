
numCombinations
==============================================

Purpose
----------------

Computes number of combinations of *n* things taken *k* at a time.

Format
----------------
.. function:: y = numCombinations(n, k)

    :param n: 
    :type n: scalar

    :param k: 
    :type k: scalar

    :return y: number of combinations of *n* things take *k* at a time.

    :rtype y: scalar

Examples
----------------

::

    y = numCombinations(25,5);
     
    print y;

The code above, returns:

::

    53130.0000

Remarks
-------

To calculate all of the combinations, use the function :func:`combinate`.


.. seealso:: Functions :func:`combinate`, :func:`combinated`

