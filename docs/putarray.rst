
putarray
==============================================

Purpose
----------------

Puts a contiguous subarray into an N-dimensional array and returns the resulting array.

Format
----------------
.. function:: y = putarray(dest, loc, src)

    :param dest: destination data
    :type dest: N-dimensional array

    :param loc: indices into the array to locate the subarray of interest, where *M* is a value from 1 to *N*.
    :type loc: Mx1 vector

    :param src: source data
    :type src: [N-M]-dimensional array or matrix or scalar.

    :return y: resulting array with destination data in *a* inserted into the source data.

    :rtype y: N-dimensional array

Examples
----------------


Example 1: 3D array
+++++++++++++++++++++

::

    // Create a 2x3x4 dimensional array filled with zeros
    dest = arrayinit(2|3|4, 0);

    // Create a 3x4 matrix of random numbers
    rndseed 54324;
    src = rndn(3,4);

    // Place the contents of 'src' into the
    // first 3x4 submatrix of the array
    loc = 1;
    a = putarray(dest, loc, src);

After the above code, *a* will equal:

::

    Plane [1,.,.] 
    
     -2.4904   0.5745  -2.6505   1.1118 
      0.8425   1.3397  -1.1305   0.8991 
     -1.3205  -0.3568   1.8457   0.6052 
    
    Plane [2,.,.] 
    
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000

Note that in the above call to :func:`putarray`, a complete copy of the *dest* array will be made to copy into *a*. In this case, it is obvious that is is needed. However, even if we change the code to:

::

    dest = putarray(dest, loc, src);

a complete copy of *dest* will be made. This will significantly slow down your code. We can avoid this in one of two ways. The first is to use an index assignment instead of :func:`putarray` like this:

::

    // An index assignment avoids a complete copy
    // of the array and improves performance
    dest[loc,.,.] = src; 

The other option is to use the `move` keyword to tell GAUSS that it does not need to keep the original version of *dest*, like this:

::

    // 'move' tells GAUSS it does not need to keep
    // the original copy of 'dest', which will improve performance
    dest = putarray(move(dest), loc, src);


Example 2: Arrays with more than 3 dimensions
++++++++++++++++++++++++++++++++++++++++++++++++

To use :func:`putarray` with arrays with more than three dimensions, the location variable will need to have two fewer dimensions than the array being assigned to. Our example array below has four dimensions, so the location variable has two dimensions.

::

    // Initialize a 2x2x3x4 array with zeros
    a = arrayinit(2|2|3|4, 0);
    
    // Fill the [2, 1, ., .] submatrix
    // with the value of pi
    loc = { 2, 1 };
    src = ones(3, 4) .* pi;
    a = putarray(a, loc, src);

After the above code, *a* is equal to:

::

    Plane [1,1,.,.] 
    
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
    
    Plane [1,2,.,.] 
    
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
    
    Plane [2,1,.,.] 
    
      3.1416   3.1416   3.1416   3.1416 
      3.1416   3.1416   3.1416   3.1416 
      3.1416   3.1416   3.1416   3.1416 
    
    Plane [2,2,.,.] 
    
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000 
      0.0000   0.0000   0.0000   0.0000
 

Remarks
-------

See the performance indications in example 1 above.

If *loc* is an Nx1 vector, then *src* must be a scalar. If *loc* is an [N-1]x1
vector, then *src* must be a 1-dimensional array or a 1xL vector, where *L*
is the size of the fastest moving dimension of the array. If *loc* is an
[N-2]x1 vector, then *src* must be a KxL matrix, or a KxL 2-dimensional
array, where *K* is the size of the second fastest moving dimension.

Otherwise, if *loc* is an Mx1 vector, then *src* must be an [N-M]-dimensional
array, whose dimensions are the same size as the corresponding
dimensions of array *dest*.


.. seealso:: Functions `setarray`
