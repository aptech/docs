
vput
==============================================

Purpose
----------------
Inserts a matrix or string into a data buffer.

Format
----------------
.. function:: dbufnew = vput(dbuf, x, xname)

    :param dbuf: a data buffer containing various strings and matrices. 
        If *dbuf* is a scalar 0, a new data buffer will be created.
    :type dbuf: Nx1 vector

    :param x: item to be inserted into *dbuf*.
    :type x: LxM matrix or string

    :param xname: the name of *x*, will be inserted with *x* into *dbuf*.
    :type xname: string

    :return dbufnew: the data buffer after *x* and *xname* have been inserted.

    :rtype dbufnew: Kx1 vector

Remarks
-------

If *dbuf* already contains *x*, the new value of *x* will replace the old one.

Source
------

vpack.src

.. seealso:: Functions :func:`vget`, :func:`vlist`, :func:`vread`

