
ffti
==============================================

Purpose
----------------

Computes an inverse 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: y = ffti(x)

    :param x: The values used to compute the inverse Fast Fourier transform.
    :type x: NxK matrix

    :return y: where *L* and *M* are the smallest prime factor products greater than or equal to *N* and *K*, respectively.

    :type y: LxM matrix

Examples
----------------

::

    x = { 8 1 6,
          3 5 7,
          4 9 2 };

    x_ffti = ffti(fft(x));

    print real(x_ffti);

After the code:

::

    8.0000   1.0000   6.0000   0.0000
    3.0000   5.0000   7.0000   0.0000
    4.0000   9.0000   2.0000   0.0000
    0.0000   0.0000   0.0000   0.0000
    
Remarks
-------

Computes the inverse Fourier Fast transform of *x*, scaled by :math:`1/N`.

This uses a Temperton prime factor Fast Fourier algorithm.

.. seealso:: Functions :func:`fft`, :func:`rfft`, :func:`rffti`
