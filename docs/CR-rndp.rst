
rndp
==============================================

Purpose
----------------

Computes pseudo-random numbers with Poisson distribution.

Format
----------------
.. function:: rndp(r, c, lambda)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param lambda: ExE conformable with r x c resulting matrix, shape parameters for Poisson distribution.
    :type lambda: MxN matrix

    :returns: x (*r x c matrix*), Poisson distributed pseudo-random numbers.



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

Source
------

random.src

