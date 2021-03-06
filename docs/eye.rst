
eye
==============================================

Purpose
----------------

Creates an identity matrix.

Format
----------------
.. function:: y = eye(n)

    :param n: size of identity matrix to be created.
    :type n: scalar

    :return y: identity matrix, containing 1's down the diagonal and 0's everywhere else.

    :rtype y: NxN identity matrix

Examples
----------------

::

    x = eye(3);

The code above assigns *x* to be equal to:

::

    1.0000 0.0000 0.0000
    0.0000 1.0000 0.0000
    0.0000 0.0000 1.0000

Remarks
-------

If *n* is not an integer it will be truncated to an integer.

.. seealso:: Functions :func:`zeros`, :func:`ones`
