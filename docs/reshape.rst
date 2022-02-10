
reshape
==============================================

Purpose
----------------
Reshapes a dataframe, matrix or string array.

Format
----------------
.. function:: y = reshape(x, r [, c])

    :param x: data
    :type x: NxK matrix

    :param r: new row dimension. If -1 is passed in, the row dimension will be inferred based on the size of the input data and the column dimension.
    :type r: scalar

    :param c: Optional input, new column dimension. If ``c`` is not passed in a default value of 1 will be used. If -1 is passed in, the column dimension will be inferred based on the size of the input data and the row dimension. 
    :type c: scalar

    :return y: created from the elements of *x*.

    :rtype y: RxC matrix

Examples
----------------

Repeating a scalar element
+++++++++++++++++++++++++++++

::

    // Create a 3x1 vector of 5's
    x = reshape(5, 3);


After the above code, ``x`` will equal:

::

    5
    5
    5

::

    // Create a 1x4 row vector of 5's
    x = reshape(5, 1, 4);

After the above code, ``x`` will equal:

::

    5   5   5   5


Examples with a -1 row or column input
++++++++++++++++++++++++++++++++++++++++++


::

    // Create a 3x4 matrix
    x = { 1  2  3  4,
          5  6  7  8,
          9 10 11 12 };

    y = reshape(x, 2, -1);

After the above code, ``y`` will equal:

::

    1   2   3    4    5    6
    7   8   9   10   11   12


Continuing with the ``x`` from above:

::

    y = reshape(x, -1, 3);

::
 
     1    2    3
     4    5    6
     7    8    9   
    10   11   12


Other basic examples
++++++++++++++++++++++

::

    y = reshape(x, 2, 6);

::

            1  2  3  4
    if x =  5  6  7  8  then y = 1  2  3  4  5  6
            9 10 11 12           7  8  9 10 11 12

::

            1  2  3
    if x =  4  5  6  then y = 1  2  3  4  5  6
            7  8  9           7  8  9  1  2  3

::

            1  2  3  4  5
    if x =  6  7  8  9 10  then y = 1  2  3  4  5  6
           11 12 13 14 15           7  8  9 10 11 12

::

    if x = 1  2  then y = 1 2 3 4 1 2
           3  4           3 4 1 2 3 4

::

    if x = 1  then y = 1 1 1 1 1 1
                       1 1 1 1 1 1

Remarks
-------

Matrices (as well as dataframes and string arrays) are stored in row major order.

The first *c* elements are put into the first row of *y*, the second in the
second row, and so on. If there are more elements in *x* than in *y*, the
remaining elements are discarded. If there are not enough elements in *x*
to fill *y*, then when reshape runs out of elements, it goes back to the
first element of *x* and starts getting additional elements from there.


.. seealso:: Functions :func:`submat`, :func:`vec`
