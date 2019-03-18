
ceil
==============================================

Purpose
----------------

Round up toward +∞.

Format
----------------
.. function:: ceil(x)

    :param x: NxK matrix.
    :type x: TODO

    :returns: y (*TODO*), NxK matrix.

Examples
----------------

::

    x = 10*rndn(2,2);
    y = ceil(x);

After the code above, the matrices x and y should hold values similar to below. Answers will vary due to the use of random numbers as the input to the ceil function.

::

    x = 8.73383  -0.783488  y = 9.0000000  0.0000000
        13.1106   7.155113      14.000000  8.0000000

.. seealso:: Functions :func:`floor`, :func:`trunc`
