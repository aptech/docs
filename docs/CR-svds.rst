
svds
==============================================

Purpose
----------------
Computes the singular values of a x.

Format
----------------
.. function:: svds(x)

    :param x: NxP matrix or K-dimensional array
        where the last two dimensions are NxP, whose singular values
        are to be computed.
    :type x: TODO

    :returns: s (*TODO*), min(N,P)x1 vector or K-dimensional array where the last two dimensions are min(N,P)x1, the
        singular values of x arranged in descending order.

Examples
----------------

::

    //Create a 10x3 matrix
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
    
    //Calculate the singular values
    s = svds(x);

After the code above, s will be equal to:

::

    49.58 
    14.96 
     2.24

Remarks
+++++++

#. If x is an array, the result will be an array containing the singular
   values of each of the 2-dimensional arrays described by the two
   trailing dimensions of x. In other words, for a 10x4x5 array x, s
   will be a 10x4x1 array containing the singular values of each of the
   10 4x5 arrays contained in x.

#. If the singular values cannot be computed, either the program will be
   terminated with an error message, or the first element of the return,
   s[1], is set to a missing value. This behavior is controlled by the
   trap command. Below is an example with error trapping:

   ::

      //Turn on error trapping
      trap  1;

      //Calculate singular values
      s = svds(x);

      //Check for success or failure
      if ismiss(s);
      //Code to handle failure case
      endif;

   Note that in the trap 1 case, if the input to svds is a
   multi-dimensional array and the singular values for a submatrix fail
   to compute, only the first value of that s submatrix will be set to a
   missing value. For a 3 dimensional array, you could change the if
   check in the above example to:

   ::

      //Check for success or failure of each submatrix
      if ismiss(s[.,1,1]);

#. Call either svdcusv or svdusv, to also calculate the right and left
   singular vectors

.. seealso:: Functions :func:`svd`, :func:`svdcusv`, :func:`svdusv`

singular value decomposition
