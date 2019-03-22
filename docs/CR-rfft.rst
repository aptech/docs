
rfft
==============================================

Purpose
----------------

Computes a real 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: rfft(x)

    :param x: 
    :type x: NxK real matrix

    :returns: y (*LxM matrix*), where L and M are the smallest powers of 2 greater than or equal to N and K, respectively.



Remarks
-------

Computes the RFFT of x, scaled by 1/(L*M).

This uses a Temperton Fast Fourier algorithm.

If N or K is not a power of 2, x will be padded out with zeros before
computing the transform.

.. seealso:: Functions :func:`rffti`, :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`
