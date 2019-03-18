
cvtos
==============================================

Purpose
----------------

Converts a character vector to a string.

Format
----------------
.. function:: cvtos(v)

    :param v: to be converted to a string.
    :type v: Nx1 character vector

    :returns: s (*string*), contains the contents of  v.

Examples
----------------

::

    let v = { "Now is t" "he time " "for all " "good men" };
    s = cvtos(v);

Now the variable s is a string with the following contents.

::

    s = "Now is the time for all good men"

.. seealso:: Functions :func:`stocv`, :func:`vget`, :func:`vlist`, :func:`vput`, :func:`vread`
