
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

.. seealso:: Functions :func:`rffti`, :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`
