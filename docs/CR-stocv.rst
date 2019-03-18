
stocv
==============================================

Purpose
----------------

Converts a string to a character vector.

Format
----------------
.. function:: stocv(s)

    :param s: to be converted to character vector.
    :type s: string

    :returns: v (*Nx1 character vector*), contains the contents of  s.

Examples
----------------

::

    s = "Now is the time for all good men";
    v = stocv(s);

::

    "Now is t"
    
         "the time "
    v =
         "for all "
    
         "good men"

.. seealso:: Functions :func:`cvtos`, :func:`vget`, :func:`vlist`, :func:`vput`, :func:`vread`
