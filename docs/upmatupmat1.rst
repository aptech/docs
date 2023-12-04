
upmat, upmat1
==============================================

Purpose
----------------

Returns the upper portion of a matrix. :func:`upmat` returns the main diagonal and every element above. 
:func:`upmat1` is the same except it replaces the main diagonal with ones.

Format
----------------
.. function:: u = upmat(x [, k, vector])
              u = upmat1(x)

    :param x: data
    :type x: NxK matrix

    :param k: Optional input, an offset for the start of the upper diagonal. See examples.
    :type k: scalar

    :param vector: A binary input with a 1 indicating that the return should be a column vector containing only the upper triangular elements, or a zero indicating the return should be the standard matrix return. 
    :type vector: scalar

    :return u: containing the upper elements of *x*. The lower elements are
        replaced with zeros. :func:`upmat` returns the main diagonal intact. :func:`upmat1`
        replaces the main diagonal with ones.

    :rtype u: NxK matrix

Examples
----------------

Basic example
+++++++++++++++

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

Example with offset
+++++++++++++++++++++

Below we will set the second input, *k* equal to 2. This will set the main diagonal and the diagonal immediately above to be equal to zero.

::

    x = { 16   37   48   46 
          19   39   58   85 
          84   42   44   63 
           8   11   73   50 };


    // Set the first 2 bands of the
    // upper triangle to zero as well
    // as the lower triangle
    u = upmat(x, 2);

::

    u =  0    0   48   46 
         0    0    0   85 
         0    0    0    0 
         0    0    0    0 

Example with a vector return
++++++++++++++++++++++++++++++

Below we will return only the upper triangular elements as a column vector.

::

    x = { 16   37   48   46 
          19   39   58   85 
          84   42   44   63 
           8   11   73   50 };


    u = upmat(x, 0, 1);

::

    u = 16 
        37 
        48 
        46 
        19 
        39 
        58 
        85 
        84 
        42 
        44 
        63 
         8 
        11 
        73 
        50

Source
------

diag.src

.. seealso:: Functions :func:`lowmat`, :func:`lowmat1`, :func:`diag`, :func:`diagrv`, :func:`crout`

