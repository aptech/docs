
cdfGam
==============================================

Purpose
----------------
Computes the regularized lower incomplete gamma function.

Format
----------------
.. function:: p = cdfGam(x, intlim)

    :param x: Values at which to evaluate the regularized lower incomplete gamma function. :math:`x > 0`.
    :type x: NxK matrix

    :param int_lim: ExE compatible with *x*, containing the integration limit. :math:`int\_lim > 0`.
    :type int_lim: LxM matrix

    :return p: Each element in *p* is the regularized lower incomplete gamma function evaluated at the corresponding element in *x*.

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
    x = { 0.5 1 3 10 };

    // Create a 6x1 column vector: 0, 0.2, 0.4, ..., 1.0
    int_lim = seqa(0,.2,6);

    /*
    ** Compute for all combinations of the elements
    ** of 'x' and 'int_lim'
    */
    p = cdfGam(x, int_lim);

    print "intlim = " int_lim;
    print "p = " p;

After the code above:

::

    intlim =
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

This computes the integrals over the range from 0 to 1, in increments of 0.2, at the parameter values 0.5, 1, 3, 10.

Remarks
-------

The regularized lower incomplete gamma function returns the integral

.. math:: \text{cdfGam(x, int_lim)} = \int_{0}^{int\_lim} \frac{e^{-t}t^{(x-1)}}{\Gamma(x)}dt

A -1 is returned for those elements with invalid inputs.

