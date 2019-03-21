
upmat, upmat1
==============================================

Purpose
----------------

Returns the upper portion of a matrix. upmat returns the main diagonal and every element above.
           upmat1 is the same except it replaces the main diagonal with ones.

Format
----------------
.. function:: upmat(x)  
			  upmat1(x)

    :param x: 
    :type x: NxK matrix

    :returns: u (*NxK matrix*), containing the upper elements of x. The lower elements are
        replaced with zeros. upmat returns the main diagonal intact. upmat1
        replaces the main diagonal with ones.

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
++++++

diag.src

.. seealso:: Functions :func:`lowmat`, :func:`lowmat1`, :func:`diag`, :func:`diagrv`, :func:`crout`
