
svd
==============================================

Purpose
----------------
Computes the singular values of a matrix.

Format
----------------
.. function:: svd(x)

    :param x: matrix whose singular values are to be computed
    :type x: NxP matrix 

    :returns: s (*Mx1 vector*), where :math:`M = min(N,P)`, containing the
        singular values of *x* arranged in descending order.

Global Input
------------

.. data:: _svderr

    scalar, if the singular values cannot be computed, *\_svderr* will be nonzero.

Remarks
-------

#. :func:`svd` is not threadsafe. New code should use :func:`svds` instead.
#. Error handling is controlled with the low bit of the `trap` flag.

   +------------+---------------------------------------------------------------+
   | **trap 0** | set *\_svderr* to a non-zero value and terminate with message |
   +------------+---------------------------------------------------------------+
   | **trap 1** | set *\_svderr* to a non-zero value and continue execution     |
   +------------+---------------------------------------------------------------+

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
    s = svd(x);

After the code above, *s* will be equal to:

::

    49.58 
    14.96 
     2.24

Source
------

svd.src

.. seealso:: Functions :func:`svd2`, :func:`svds`

