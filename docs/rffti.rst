
rffti
==============================================

Purpose
----------------

Computes inverse real 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: y = rffti(x)

    :param x: data
    :type x: NxK matrix

    :return y: where :math:`L` and :math:`M` are the smallest
        prime factor products greater than or equal to :math:`N` and :math:`K`.

    :rtype y: LxM real matrix

Remarks
-------

It is up to the user to guarantee that the input will return a real result. If in doubt, use :func:`ffti`.

Examples
--------

::

    // Create an 8-element signal
    x = { 1, 2, 3, 4, 5, 6, 7, 8 };

    // Forward FFT
    y = rfft(x);

    // Inverse FFT recovers the original signal
    z = rffti(y);

    print "Original x:";
    print x;
    print "Recovered via rffti:";
    print z;

The above code produces the following output:

::

    Original x:

       1.0000000
       2.0000000
       3.0000000
       4.0000000
       5.0000000
       6.0000000
       7.0000000
       8.0000000

    Recovered via rffti:

       1.0000000
       2.0000000
       3.0000000
       4.0000000
       5.0000000
       6.0000000
       7.0000000
       8.0000000

.. seealso:: Functions :func:`rfft`, :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`
