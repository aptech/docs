
dotfeqmt, dotfgemt, dotfgtmt, dotflemt, dotfltmt, dotfnemt
===========================================================

Purpose
----------------

Fuzzy comparison functions. These functions
use the *fcmptol* argument to fuzz the comparison operations to allow for
roundoff error.

Format
----------------
.. function:: y = dotfeqmt(a, b, fcmptol)
              y = dotfgemt(a, b, fcmptol)
              y = dotfgtme(a, b, fcmptol)
              y = dotflemt(a, b, fcmptol)
              y = dotfltmt(a, b, fcmptol)
              y = dotfnemt(a, b, fcmptol)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :param fcmptol: comparison tolerance.
    :type fcmptol: scalar

    :return y: matrix of 1's and 0's.

    :type y: max(N,L) by max(K,M)

Remarks
-------

The return value is 1 if ``TRUE`` and 0 if ``FALSE``.

The statement:

::

   y = dotfeqmt(a, b, 1e-13);

is equivalent to:

::

   y = abs(a-b) .<= 1e-13;


Examples
----------------

::

    // Create x matrix
    x = rndu(2, 2);

    // Create y matrix
    y = x;
    y[1, 1] = y[1, 1] + 0.00000002;

    t = dotfgemt(x,y,1e-15);

::

    t = 0 1   x-y = -2e-8   0
        1 1             0   0

Source
------

fcomparemt.src

.. seealso:: Functions :func:`feqmt`, :func:`fgemt`, :func:`flemt`, :func:`fltmt`, :func:`fnemt`
