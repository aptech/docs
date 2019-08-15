
meanc
==============================================

Purpose
----------------

Computes the mean of every column of a matrix.

Format
----------------
.. function:: y = meanc(x)

    :param x: data
    :type x: NxK matrix

    :return y: containing the mean of every column of *x*.

    :rtype y: Kx1 matrix

Examples
----------------

::

    x = meanc(rndu(1e5,4));

After the code above, *x* is equal to:

::

    0.5007
    0.5004
    0.4995
    0.5016

In this example, 4 columns of uniform random numbers are generated in
a matrix, and the mean is computed for each column. Due to the use of random input data
in this example, your results may differ slightly.

.. seealso:: Functions :func:`stdc`

