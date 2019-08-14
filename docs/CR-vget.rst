
vget
==============================================

Purpose
----------------
Extracts a matrix or string from a data buffer constructed with :func:`vput`.

Format
----------------
.. function:: { x, dbufnew } = vget(dbuf, name)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :param name: the name of the string or matrix to extract from *dbuf*.
    :type name: string

    :return x: the item extracted from *dbuf*.

    :type x: LxM matrix or string

    :return dbufnew: the remainder of *dbuf* after *x* has been extracted.

    :type dbufnew: Kx1 vector

Source
------

pack.src

.. seealso:: Functions :func:`vlist`, :func:`vput`, :func:`vread`

