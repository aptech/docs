
aconcat
==============================================

Purpose
----------------

Concatenates conformable matrices and arrays in a user-specified dimension.

Format
----------------
.. function:: y = aconcat(a, b, dim)

    :param a:
    :type a: Matrix or N-dimensional array.

    :param b: Conformable with  *a*.
    :type b: Matrix or K-dimensional array

    :param dim: Dimension in which to concatenate.
    :type dim: Scalar

    :return y: The result of the concatenation.
    :rtype y: N-dimensional array

Examples
----------------

::

    // Create a 2x3x4 array with each element set to 0
    a = arrayinit(2|3|4,0);

    // Create a 3x4 matrix with each element set to 3
    b = 3*ones(3, 4);
    y = aconcat(a, b, 3);

*y* will be a 3x3x4 array, where :math:`[1,1,1]`
through :math:`[2,3,4]` are zeros and :math:`[3,1,1]` through :math:`[3,2,4]` are threes.

::

    /*
    ** Create an additive sequence from 1-20 and 'reshape' it
    ** into a 4x5 matrix
    */
    a = reshape(seqa(1, 1, 20), 4, 5);

    b = zeros(4, 5);
    y = aconcat(a, b, 3);

*y* will be a 2x4x5 array, where :math:`[1,1,1]` through :math:`[1,4,5]`
are sequential integers beginning with 1, and :math:`[2,1,1]` through
:math:`[2,4,5]` are zeros.

::

    /*
    ** The pipe operator '|' causes vertical concatenation so
    ** that the statement 2|3|4 creates a 3x1 column vector
    ** equal to { 2, 3, 4 }
    */
    a = arrayinit(2|3|4,0);
    b = seqa(1, 1, 24);

    // 'Reshape' the vector 'b' into a 2x3x4 dimensional array
    b = areshape(b,2|3|4);
    y = aconcat(a, b, 5);

*y* will be a 2x1x2x3x4 array,
where :math:`[1,1,1,1,1]` through :math:`[1,1,2,3,4]` are zeros, and :math:`[2,1,1,1,1]`
through :math:`[2,1,2,3,4]` are sequential integers beginning with 1.

::

    a = arrayinit(2|3|4, 0);
    b = seqa(1, 1, 6);
    b = areshape(b, 2|3|1);
    y = aconcat(a, b, 1);
    print "y = " y;

*y* will be a 2x3x5 array:

::

    y =

    Plane [1,.,.]

    0.00     0.00     0.00     0.00      1.0
    0.00     0.00     0.00     0.00      2.0
    0.00     0.00     0.00     0.00      3.0

    Plane [2,.,.]

    0.00     0.00     0.00     0.00      4.0
    0.00     0.00     0.00     0.00      5.0
    0.00     0.00     0.00     0.00      6.0

Remarks
-------

*a* and *b* are conformable if all dimensions other than the dimension specified by *dim* have
the same sizes. 

If *a* or *b* is a matrix, then the size of dimension 1 is the number of columns in the matrix, and the size of dimension 2 is the
number of rows in the matrix.

.. seealso:: Functions :func:`areshape`
