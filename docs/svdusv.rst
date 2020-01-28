
svdusv
==============================================

Purpose
----------------
Computes the singular value decomposition of *x* so that: :math:`x = u * s * v'`.

Format
----------------
.. function:: { u, s, v } = svdusv(x)

    :param x: data whose singular values are to be computed, where the last two dimensions are NxP.
    :type x: NxP matrix or K-dimensional array

    :return u: where the last two dimensions are :math:`NxN`, the left singular vectors
        of x.

    :rtype u: NxN matrix or K-dimensional array

    :return s: where the last two dimensions describe :math:`NxP` diagonal
        arrays, the singular values of *x* arranged in descending order on the principal diagonal.

    :rtype s: NxP diagonal matrix or K-dimensional array

    :return v: where the last two dimensions are :math:`PxP`, the right singular vectors of *x*.

    :rtype v: PxP matrix or K-dimensional array

Examples
----------------

::

    // Create 6x3 matrix
    x = { -9.35    15.67   -41.75,
         -13.55    40.97    15.55,
          -0.95   -17.03    40.15,
           8.15    -9.73    13.15,
           2.35   -36.73   -43.55,
          13.35     6.87    16.45  };

    // Perform matrix decomposition
    { u, s, v } = svdusv(x);

After the code above, the outputs will have the following values;

::

    u =  0.44    -0.49    -0.06     0.36    -0.24     0.61
        -0.35    -0.60    -0.28     0.12     0.65    -0.08
        -0.41     0.46    -0.53     0.07     0.03     0.58
        -0.12     0.25     0.24     0.91     0.08    -0.18
         0.67     0.35    -0.13    -0.02     0.64     0.05
        -0.23     0.04     0.75    -0.17     0.33     0.50

    s = 79.03     0.00     0.00
         0.00    60.19     0.00
         0.00     0.00    17.16
         0.00     0.00     0.00
         0.00     0.00     0.00
         0.00     0.00     0.00

    v = -0.02     0.26     0.97
        -0.32    -0.91     0.24
        -0.95     0.31    -0.10

Remarks
-------

#. If *x* is an array, the resulting arrays *u*, *s* and *v* will contain their
   respective results for each of the corresponding 2-dimensional arrays
   described by the two trailing dimensions of *x*. In other words, for a
   10x4x5 array *x*:

   -  *u* will be a 10x4x4 array, containing the left singular vectors of
      each of the 10 corresponding 4x5 arrays contained in *x*.
   -  *s* will be a 10x4x5 array, containing the singular values.
   -  *v* will be a 10x5x5 array containing, the right singular vectors.

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
      { u, s, v } = svdusv(x);

      // Check for failure or success
      if scalmiss(s[1, 1]);
         // Code for failure case
      endif;

   Note that in the ``trap 1`` case, if the input to :func:`svdusv` is a
   multi-dimensional array and the singular values for a submatrix fail
   to compute, only the first value of that *s* submatrix will be set to a
   missing value. For a 3 dimensional array, you could change the `if`
   check in the above example to:

   ::

      // Check for success or failure of each submatrix
      if ismiss(s[., 1, 1]);

.. seealso:: Functions :func:`svd1`, :func:`svdcusv`, :func:`svds`
