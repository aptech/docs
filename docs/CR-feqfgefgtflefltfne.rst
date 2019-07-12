
feq, fge, fgt, fle, flt, fne
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use `_fcmptol` to fuzz the comparison operations to allow for roundoff error.

Format
----------------
.. function:: feq(a, b)
              fge(a, b)
              fgt(a, b)
              fle(a, b)
              flt(a, b)
              fne(a, b)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :returns: **ret** (*scalar*) - returns 1 if ``TRUE``  and 0  if ``FALSE``.

Global Input
------------

.. data::  \_fcmptol

    scalar, comparison tolerance. The default value is 1.0e-15.


Remarks
-------

The return value is ``TRUE`` if every comparison is ``TRUE``.

The statement:

::

   y = feq(a, b);

is equivalent to:

::

   y = a eq b;

For the sake of efficiency, these functions are not written to handle
missing values. If *a* and *b* contain missing values, use :func:`missrv` to convert
the missing values to something appropriate before calling a fuzzy
comparison function.

The calling program can reset `\_fcmptol` before calling these procedures:

::

   _fcmptol = 1e-12;


Examples
----------------

::

    _fcmptol = 1e-12;

    a = rndu(2, 2);

    b = a + 0.5*(_fcmptol);

    if fge(a, b);
       print "each element of a is greater than";
       print "or equal to each element of b";
    else;
       print "at least one element of a is less";
       print "its corresponding element in b";
    endif;

Source
------

fcompare.src

.. seealso:: Functions :func:`dotfeq`, :func:`dotfge`, :func:`dotfgt`, :func:`dotfle`, :func:`dotflt`, :func:`dotfne`
