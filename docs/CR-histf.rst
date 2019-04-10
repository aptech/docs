
histf
==============================================

Purpose
----------------

Graphs a histogram given a vector of frequency counts. Note: This function is for use with the deprecated PQG graphics.
Use plotSetHistF instead.

Library
-------

pgraph

Format
----------------
.. function:: histf(f, c)

    :param f: frequencies to be graphed.
    :type f: Nx1 vector

    :param c: numeric labels for categories. If this is a scalar 0, a sequence from 1 to :code:`rows(f)` will be created.
    :type c: Nx1 vector



Remarks
-------

The axes are not automatically labeled. Use :func:`xlabel` for the category axis
and :func:`ylabel` for the frequency axis.


Source
------

phist.src

.. seealso:: Functions :func:`hist`, :func:`bar`, :func:`xlabel`, :func:`ylabel`

