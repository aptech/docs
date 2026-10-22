
cdfGam
==============================================

Purpose
----------------
Computes the regularized lower incomplete gamma function.

Format
----------------
.. function:: p = cdfGam(shape, x)

    :param shape: The shape parameter of the gamma distribution. :math:`shape > 0`.
    :type shape: NxK matrix

    :param x: ExE compatible with *shape*, the values at which to evaluate the function (the upper limit of integration). An *x* below 0 returns 0.
    :type x: LxM matrix

    :return p: Each element in *p* is the regularized lower incomplete gamma function with the corresponding shape in *shape*, evaluated at the corresponding element in *x*.

    :rtype p: matrix, max(N,L) by max(K,M)

Examples
----------------

Basic example
+++++++++++++++
::

    p = cdfGam(1.2, 3);

After the above code, `p` will equal

::

   0.9287

Matrix example
+++++++++++++++

::

    // Create a 1x4 row vector
    shape = { 0.5 1 3 10 };

    // Create a 6x1 column vector: 0, 0.2, 0.4, ..., 1.0
    x = seqa(0,.2,6);

    /*
    ** Compute for all combinations of the elements
    ** of 'shape' and 'x'
    */
    p = cdfGam(shape, x);

    print "x = " x;
    print "p = " p;

After the code above:

::

    x =
    0.00000000
    0.20000000
    0.40000000
    0.60000000
    0.80000000
    1.0000000

    p =
    0.00000000       0.00000000       0.00000000       0.00000000
    0.47291074       0.18126925     0.0011484812   2.3530688e-014
    0.62890663       0.32967995     0.0079263319   2.0098099e-011
    0.72667832       0.45118836      0.023115288   9.6697183e-010
    0.79409679       0.55067104      0.047422596   1.4331002e-008
    0.84270079       0.63212056      0.080301397   1.1142548e-007

This computes the integrals from 0 to each value of *x* (0 to 1, in increments of 0.2) for the shape values 0.5, 1, 3, 10.

Remarks
-------

The regularized lower incomplete gamma function returns the integral

.. math:: \text{cdfGam(shape, x)} = \int_{0}^{x} \frac{e^{-t}t^{(shape-1)}}{\Gamma(shape)}dt

If *shape* is not greater than 0, :func:`cdfGam` returns a scalar error code
and :func:`scalerr` returns 1, the position of *shape*. An *x* below 0 is not
an error: it returns 0. A missing value in either argument returns a missing
value.

