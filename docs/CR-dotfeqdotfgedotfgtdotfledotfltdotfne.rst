
dotfeq, dotfge, dotfgt, dotfle, dotflt, dotfne
==============================================

Purpose
----------------

Fuzzy comparison functions. These functions use `_fcmptol` to fuzz the comparison operations to allow for
roundoff error.

Format
----------------
.. function:: dotfeq(a, b)
              dotfge(a, b)
              dotfgt(a, b)
              dotfle(a, b)
              dotflt(a, b)
              dotfne(a, b)

    :param a: first matrix.
    :type a: NxK matrix

    :param b: second matrix, ExE compatible with *a*.
    :type b: LxM matrix

    :returns: **y** (*max(N,L) by max(K,M)*) - matrix of 1's and 0's.

Global Input
------------

.. data:: \_fcmptol

    scalar, comparison tolerance. The default value is 1.0e-15.

Remarks
-------

The return value is 1 if ``TRUE`` and 0 if ``FALSE``.

The statement:

::

   y = dotfeq(a, b);

is equivalent to:

::

   // Is the absolute difference between the
   // corresponding elements of 'a' and 'b' 
   // less than or equal to '_fcmptol'?
   y = abs(a - b) .<= _fcmptol;

The calling program can reset `_fcmptol` before calling these procedures. For example:

::

   _fcmptol = 1e-12;


Examples
----------------

::

    x = pi * ones(2, 2);
    y = x;

    y[1,1] = pi + 1e-14;
    y[1,2] = pi + 3e-16;

    // Test for elements where 'x' is > 'y'
    t = dotfge(x, y);

If `_fcmptol` is equal to `1e-15`, then

::

    t = 0.00 1.00
        1.00 1.00

Continuing with the data above:

::

    // Test for elements where 'x' is < 'y '
    t = dotflt(x, y);

::

    t = 1.00 0.00
        0.00 0.00

Source
------

fcompare.src

.. seealso:: Functions :func:`feq-fne`
