
svd2
==============================================

Purpose
----------------
Computes the singular value decomposition of a matrix so that: x = u * s * v' (compact u).

Format
----------------
.. function:: svd2(x)

    :param x: 
    :type x: NxP matrix whose singular values are to be computed

    :returns: u (*NxN or NxP matrix*), the left singular vectors of x.
        If N > P, then  u will be NxP, containing only the P left
        singular vectors of x.

    :returns: s (*NxP or PxP diagonal matrix*), containing the singular
        values of x arranged in descending order on the
        principal diagonal. If N > P, then s will be PxP.

    :returns: v (*PxP matrix*), the right singular vectors of x.

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
    { u, s, v } = svd2(x);

After the code above, u, s and v will be equal to:

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

Remarks
+++++++

#. svd2 is not threadsafe. New code should use svdcusv instead.
#. Error handling is controlled with the low bit of the trap flag. If
   the singular values cannot be computed, \_svderr will be set to a
   non-zero value.

   +------------+-------------------------------------------------------------+
   | **trap 0** | set \_svderr to a non-zero value and terminate with message |
   +------------+-------------------------------------------------------------+
   | **trap 1** | set \_svderr to a non-zero value and continue execution     |
   +------------+-------------------------------------------------------------+

Source
------

svd.src

.. seealso:: Functions :func:`svd`, :func:`svd1`, :func:`svdcusv`

singular value decomposition X USV' svd1 compact
