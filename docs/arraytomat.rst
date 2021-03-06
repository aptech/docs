
arraytomat
==============================================

Purpose
----------------

Converts an array to type matrix.

Format
----------------
.. function:: y = arraytomat(a)

    :param a: 
    :type a: N-dimensional array

    :return y: where *L* is the size of the fastest moving dimension of the array and *K* is the size of the second fastest moving dimension.

    :rtype y: KxL or 1xL matrix or scalar

Examples
----------------

::

    /*
    ** Create 25x1 vector containing the sequence 0.5, 1,
    ** 1.5...12.5
    */
    x = seqa(0.5, 0.5, 25);
    
    /*
    ** Reshape into a 1x6x4 array, discarding the 25th element
    ** of 'x'
    */
    a = areshape(x, 1|6|4);
    
    /*
    **  Set 'y' to be a 6x4 variable of type matrix, with the
    ** same contents as 'a'
    */
    y = arraytomat(a);

The code above sets *y* equal to:

::

     0.5    1.0    1.5    2.0
     2.5    3.0    3.5    4.0
     4.5    5.0    5.5    6.0
     6.5    7.0    7.5    8.0
     8.5    9.0    9.5   10.0
    10.5   11.0   11.5   12.0

Remarks
-------

:func:`arraytomat` will take an array of 1 or 2 dimensions or an N-dimensional
array, in which the N-2 slowest moving dimensions each have a size of 1.

.. seealso:: Functions :func:`mattoarray`

