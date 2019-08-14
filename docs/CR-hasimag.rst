
hasimag
==============================================

Purpose
----------------

Tests whether the imaginary part of a complex matrix is negligible.

Format
----------------
.. function:: hasimag(x)

    :param x: data
    :type x: NxK matrix

    :returns: **y** (*scalar*) - 1 if the imaginary part of *x* has any nonzero elements, 0 if it consists entirely of 0's.

Remarks
-------

The function :func:`iscplx` tests whether *x* is a complex matrix or not, but it
does not test the contents of the imaginary part of *x*. :func:`hasimag` tests the
contents of the imaginary part of *x* to see if it is zero.

:func:`hasimag` actually tests the imaginary part of *x* against a tolerance to
determine if it is negligible. The tolerance used is the imaginary
tolerance set with the :func:`sysstate` command, case 21.

Some functions are not defined for complex matrices. :func:`iscplx` can be used
to determine whether a matrix has no imaginary part and so can pass
through those functions. :func:`hasimag` can be used to determine whether a
complex matrix has a negligible imaginary part and could thus be
converted to a real matrix to pass through those functions.

:func:`iscplx` is useful as a preliminary check because for large matrices it is
much faster than :func:`hasimag`.


Examples
----------------

::

    x = { 1   2 3i,
          4-i 5 6i,
          7   8i 9 };

    if hasimag(x);
        // code path for complex case
        print "X has non-zero imaginary parts"
    else;
        // code path for real case
        print "X does not have non-zero imaginary parts"
    endif;

.. seealso:: Functions :func:`iscplx`
