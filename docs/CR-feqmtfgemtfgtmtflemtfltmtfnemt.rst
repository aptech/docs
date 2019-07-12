
feqmt, fgemt, fgtmt, flemt, fltmt, fnemt
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use the *fcmptol* argument to fuzz the comparison operations to allow
for roundoff error.

Format
----------------
.. function:: feqmt(a, b, fcmptol)
              fgemt(a, b, fcmptol)
              fgtmt(a, b, fcmptol)
              flemt(a, b, fcmptol)
              fltmt(a, b, fcmptol)
              fnemt(a, b, fcmptol)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :param fcmptol: comparison tolerance.
    :type fcmptol: scalar

    :returns: **ret** (*scalar*) - returns 1 if ``TRUE``  and 0  if ``FALSE``.

Remarks
-------

The return value is ``TRUE`` if every comparison is ``TRUE``.

The statement:

::

   y = feqmt(a, b, 1e-15);

is equivalent to:

::

   y = a eq b;

For the sake of efficiency, these functions are not written to handle
missing values. If *a* and *b* contain missing values, use :func:`missrv` to convert
the missing values to something appropriate before calling a fuzzy
comparison function.


Examples
----------------

::

    tol = 1e-12;

    a = rndu(2, 2);

    b = a + 0.5*(tol);

    if fgemt(a, b, tol);
       print "each element of a is greater than";
       print "or equal to each element of b";
    else;
       print "at least one element of a is less";
       print "its corresponding element in b";
    endif;

Source
------

fcomparemt.src

.. seealso:: Functions :func:`dotfeqmt`, :func:`dotfgemt`, :func:`dotfgtme`, :func:`dotflemt`, :func:`dotfltmt`, :func:`dotfnemt`
