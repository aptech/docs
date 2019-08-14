
svd1
==============================================

Purpose
----------------
Computes the singular value decomposition of a matrix so that: :math:`x = u * s * v'`.

Format
----------------
.. function:: { u, s, v } = svd1(x)

    :param x: matrix whose singular values are to be computed
    :type x: NxP matrix

    :returns: u (*NxN matrix*), the left singular vectors of *x*.

    :returns: s (*NxP diagonal matrix*), containing the singular
        values of *x* arranged in descending order on the
        principal diagonal.

    :returns: v (*PxP matrix*), the right singular vectors of *x*.

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
    { u, s, v } = svd1(x);

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

#. :func:`svd1` is not threadsafe. New code should use svdusv instead.
#. Error handling is controlled with the low bit of the `trap` flag.

+------------+---------------------------------------------------------------+
| **trap 0** | set *\_svderr* to a non-zero value and terminate with message |
+------------+---------------------------------------------------------------+
| **trap 1** | set *\_svderr* to a non-zero value and continue execution     |
+------------+---------------------------------------------------------------+

Source
------

svd.src

.. seealso:: Functions :func:`svd`, :func:`svd2`, :func:`svdusv`

