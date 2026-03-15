
vlist
==============================================

Purpose
----------------
Lists the contents of a data buffer constructed with :func:`vput`.

Format
----------------
.. function:: vlist(dbuf)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

Remarks
-------

:func:`vlist` lists the names of all the strings and matrices stored in *dbuf*.

Examples
--------

::

    // Create a data buffer and list its contents
    dbuf = vput(0, rndn(3, 3), "myMatrix");
    dbuf = vput(dbuf, "test", "myString");
    vlist(dbuf);

Source
------

vpack.src

.. seealso:: Functions :func:`vget`, :func:`vput`, :func:`vread`

