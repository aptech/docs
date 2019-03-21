
vget
==============================================

Purpose
----------------
Extracts a matrix or string from a data buffer constructed with vput.

Format
----------------
.. function:: vget(dbuf, name)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :param name: the name of the string or matrix to extract from  dbuf.
    :type name: string

    :returns: x (*LxM matrix or string*), the item extracted from  dbuf.

    :returns: dbufnew (*Kx1 vector*), the remainder of  dbuf after x has been
        extracted.



Source
------

pack.src

