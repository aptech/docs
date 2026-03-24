
vread
==============================================

Purpose
----------------
Reads a string or matrix from a data buffer constructed with :func:`vput`.

Format
----------------
.. function:: x = vread(dbuf, xname)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :param xname: the name of the matrix or string to read from *dbuf*.
    :type xname: string

    :return x: the item read from *dbuf*.

    :rtype x: LxM matrix or string

Remarks
-------

:func:`vread`, unlike :func:`vget`, does not change the contents of *dbuf*. Reading *x* from
*dbuf* does not remove it from *dbuf*.

Examples
--------

::

    // Read an item from a data buffer without removing it
    dbuf = vput(0, rndn(2, 2), "mymat");
    dbuf = vput(dbuf, "test", "mystr");

    x = vread(dbuf, "mymat");
    print x;
    // dbuf still contains "mymat" and "mystr"

Source
------

vpack.src

.. seealso:: Functions :func:`vget`, :func:`vlist`, :func:`vput`

