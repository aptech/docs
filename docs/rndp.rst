
rndp
==============================================

Purpose
----------------

Computes pseudo-random numbers with Poisson distribution.

Format
----------------
.. function:: x = rndp(r, c, lambda)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param lambda: ExE conformable with r x c resulting matrix, shape parameters for Poisson distribution.
    :type lambda: MxN matrix

    :return x: Poisson distributed pseudo-random numbers.

    :rtype x: r x c matrix

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

+--------------+---+-----------+
| *E(x)*       | = | *lambda*  |
+--------------+---+-----------+
| *Var(x)*     | = | *lambda*  |
+--------------+---+-----------+
| *x*          | = | 0,1,2,... |
+--------------+---+-----------+
| *lambda*     | > | 0         |
+--------------+---+-----------+

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Generate a 3x2 matrix of Poisson
    // random numbers with lambda = 5
    x = rndp(3, 2, 5);
    print x;

After the code above, *x* is:

::

       1.0000000        1.0000000
       5.0000000        6.0000000
       8.0000000        2.0000000

Source
------

random.src

