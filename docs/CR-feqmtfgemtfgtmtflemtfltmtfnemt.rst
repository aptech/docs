
feqmt, fgemt, fgtmt, flemt, fltmt, fnemt
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use the *fcmptol* argument to fuzz the comparison operations to allow
for roundoff error.

Format
----------------
.. function:: y = feqmt(a, b, fcmptol)
              y = fgemt(a, b, fcmptol)
              y = fgtmt(a, b, fcmptol)
              y = flemt(a, b, fcmptol)
              y = fltmt(a, b, fcmptol)
              y = fnemt(a, b, fcmptol)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :param fcmptol: comparison tolerance.
    :type fcmptol: scalar

    :return ret: returns 1 if ``TRUE`` and 0 if ``FALSE``.

    :rtype ret: scalar

Remarks
-------

The return value is ``TRUE`` if every comparison is ``TRUE``.

The statement:

::

   ret = feqmt(a, b, 1e-15);

is equivalent to:

::

   ret = abs(a-b) <= 1e-15;

For the sake of efficiency, these functions are not written to handle
missing values. If *a* and *b* contain missing values, use :func:`missrv` to convert
the missing values to something appropriate before calling a fuzzy
comparison function.

Examples
----------------

Example 1: Fuzzy equality
++++++++++++++++++++++++++

::

    tol = 1e-12;

    ret = feqmt(2, 2 + 1e-13, tol);

The above code will set *ret* equal to 1, because 2 and (2 + 1e-13) differ by less than the value of ``tol``, which is 1e-12.

Example 2: Fuzzy greater than
++++++++++++++++++++++++++++++

::

   tol = 1e-10;

   a = 0.5;
   b = a + 1e-5;
   c = a + 1e-11; 

   ret_1 = fgtmt(b, a, tol);

   ret_2 = fgtmt(c, a, tol);

After the code above:

::

    ret_1 = 1
    ret_2 = 0


Source
------

fcomparemt.src

.. seealso:: Functions :func:`dotfeqmt`, :func:`dotfgemt`, :func:`dotfgtme`, :func:`dotflemt`, :func:`dotfltmt`, :func:`dotfnemt`
