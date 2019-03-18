
combinate
==============================================

Purpose
----------------

Computes combinations of  N things taken  K at a time.

Format
----------------
.. function:: combinate(N,  K)

    :param N: scalar.
    :type N: TODO

    :param K: scalar.
    :type K: TODO

    :returns: y (*MxK matrix*), where M is the number of combinations of  N things taken  K at a time.

Examples
----------------

::

    //Calculate all combinations of 4 items chosen 2 at a time
    n = 4;
    k = 2;
    y = combinate(n,k);
     
    print y;

The code above will create the following output:

::

    1.0000 2.0000
     1.0000 3.0000
     1.0000 4.0000
     2.0000 3.0000
     2.0000 4.0000
     3.0000 4.0000

.. seealso:: Functions :func:`combinated`, :func:`numCombinations`

combination n choose k
