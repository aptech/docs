
qrsol
==============================================

Purpose
----------------

Computes the solution of :math:`Rx = b` where :math:`R` is an upper triangular matrix.

Format
----------------
.. function:: x = qrsol(b, R)

    :param b: data
    :type b: PxL matrix

    :param R: upper triangular matrix
    :type R: PxP matrix

    :return x: solution of :math:`Rx = b` where :math:`R` is an upper triangular matrix.

    :rtype x: PxL matrix

Remarks
-------

:func:`qrsol` applies a backsolve to :math:`Rx = b` to solve for *x*. Generally *R* will be
the *R* matrix from a QR factorization. :func:`qrsol` may be used, however, in any situation
where *R* is upper triangular.

Examples
--------

::

    // Upper triangular matrix R and right-hand side b
    r = { 3 1,
          0 2 };
    b = { 7, 4 };

    // Solve R*x = b
    x = qrsol(b, r);

    print "Solution x:";
    print x;
    print "R*x (should equal b):";
    print (r * x);

The above code produces the following output:

::

    Solution x:

       1.6666667
       2.0000000

    R*x (should equal b):

       7.0000000
       4.0000000

Source
------

qrsol.src

.. seealso:: Functions :func:`qqr`, :func:`qr`, :func:`qtyr`, :func:`qrtsol`
