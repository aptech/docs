
upmat, upmat1
==============================================

Purpose
----------------

Returns the upper portion of a matrix. :func:`upmat` returns the main diagonal and every element above. 
:func:`upmat1` is the same except it replaces the main diagonal with ones.

Format
----------------
.. function:: u = upmat(x)
              u = upmat1(x)

    :param x: data
    :type x: NxK matrix

    :return u: containing the upper elements of *x*. The lower elements are
        replaced with zeros. :func:`upmat` returns the main diagonal intact. :func:`upmat1`
        replaces the main diagonal with ones.

    :rtype u: NxK matrix

Examples
----------------

::

    x = { 7  2 -1,
          2  3 -2,
          4 -2  8 };
     
    u = upmat(x);
    u1 = upmat1(x);

The resulting matrices are:

::

        7  2 -1       1  2 -1
    u = 0  3 -2  u1 = 0  1 -2
        0  0  8       0  0  1

Source
------

diag.src

.. seealso:: Functions :func:`lowmat`, :func:`lowmat1`, :func:`diag`, :func:`diagrv`, :func:`crout`

