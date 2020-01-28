
cvtos
==============================================

Purpose
----------------

Converts a character vector to a string.

Format
----------------
.. function:: s = cvtos(v)

    :param v: Character vector to be converted to a string.
    :type v: Nx1 vector

    :return s: contains the contents of *v*.

    :rtype s: string

Examples
----------------

::

    v = { "Now is t" "he time " "for all " "good men" };
    s = cvtos(v);

Now the variable *s* is a string with the following contents.

::

    s = "Now is the time for all good men"

Remarks
-------

:func:`cvtos` in effect appends the elements of *v* together into a single string.

:func:`cvtos` was written to operate in conjunction with :func:`stocv`. If you pass it a
character vector that does not conform to the output of :func:`stocv`, you may
get unexpected results. For example, :func:`cvtos` does NOT look for 0
terminating bytes in the elements of *v*; it assumes every element except
the last is 8 characters long. If this is not true, there will be 0's in
the middle of *s*.

If the last element of *v* does not have a terminating 0 byte, :func:`cvtos`
supplies one for *s*.


.. seealso:: Functions :func:`stocv`, :func:`vget`, :func:`vlist`, :func:`vput`, :func:`vread`
