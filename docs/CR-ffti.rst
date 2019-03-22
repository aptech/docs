
ffti
==============================================

Purpose
----------------

Computes an inverse 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: ffti(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*LxM matrix*), where L and M are the smallest prime factor products greater than or equal to N and K, respectively.



Remarks
-------

Computes the inverse FFT of x, scaled by 1/N.

This uses a Temperton prime factor Fast Fourier algorithm.

.. seealso:: Functions :func:`fft`, :func:`rfft`, :func:`rffti`
