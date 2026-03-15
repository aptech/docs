
rndvm
==============================================

Purpose
----------------

Computes von Mises pseudo-random numbers.

Format
----------------
.. function:: x = rndvm(r, c, m, k)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param m: ExE conformable with r x c, means for von Mises distribution.
    :type m: NxK matrix

    :param k: ExE conformable with r x c, shape argument for von Mises distribution.
    :type k: LxM matrix

    :return x: von Mises distributed random numbers.

    :rtype x: RxC matrix

Examples
----------------

::

    // Generate a 3x2 matrix of von Mises
    // random numbers with mean = pi, shape = 2
    x = rndvm(3, 2, 3.14, 2);
    print x;

Source
------

random.src

