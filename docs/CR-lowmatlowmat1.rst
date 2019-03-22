
lowmat, lowmat1
==============================================

Purpose
----------------

Returns the lower portion of a matrix. lowmat returns the main diagonal and every element below. lowmat1 is the same except it replaces the main diagonal with ones.

Format
----------------
.. function:: lowmat(x) 
			  lowmat1(x)

    :param x: 
    :type x: NxN matrix

    :returns: L (*NxN matrix*) containing the lower elements
        of the matrix. The upper elements
        are replaced with zeros. lowmat returns the
        main diagonal intact. lowmat1 replaces the main
        diagonal with ones.

Remarks
-------

The lowmat function along with upmat1 can be used to extract the LU
factors from the return


Examples
----------------

::

    x = { 1 2 -1,
          2 3 -2,
          1 -2 4 };
     
    L = lowmat(x);
    L1 = lowmat1(x);

The resulting matrices are

::

    1  0  0       1   0   0
    L = 2  3  0  L1 = 2   1   0
        1 -2  4       1  -2   1

Source
------

diag.src

.. seealso:: Functions :func:`upmat`, :func:`upmat1`, :func:`diag`, :func:`diagrv`, :func:`crout`, :func:`croutp`
