
conv
==============================================

Purpose
----------------

Computes the convolution of two vectors.

Format
----------------
.. function:: conv(b, x, f, l)

    :param b:
    :type b: Nx1 vector

    :param x:
    :type x: Lx1 vector

    :param f: the first convolution to compute.
    :type f: scalar

    :param l: the last convolution to compute.
    :type l: scalar

    :returns: **c** (*Qx1 result*) - where: :math:`Q = (l - f + 1)`

        If *f* is 0, the first
        to the l'th convolutions are computed. If *l* is 0, the
        f'th to the last convolutions are computed. If *f* and *l*
        are both zero, all the convolutions are computed.

Remarks
-------

If *x* and *b* are vectors of polynomial coefficients, this is the same as
multiplying the two polynomials.

Examples
----------------

Full convolution
++++++++++++++++

The following example is equivalent to the following polynomial multiplication :math:`(x^2 + 3)(2x + 7) = 2x^3 + 7x^2 + 6x + 21`

::

    // Vectors
    u = {1, 0, 3};
    v = {2, 7};

    /*
    ** Set f, l equal to zero and
    ** all the convolutions are computed
    */
    print conv(u, v, 0, 0);

After the code the following is printed to the screen:

::

    2.0000
    7.0000
    6.0000
   21.0000 

Partial convolution
+++++++++++++++++++

::

    // Vectors
    u = {1, 0, 3};
    v = {2, 7};

    /*
    ** In this case we
    ** set f =1 and l =2 to see just the
    ** first and second convolutions
    */
    print conv(u, v, 1, 2);

After the code the following is printed to the screen:

::

    2.0000
    7.0000

.. seealso:: :func:`polymult`
