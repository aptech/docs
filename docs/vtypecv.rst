
vtypecv
==============================================

Purpose
----------------
Returns the types of the elements of a data buffer constructed with :func:`vput`.

Format
----------------
.. function:: cv = vtypecv(dbuf)

    :param dbuf: a data buffer containing various strings and matrices.
    :type dbuf: Nx1 vector

    :return cv: containing the types of the elements of *dbuf*.

    :rtype cv: Kx1 character vector

.. seealso:: Functions :func:`vget`, :func:`vput`, :func:`vread`, :func:`vnamecv`

