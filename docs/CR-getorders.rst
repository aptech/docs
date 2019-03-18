
getorders
==============================================

Purpose
----------------

Returns a vector containing the size of the dimensions of an array, matrix, or other symbol.
sss

Format
----------------
.. function:: getorders(a)

    :param a: N-dimensional array, matrix, sparse matrix, string or string array.
    :type a: TODO

    :returns: orders (*Nx1 vector of orders*), the sizes of the dimensions of the array.

Examples
----------------

::

    //Allocate a 5x100x3 dimensional array with each element equal to 0.
    a = arrayinit(5|100|3,0);
    
    //Find the size of the dimensions in 'a'
    orders = getorders(a);

After the code above:

::

    orders =   5
             100
               3

//Create 121x4 random matrix
x = rndn(121, 4);

//Get the number of rows and columns of the matrix
dims = getorders(x);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code, dims should equal:

::

    121
      4

.. seealso:: Functions :func:`getdims`, :func:`rows`, :func:`cols`
