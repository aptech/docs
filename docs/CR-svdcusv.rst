
svdcusv
==============================================

Purpose
----------------
Computes the singular value decomposition of *x* so that: :math:`x = u * s * v'` (compact *u*).

Format
----------------
.. function:: { u, s, v } = svdcusv(x)

    :param x: , whose singular values are to be computed.
    :type x: NxP matrix or K-dimensional array where the last two dimensions are NxP

    :returns: u (*NxN or NxP matrix or K-dimensional array*) where the last two dimensions are :math:`NxN` or
        :math:`NxP`, the left singular vectors of *x*. If :math:`N > P`, *u* is :math:`NxP`, containing only the :math:`P` left
        singular vectors of *x*.

    :returns: s (*NxP or PxP diagonal matrix or K-dimensional array*) where the last two dimensions describe :math:`NxP`
        or :math:`PxP` diagonal arrays, the singular values of *x* arranged in descending order on the
        principal diagonal. If :math:`N > P`, *s* is :math:`PxP`.

    :returns: v (*PxP matrix or K-dimensional array*) where the last two dimensions are :math:`PxP`, the right singular vectors of *x*.

Remarks
-------

#. If *x* is an array, the resulting arrays *u*, *s* and *v* will contain their
   respective results for each of the corresponding 2-dimensional arrays
   described by the two trailing dimensions of *x*. In other words, for a
   10x4x5 array *x*:

   -  *u* will be a 10x4x4 array containing the left singular vectors of
      each of the 10 corresponding 4x5 arrays contained in *x*.
   -  *s* will be a 10x4x5 array containing the singular values.
   -  *v* will be a 10x5x5 array containing the right singular vectors

#. Error handling is controlled by the `trap` command. If not all of the
   singular values can be computed:

   +-----------------------------------+-----------------------------------+
   | **trap 0**                        | terminate with an error message   |
   +-----------------------------------+-----------------------------------+
   | **trap 1**                        | set the first element of *s* to a |
   |                                   | scalar missing value and continue |
   |                                   | execution                         |
   +-----------------------------------+-----------------------------------+

   ::

      // Turn on error trapping
      trap 1;

      // Compute singular value decomposition
      { u, s, v } = svdcusv(x);

      // Check for failure or success
      if scalmiss(s[1,1]);
         // Code for failure case
      endif;

   Note that in the ``trap 1`` case, if the input to :func:`svdcusv` is a
   multi-dimensional array and the singular values for a submatrix fail
   to compute, only the first value of that *s* submatrix will be set to a
   missing value. For a 3 dimensional array, you could change the if
   check in the above example to:

   ::

      // Check for success or failure of each submatrix
      if ismiss(s[.,1,1]);

Examples
----------------

::

    // Create a 10x3 matrix
    x = {  -0.60     3.50     0.47, 
            8.40    16.50     0.27,
           11.40     6.50     0.17,
            7.40    -0.50    -2.43,
           -9.60   -10.50     0.57,
          -17.60    -5.50     0.67,
          -12.60   -14.50     0.87,
           18.40    12.50    -1.43,
          -11.60   -19.50     0.77,
            6.40    11.50     0.07 };
    
    // Calculate the singular values
    { u, s, v } = svdcusv(x);

After the code above, *u*, *s* and *v* will be equal to:

::

    u =  0.04     0.20    -0.11
         0.36     0.38    -0.14
         0.25    -0.23    -0.44
         0.10    -0.39     0.75 
        -0.29    -0.04    -0.06 
        -0.33     0.57     0.35 
        -0.39    -0.08    -0.14 
         0.44    -0.29     0.10 
        -0.44    -0.37    -0.25 
         0.26     0.24    -0.07 
    
    s = 49.58     0.00     0.00 
         0.00    14.96     0.00 
         0.00     0.00     2.24 
    
    v =  0.70    -0.70    -0.10 
         0.71     0.70     0.05 
        -0.04     0.10    -0.99

.. seealso:: Functions :func:`svd2`, :func:`svds`, :func:`svdusv`

