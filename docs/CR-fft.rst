
fft
==============================================

Purpose
----------------

Computes a 1- or 2-D Fast Fourier transform.

Format
----------------
.. function:: fft(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*LxM matrix*), where *L* and *M* are the smallest powers of 2 greater than or equal to *N* and *K*, respectively.

Remarks
-------

This computes the FFT of *x*, scaled by :math:`1/N`.

This uses a Temperton Fast Fourier algorithm.

If *N* or *K* is not a power of 2, *x* will be padded out with zeros before computing the transform.

.. seealso:: Functions :func:`ffti`, :func:`rfft`, :func:`rffti`

