
vnamecv
==============================================

Purpose
----------------
Returns the names of the elements of a data buffer constructed with :func:`vput`.

Format
----------------
.. function:: cv = vnamecv(dbuf)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :return cv: containing the names of the elements of *dbuf*.

    :rtype cv: Kx1 character vector

Examples
--------

::

    // Get the names of items stored in a data buffer
    dbuf = vput(0, rndn(2, 2), "alpha");
    dbuf = vput(dbuf, "hello", "beta");
    cv = vnamecv(dbuf);
    print cv;

.. seealso:: Functions :func:`vget`, :func:`vput`, :func:`vread`, :func:`vtypecv`

