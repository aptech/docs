
stocv
==============================================

Purpose
----------------

Converts a string to a character vector.

Format
----------------
.. function:: v = stocv(s)

    :param s: to be converted to character vector.
    :type s: string

    :returns: v (*Nx1 character vector*), contains the contents of *s*.

Remarks
-------

:func:`stocv` breaks *s* up into a vector of 8-character length matrix elements.

.. NOTE:: The character information in the vector is not guaranteed to be null-terminated.

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

