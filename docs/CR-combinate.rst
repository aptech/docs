
combinate
==============================================

Purpose
----------------

Computes combinations of *N* things taken *K* at a time.

Format
----------------
.. function:: combinate(N, K)

    :param N: scalar.
    :type N: scalar

    :param K: 
    :type K: scalar

    :returns: y (*MxK matrix*), where :math:`M` is the number of combinations of *N* things taken *K* at a time.

Remarks
-------

"Things" are represented by a sequence of integers from 1 to *N*, and the
integers in each row of *y* are the combinations of those integers taken *K*
at a time.

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

