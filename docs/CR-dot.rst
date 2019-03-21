
dot
==============================================

Purpose
----------------

Returns a scalar dot product of the columns of two matrices.

Format
----------------
.. function:: dot(x, y)

    :param x: 
    :type x: Nx1 vector or NxK matrix

    :param y: 
    :type y: Nx1 vector or NxK matrix

    :returns: z (*TODO*), scalar or Kx1 dot product

Examples
----------------

Basic usage
+++++++++++

::

    //Create two 4x1 column vectors
    x = { 5,
          9,
          3,
          4 };
    
    y = { 9,
         -6,
          8,
          1  };
    
    //Compute dot product
    z = dot(x,y);
    
    print  "z = " z;

After the code above:

::

    z = 19

Dot product of the corresponding columns of two matrices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Create two 4x2 matrices
    x = { 5 1,
          9 3,
          3 8,
          4 2 };
    
    y = { 9  8,
         -6  4,
          8  3,
          1 -2 };
    
    //Compute dot product
    z = dot(x, y);
    
    print  "z = " z;

After the code above:

::

    z = 19
        40

Remarks
-------

Inputs x and y should have the same columns.

.. seealso:: Functions :func:`crossprd`, :func:`norm`

dot product inner product scalar dot product
