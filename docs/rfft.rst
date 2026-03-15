
rfft
==============================================

Purpose
----------------

Computes a real 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: y = rfft(x)

    :param x: data
    :type x: NxK real matrix

    :return y: where :math:`L` and :math:`M` are the smallest powers of 2 greater than or equal to :math:`N` and :math:`K`, respectively.

    :rtype y: LxM matrix

Remarks
-------

Computes the RFFT of *x*, scaled by :math:`\frac{1}{(L*M)}`.

This uses a Temperton Fast Fourier algorithm.

If :math:`N` or :math:`K` is not a power of 2, *x* will be padded out with zeros before
computing the transform.

Examples
--------

::

    // Create an 8-element signal
    x = { 1, 2, 3, 4, 5, 6, 7, 8 };

    // Compute the real FFT
    y = rfft(x);

    print "Real FFT of x:";
    print y;

The above code produces the following output:

::

    Real FFT of x:

       4.5000000
     -0.50000000 +        1.2071068i
     -0.50000000 +       0.50000000i
     -0.50000000 +       0.20710678i
     -0.50000000
     -0.50000000 -       0.20710678i
     -0.50000000 -       0.50000000i
     -0.50000000 -        1.2071068i

.. seealso:: Functions :func:`rffti`, :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`
