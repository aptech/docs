
sumr
==============================================

Purpose
----------------
Computes the sum of each row of a matrix or the sum of the fastest moving dimension of an L-dimensional array.

Format
----------------
.. function:: y = sumr(x)

    :param x:  data matrix where the last two dimensions are NxK
    :type x: NxK matrix or L-dimensional array

    :return y: contains the sum of each row. The last two dimensions are Nx1.

    :rtype y: Nx1 vector or L-dimensional array

Examples
----------------

::

    // Create an additive sequence from 1-12 and reshape it into
    // a 3x4 matrix
    x = reshape(seqa(1, 1, 12), 3, 4);

    // Sum the rows
    y = sumr(x);

After the above code, the variables ``x`` and ``y`` will be:

::

        1  2  3  4        10
    x = 5  6  7  8   y =  26
        9 10 11 12        42

::

    // Reshape an additive sequence from 1-24 into a 2x3x4
    // dimensional array
    a = areshape(seqa(1, 1, 24), 2|3|4);
    z = sumr(a);

``a`` is a 2x3x4 array such that:

::

    Plane [1,.,.]

          1.0000000     2.0000000     3.0000000     4.0000000
          5.0000000     6.0000000     7.0000000     8.0000000
          9.0000000     10.000000     11.000000     12.000000

    Plane [2,.,.]

          13.000000     14.000000     15.000000     16.000000
          17.000000     18.000000     19.000000     20.000000
          21.000000     22.000000     23.000000     24.000000

The variable ``z`` is equal to:

::

    Plane [1,.,.]

          10.000000
          26.000000
          42.000000

    Plane [2,.,.]

          58.000000
          74.000000
          90.000000

.. seealso:: Functions :func:`sumc`
