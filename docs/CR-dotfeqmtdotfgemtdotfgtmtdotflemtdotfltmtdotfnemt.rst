
dotfeqmt,dotfgemt,dotfgtmt,dotflemt,dotfltmt,dotfnemt
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions
use the fcmptol argument to fuzz the comparison operations to allow for
roundoff error.

Format
----------------
.. function:: dotfnemt(a,  b,  fcmptol)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with  a.
    :type b: LxM matrix

    :param fcmptol: comparison tolerance.
    :type fcmptol: scalar

    :returns: y (*TODO*), max(N,L) by max(K,M) matrix of 1's and 0's.

Examples
----------------

::

    x = rndu(2,2);
    y = x;
    y[1,1] = y[1,1] + 0.00000002;
    t = dotfgemt(x,y,1e-15);

::

    t = 0 1   x-y = -2e-8   0
        1 1             0   0

Source
++++++

fcomparemt.src

.. seealso:: Functions 
