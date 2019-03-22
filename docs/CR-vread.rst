
vread
==============================================

Purpose
----------------
Reads a string or matrix from a data buffer constructed with vput.

Format
----------------
.. function:: vread(dbuf, xname)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :param xname: the name of the matrix or string to read from dbuf.
    :type xname: string

    :returns: x (*LxM matrix or string*), the item read from dbuf.



Remarks
-------

vread, unlike vget, does not change the contents of dbuf. Reading x from
dbuf does not remove it from dbuf.



Source
------

vpack.src

.. seealso:: Functions :func:`vget`, :func:`vlist`, :func:`vput`
