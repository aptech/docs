
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

    :type y: LxM real matrix

Remarks
-------

It is up to the user to guarantee that the input will return a real result. If in doubt, use :func:`ffti`.

.. seealso:: Functions :func:`rfft`, :func:`fft`, :func:`ffti`, :func:`fftm`, :func:`fftmi`

