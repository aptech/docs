
feq, fge, fgt, fle, flt, fne
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use `_fcmptol` to fuzz the comparison operations to allow for roundoff error.

Format
----------------
.. function:: ret = feq(a, b)
              ret = fge(a, b)
              ret = fgt(a, b)
              ret = fle(a, b)
              ret = flt(a, b)
              ret = fne(a, b)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :return ret: returns 1 if ``TRUE``  and 0  if ``FALSE``.

    :rtype ret: scalar

Global Input
------------

.. data::  \_fcmptol

    scalar, comparison tolerance. The default value is 1.0e-15.


Examples
----------------

Example 1: Fuzzy equality
++++++++++++++++++++++++++

::

    _fcmptol = 1e-12;

    ret = feq(2, 2 + 1e-13);

The above code will set *ret* equal to 1, because 2 and (2 + 1e-13) differ by less than the value of ``_fcmptol``, which is 1e-12.

Example 2: Fuzzy greater than
++++++++++++++++++++++++++++++

::

   _fcmptol = 1e-10;

   a = 0.5;
   b = a + 1e-5;
   c = a + 1e-11; 

   ret_1 = fgt(b, a);

   ret_2 = fgt(c, a);

After the code above:

::

    ret_1 = 1
    ret_2 = 0

Remarks
-------

The return value is ``TRUE`` if every comparison is ``TRUE``.

The statement:

::

   ret = feq(a, b);

is equivalent to:

::

   ret = abs(a-b) <= _fcmptol;

For the sake of efficiency, these functions are not written to handle
missing values. If *a* and *b* contain missing values, use :func:`missrv` to convert
the missing values to something appropriate before calling a fuzzy
comparison function.

The calling program can reset `\_fcmptol` before calling these procedures:

::

   _fcmptol = 1e-12;


Source
------

fcompare.src

.. seealso:: Functions :func:`dotfeq`, :func:`dotfge`, :func:`dotfgt`, :func:`dotfle`, :func:`dotflt`, :func:`dotfne`
